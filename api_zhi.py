# --- 虽有多闻 若不修行 与不闻等 如人说食 终不能饱


import os
import json
import time
import base64
import argparse
from threading import Thread
from tools.ocrService import OCR
from tools.showTime import electronic_clock
from tools.completeOther import complete_it
from tools.getFullPath import through_full_path
from tools.cutListUWant import customize_cut_list
from tools.originFileName import get_the_filename


class Api:


    def __init__(self, data, output_path, server, main_scene, sub_scene, index_num, depends, count=None, vers=None):
        """
        data: 完整输入路径
        output_path: 输出路径
        server: 服务地址
        main_scene: 一级预估目录
        sub_scene: 二级预估目录
        index_num: 路径长度定位值
        depends: 输出类型
        count: 计数器
        vers: OCR版本
        return: None
        """
        self.data = data
        self.output_path = output_path
        self.server = server
        self.main_scene = main_scene
        self.sub_scene = sub_scene
        self.index_num = index_num
        self.depends = depends
        self.count = count
        self.vers = vers


    def json_way(self, finalot_upper, ocrd_upper):
        """json输出逻辑"""
        json_format_name = get_the_filename(self.data, self.index_num, 'json')
        with open(os.path.join(finalot_upper[0], json_format_name), 'w') as d:
            json.dump(ocrd_upper, d, indent=4, ensure_ascii=False)
        if self.count: print('No.{} completed, named {}'.format(self.count, json_format_name))
        else: print('Json sample 「 {} 」 completed'.format(json_format_name))


    def excel_way(self, fin_up, ocr_up):
        """excel输出逻辑"""
        excel_format_name = get_the_filename(self.data, self.index_num, 'excel')
        excel_data = base64.b64decode(ocr_up['data']['resultFile'])
        with open(os.path.join(fin_up[0], excel_format_name), 'wb') as d: d.write(excel_data)
        if self.count: print('No.{} completed, named {}'.format(self.count, excel_format_name))
        else: print('Excel sample 「 {} 」 completed'.format(excel_format_name))


    def crossroads(self, final_ot, ocr_d):
        """十字路口 """
        try:
            # 作何抉择，以何输出
            if self.depends == 'json': self.json_way(final_ot, ocr_d)
            elif self.depends == 'excel': self.excel_way(final_ot, ocr_d)
        except Exception: pass


    def final_produce(self):
        """最终产出逻辑"""
        try:
            # 获取预估识别结果
            ocr_data = OCR(self.server, self.data, self.main_scene, self.sub_scene, self.vers).post_request()
            # 输出路径创建
            final_output = complete_it(self.data, self.output_path, self.index_num)
            # 十字路口
            self.crossroads(final_output, ocr_data)
        except Exception: print(get_the_filename(self.data, self.index_num, '') + ' failed!')


if __name__ == '__main__':
    local_server, main_sce, sub_sce, ver, thread_nums = 'http://127.0.0.1:8506', 'general', 'print', '110', 5

    parser = argparse.ArgumentParser(description='The script serves AutoOCR')
    parser.add_argument('-i', '--input_folder', help='Input folder path (only folder)', type=str, default='')
    parser.add_argument('-s', '--save_folder', help='Save folder path (only folder)', type=str, default='')
    parser.add_argument('-ot', '--out_type', help='Which output type you want (Default "json")', type=str, default='json')
    parser.add_argument('-w', '--different_way', help='Which way you want, thread or single (Default "thread")', type=str, default='thread')
    args = parser.parse_args()
    if args.input_folder[-1] != '/': args.input_folder += '/'
    if args.save_folder[-1] != '/': args.save_folder += '/'

    print('----------------- Start the process -----------------')
    start = time.perf_counter()

    if args.different_way == 'thread':
        # 资源整理
        data_list = [item for item in through_full_path(args.input_folder)]
        new_data_li = customize_cut_list(data_list, thread_nums)
        # 调用主函数
        def main_process(input_da):
            for img_data in input_da:
                Api(img_data, args.save_folder, local_server,
                            main_sce, sub_sce, len(args.input_folder), args.out_type, vers=ver).final_produce()
        # 多线程环节
        threads = [Thread(target=main_process, args=[block]) for block in new_data_li]
        for thd in threads: thd.start()
        for item in threads: item.join()
    elif args.different_way == 'single':
        origin_count = 1
        for img_data in (item for item in through_full_path(args.input_folder)):
            Api(img_data, args.save_folder, local_server, main_sce, sub_sce, len(args.input_folder),
                        args.out_type, origin_count, vers=ver).final_produce()
            origin_count += 1

    stop = time.perf_counter() - start
    final_show = electronic_clock(stop)
    hour, minute, second = final_show[0], final_show[1], final_show[2]
    print('Time consumption of AutoOCR is 「 %02d : %02d : %02d 」' % (hour, minute, second))
    print('-------------- All process is complete --------------')

# --- 虽有多闻 若不修行 与不闻等 如人说食 终不能饱


import time
import fitz
import argparse
from tools.randomStr import random_s
from tools.showTime import calculate_time
from tools.showTime import electronic_clock
from tools.completeOther import complete_it
from tools.getFullPath import through_full_path


class Pdf2Img:


    def __init__(self, open_file_path, save_file_path, index_num, platform, crossroad):
        """
        open_file_path: 完整输入路径
        save_file_path: 输出路径
        index_num: 路径长度定位值
        platform: 操作系统环境
        crossroad: 十字路口
        """
        self.open_file_path = open_file_path
        self.save_file_path = save_file_path
        self.index_num = index_num
        self.platform = platform
        self.crossroad = crossroad
        self.folder_symbol = '/'
        if self.platform == 'windows': self.folder_symbol = '\\'


    def full_way(self, fpdf, ftrans, forigin_name):
        """全量及原文件名输出"""
        full_output = complete_it(self.open_file_path, self.save_file_path,
                                  self.index_num, forigin_name + self.folder_symbol, self.folder_symbol)
        for i in range(fpdf.pageCount):
            pm = fpdf[i].getPixmap(matrix=ftrans, alpha=False)
            pm.writePNG(full_output[0] + self.folder_symbol + '%s.png' % (forigin_name  + '-' + str(i + 1)))


    def random_way(self, rpdf, rtrans, rrandom_sign):
        """全量及随机文件名输出"""
        random_output = complete_it(self.open_file_path, self.save_file_path,
                                    self.index_num, rrandom_sign + self.folder_symbol, self.folder_symbol)
        for i in range(rpdf.pageCount):
            pm = rpdf[i].getPixmap(matrix=rtrans, alpha=False)
            random_name = rrandom_sign + '-' + str(i + 1)
            pm.writePNG(random_output[0] + self.folder_symbol + '%s.png' % random_name)


    def first_page_way(self, fppdf, fptrans, fporigin_name):
        """仅首页及原文件名输出"""
        final_output = complete_it(self.open_file_path, self.save_file_path, self.index_num, symbol=self.folder_symbol)
        pm = fppdf[0].getPixmap(matrix=fptrans, alpha=False)
        pm.writePNG(final_output[0] + self.folder_symbol + '%s.png' % fporigin_name )


    @calculate_time
    def main_process(self):
        """主转化逻辑"""
        if self.open_file_path.split(self.folder_symbol)[-1].split('.')[1] != 'pdf': return
        # zoom_x, zoom_y --> 图像质量
        rotate, zoom_x, zoom_y = int(0), 2.33, 2.33
        # pdf关键参数
        trans, pdf = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate), fitz.open(self.open_file_path)
        # 随机或原名产出前置
        random_sign, origin_name = random_s(), self.open_file_path.split(self.folder_symbol)[-1].split('.')[0].replace(' ', '_')
        if self.crossroad == 'full': self.full_way(pdf, trans, origin_name)
        elif self.crossroad == 'random': self.random_way(pdf, trans, random_sign)
        elif self.crossroad == 'first': self.first_page_way(pdf, trans, origin_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='The script transfer pdf to image')
    parser.add_argument('-i', '--input_folder', help='Input folder path (only folder)', type=str, default='')
    parser.add_argument('-s', '--save_folder', help='Save folder path (only folder)', type=str, default='')
    parser.add_argument('-p', '--platform', help='Which system you live, linux or windows?', type=str, default='linux')
    parser.add_argument('-c', '--crossroad', help='Which way you want, full random or first?', type=str, default='full')
    args = parser.parse_args()

    out_symbol = '/'
    if args.platform == 'windows': out_symbol = '\\'
    if args.input_folder[-1] != out_symbol: args.input_folder += out_symbol
    if args.save_folder[-1] != out_symbol: args.save_folder += out_symbol

    print('----------------- Start the process -----------------')
    start = time.perf_counter()

    for pdf_path in (item for item in through_full_path(args.input_folder)):
        Pdf2Img(pdf_path, args.save_folder, len(args.input_folder), args.platform, args.crossroad).main_process()

    stop = time.perf_counter() - start
    final_show = electronic_clock(stop)
    hour, minute, second = final_show[0], final_show[1], final_show[2]
    print('Time consumption of PDF to Image is 「 %02d : %02d : %02d 」' % (hour, minute, second))
    print('-------------- All process is complete --------------')


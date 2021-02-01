# --- 虽有多闻 若不修行 与不闻等 如人说食 终不能饱


import cv2
import sys
import numpy as np
from tools.completeOther import complete_it
from tools.getFullPath import through_full_path
from tools.originFileName import get_the_filename


class RmRedSeal:


    def __init__(self, image_data, save_to, index, thresh=160, plat_symbol='/'):
        """
        image_data: 完整输入路径
        save_to: 输出路径
        index: 输入路径长度
        thresh: 脱粒值
        plat_symbol: 当前系统文件夹分隔符，默认Linux
        """
        self.image_data = image_data
        self.save_to = save_to
        self.index = index
        self.thresh = thresh
        self.plat_symbol = plat_symbol
        origin_data = cv2.imread(self.image_data)
        self.blue, self.green, self.red = cv2.split(origin_data)


    def save_method(self, after_img):
        """输出逻辑"""
        out_where = complete_it(self.image_data, self.save_to, self.index, symbol=self.plat_symbol)
        file_name = get_the_filename(self.image_data, self.index, 'jpg', self.plat_symbol)
        cv2.imwrite(out_where[0] + file_name, after_img)


    def main_process(self):
        """主逻辑"""
        if not self.image_data: return
        # 转换图像
        after = cv2.threshold(self.red, self.thresh, 255, cv2.THRESH_BINARY)[1]
        return self.save_method(after)


if __name__ == "__main__":
    # 输入路径 输出路径 脱粒值
    # 脱粒值应根据实际需求做出更改
    input_way, save_way, thresh_way, symb = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    for img_data in (img for img in through_full_path(input_way)):
        RmRedSeal(img_data, save_way, len(input_way), int(thresh_way), symb).main_process()
    print('Process done')
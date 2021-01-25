# --- 虽有多闻 若不修行 与不闻等 如人说食 终不能饱


import cv2
import base64
import numpy as np
from PIL import Image
from io import BytesIO
import pyzbar.pyzbar as pyz


class CvMultMethod:


    @staticmethod
    def byte2ndarray(b2n_data_image):
        """Convert buffer to ndarray"""
        one_array = np.frombuffer(b2n_data_image, np.uint8)
        return cv2.imdecode(one_array, cv2.IMREAD_COLOR)


    @staticmethod
    def ndarray2byte(ndarray_image):
        """Convert ndarray to byte"""
        img_barray = BytesIO()
        Image.fromarray(ndarray_image).save(img_barray, format='PNG', quality=95)
        return img_barray.getvalue()


    @staticmethod
    def crop_image(ci_data_image, list_bboxes):
        """
        Get a crop image
        ci_data_image: image data
        list_bboxes: bboxes list
        return: a crop image by cv2
        """
        # into a composite list
        sign = sum(list_bboxes, [])
        # get a normal list
        y0, y1, x0, x1 = sign[1], sign[5], sign[0], sign[2]
        return ci_data_image[y0:y1, x0:x1]


    @staticmethod
    def barcode_recognition(br_data_image):
        """
        br_data_image: byte data
        return: barcode information
        """
        buf2nday = CvMultMethod.byte2ndarray(br_data_image)
        gray_img = cv2.cvtColor(buf2nday, cv2.COLOR_BGR2GRAY)
        return pyz.decode(gray_img)[0].data.decode('utf-8')

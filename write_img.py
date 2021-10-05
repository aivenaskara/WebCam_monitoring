import cv2
import numpy as nm

from get_img import get_img
from time import sleep


def write_img():
    img_num = 1
    seconds_left = 50400
    while seconds_left > 0:
        img = get_img()
        img_name = 'dataset/image' + str(img_num) + '.jpg'
        cv2.imwrite(img_name, img)
        img_name = 'dataset/image' + str(img_num) + '.npy'
        nm.save(img_name, img)
        seconds_left -= 300
        img_num += 1
        sleep(240)


if __name__ == "__main__":
    write_img()

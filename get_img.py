import cv2
from config import CAM_ID, CAM_WIGHT, CAM_HEIGHT

cam_id = CAM_ID
cam_wight = CAM_WIGHT
cam_height = CAM_HEIGHT


def get_img():
    cap = cv2.VideoCapture(cam_id)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cam_wight)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)
    try:
        img = cap.read()
        cap.release()
    except cv2.error as e:
        print(e)
    return img

import cv2
from camera_config import CAM_ID, CAM_WIGHT, CAM_HEIGHT


def get_img():
    cap = cv2.VideoCapture(CAM_ID)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_WIGHT)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)
    try:
        img = cap.read()
        cap.release()
    except cv2.error as e:
        print(e)
    return img

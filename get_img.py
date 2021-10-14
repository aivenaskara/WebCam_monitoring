import cv2


def get_img():
    # Set 0 if use notebook webcam or you have only one usb-webcam
    # Set 1 if you use additional webcam
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # width of video
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # height of video
    try:
        ret, img = cap.read()
        cap.release()
    except cv2.error as e:
        print(e)
    return img

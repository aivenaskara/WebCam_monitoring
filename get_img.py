import cv2


def get_img():
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Ширина кадров в видеопотоке.
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Высота кадров в видеопотоке.
    try:
        ret, img = cap.read()
        cap.release()
    except cv2.error as e:
        print(e)
    return img

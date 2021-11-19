import io
import pickle

from PIL import Image
from time import sleep
from smtplib import SMTPServerDisconnected, SMTPAuthenticationError

from db import db_session
from get_img import get_img
from models import Photo
from notific_mail import send_email_warning
from human_checker import HumanChecker
from security_config import IMG_FREQUENCY, NETWORK_SENSITIVITY, EMAIL_PAUSE


def write_img():
    human_checker = HumanChecker(device='cpu', thr=NETWORK_SENSITIVITY)
    send_letter_pause = 0
    while True:
        image = get_img()
        if send_letter_pause == EMAIL_PAUSE:
            send_letter_pause = 0
        with_human, vis_image = human_checker(image)
        try:
            if with_human and send_letter_pause not in range(1, EMAIL_PAUSE):
                send_email_warning()
        # add SMTPAuthenticationError!!!
        except (SMTPServerDisconnected, SMTPAuthenticationError) as e:
            print(e)
        # BGR to RGB transformations
        vis_image = vis_image[:, :, [2, 1, 0]]
        # Transfotmation array to JPEG and write to binary string
        file_object = io.BytesIO()
        img = Image.fromarray(vis_image)
        img.save(file_object, 'JPEG')
        db_photo = pickle.dumps(file_object)
        check_result = with_human
        new_photo = Photo(
            camera_name='Home cam',
            photo=db_photo,
            detect=check_result
        )
        db_session.add(new_photo)
        db_session.commit()
        send_letter_pause += 1
        sleep(IMG_FREQUENCY)


if __name__ == "__main__":
    write_img()

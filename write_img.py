import pickle

from db import db_session
from models import Photo, RandomChecker
from get_img import get_img
from time import sleep


def write_img():
    while True:
        img = get_img()
        db_photo = pickle.dumps(img)
        random_answer = RandomChecker()
        check_result = random_answer()
        new_photo = Photo(
            camera_name='Home cam',
            photo=db_photo,
            detect=check_result
        )
        db_session.add(new_photo)
        db_session.commit()
        # Set time between image records in seconds
        sleep(5)


if __name__ == "__main__":
    write_img()

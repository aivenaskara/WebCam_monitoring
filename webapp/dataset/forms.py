from flask_wtf import FlaskForm
from wtforms import BooleanField


class DetectionON(FlaskForm):
    detection_on = BooleanField(
        'Показывать только обнаруженное движение',
        default=False,
        render_kw={"class": "form-check-input"}
    )

from webapp.db import db


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    camera_name = db.Column(db.String)
    photo = db.Column(db.BLOB)
    created_on = db.Column(db.DateTime())
    detect = db.Column(db.Boolean)

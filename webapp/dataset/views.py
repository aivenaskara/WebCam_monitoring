import base64
import pickle

from flask import Blueprint, render_template, request, url_for
from PIL import Image
from webapp.dataset.forms import DetectionON
from webapp.dataset.models import Photo

blueprint = Blueprint('dataset', __name__, url_prefix='/dataset')


@blueprint.route('/')
def index():
    title = "Архив записей"
    page = request.args.get('page', 1, type=int)
    records_list = Photo.query.filter(Photo.created_on).order_by(Photo.created_on.desc()).paginate(page, 10, False)
    next_url = url_for('dataset.index', page=records_list.next_num) \
        if records_list.has_next else None
    prev_url = url_for('dataset.index', page=records_list.prev_num) \
        if records_list.has_prev else None
    """
    form = DetectionON()
    if form.detection_on:
        records_list = Photo.query.filter(Photo.detect.is_(True)).order_by(Photo.created_on.desc()).all()
    else:
        records_list = Photo.query.filter(Photo.created_on).order_by(Photo.created_on.desc()).all()
    """
    return render_template(
        'dataset/index.html',
        page_title=title,
        records_list=records_list.items,
        next_url=next_url,
        prev_url=prev_url,
        page=page
    )


@blueprint.route('/dataset/<int:photo_id>')
def show_photo(photo_id):
    cam_photo = Photo.query.filter(Photo.id == photo_id).first()
    load_photo = pickle.loads(cam_photo.photo)
    base64img = "data:image/png;base64,"+base64.b64encode(load_photo.getvalue()).decode('ascii')
    return render_template(
        'dataset/show_photo.html',
        page_title=cam_photo.created_on.strftime('%d.%m.%Y %H:%M:%S'),
        base64img=base64img
    )

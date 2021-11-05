from flask import Blueprint, render_template
from webapp.dataset.models import Photo

blueprint = Blueprint('dataset', __name__, url_prefix='/dataset')


@blueprint.route('/')
def index():
    title = "Архив записей"
    records_list = Photo.query.filter(Photo.created_on).order_by(Photo.created_on.desc()).all()
    return render_template(
        'dataset/index.html',
        page_title=title,
        records_list=records_list
    )

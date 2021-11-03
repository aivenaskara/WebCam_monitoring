from flask import Blueprint, render_template
from webapp.dataset.models import Photo

blueprint = Blueprint('dataset', __name__)


@blueprint.route('/')
def index():
    title = "Архив записей"
    return render_template('dataset/index.html', page_title=title)

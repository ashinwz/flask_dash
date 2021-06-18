from flask import Blueprint
from flask_login import login_required

demo = Blueprint('demo', __name__, url_prefix='/')


@demo.route('/demo', methods=['GET'])
@login_required
def index():
    return "welcome demo"

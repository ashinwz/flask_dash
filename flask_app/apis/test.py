from flask import Blueprint, render_template

test = Blueprint('test', __name__, url_prefix='/')


@test.route('/', methods=['GET'])
def index():
    """Return index file (home page)"""
    return "welcome test"
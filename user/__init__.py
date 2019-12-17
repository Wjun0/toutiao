from flask import Blueprint

new_blu = Blueprint('news_b',__name__,static_folder='status')

from . import index
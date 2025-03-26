from flask import Blueprint

# __init__ >> 초기화 파일
board_bp = Blueprint('board_bp'
                     ,__name__
                     ,template_folder='templates')

from . import routes
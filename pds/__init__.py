from flask import Blueprint

# __init__ >> 초기화 파일
pds_bp = Blueprint('pds_bp'
                     ,__name__
                     ,template_folder='templates')

from . import routes
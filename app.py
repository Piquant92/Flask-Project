from flask import Flask, render_template
from board import board_bp
from pds import pds_bp

app  = Flask(__name__)

# 블루프린트 등록하기
app.register_blueprint(board_bp, url_prefix='/board')
app.register_blueprint(pds_bp, url_prefix='/pds')


@app.route('/')
def  hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)



@board_bp.route('/boardList')
def board_list():
    print("====> board_list")
    return render_template('board/board_list.html')

if __name__ == '__main__':
    app.run(debug = True)



@pds_bp.route('/pds_List')
def pds_list():
    print("====> pds_list")
    return render_template('pds/pds_list.html')

if __name__ == '__main__':
    app.run(debug = True)
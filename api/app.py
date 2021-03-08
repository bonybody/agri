# coding: utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import codecs
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_cors import CORS
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

# アプリケーションの初期化
app = Flask(__name__)

# 設定ファイルの読み込み
app.config.from_pyfile("config.py")

with app.app_context():
    from database import database

    database.init_db()

    # CORSを適応
    CORS(app)
    from plugin import auth

    jwt = auth.set_jwt(app)

    # 各コントローラーをルーティングに追加
    from controllers import register_controller_blueprint

    register_controller_blueprint(app)
    # JWT認証を追加


# アプリケーションの開始
if __name__ == '__main__':
    host = os.environ['HOST']
    port = os.environ['PORT']
    app.run(host=host, port=port, debug=True)

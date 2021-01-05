# coding: utf-8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

# アプリケーションの初期化
from flask import Flask
app = Flask(__name__)

# 設定ファイルの読み込み
app.config.from_pyfile("config/base_setting.py")

# CORSを適応
from flask_cors import CORS
CORS(app)

# JWT認証を追加
from plugin.auth import *

# 各コントローラーをルーティングに追加
import routing
routing.register_controller_blueprint(app)

if __name__ == '__main__':
  app.run()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy
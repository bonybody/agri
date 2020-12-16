# 農産物フリマサイト「アグリー」

## セットアップ
1から順番に実行していく
```bash
# 1 リポジトリのクローン
$ git clone https://github.com/bonybody/2020_hew_app.git

# 2 コンテナイメージの作成
$ docker-compose build
# ※2 コンテナイメージの作成（ビルドキャッシュを利用しない）
$ docker-compose build --no-cache

# 3 frontのモジュール群をインスール
$ docker-compose run --rm front npm install

# 4 コンテナの起動
$ docker-compose up
# ※4 コンテナの起動（logを表示しない）
$ docker-compose up -d
```

## それぞれのサービスで公開されるFQDN
- front **localhost:8001**
- api **localhost:8002**
- db **localhost:3306** ※他のデータベースが起動されているとポート（3306）が競合するので注意）

## 公式ドキュメントリンク
- [Nuxt.js（front）](https://ja.nuxtjs.org/)
- [Flask（api）](https://flask.palletsprojects.com/)
- [mariaDB（db）](https://mariadb.com/kb/ja/mariadb/)

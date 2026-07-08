# データマネジメント工学

## 概要
- データマネジメント工学で課題を解くために使用する環境の構築

## コマンド
```bash
docker compose exec mysql bash
# コンテナ内で SQL を実行する場合
mysql -u root -p "test01" < /docker-entrypoint-initdb.d/test02.sql
```
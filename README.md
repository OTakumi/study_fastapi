# このプロジェクトはなに？
FastAPI勉強用のプロジェクトです。

# Usage
DockerとDocker Composeがインストールされている環境で、以下コマンドで起動します。
```bash
docker compose up
```
起動後、ブラウザやターミナルから、localhost:8000にアクセスします。

サービスの再起動をする場合、以下のコマンドを使用する。
```bash
docker compose down && docker compose build && docker compose up
```

## 単体テストを動かすとき
```bash
docker compose --profile testing up
```

# Requirement
* Docker
* docker compose
* FastAPI
* uvicorn



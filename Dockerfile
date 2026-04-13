FROM python:3.12-slim

WORKDIR /app

# requirements.txtをコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 作業ディレクトリを作成
RUN mkdir -p /app/src /app/data

CMD ["bash"]

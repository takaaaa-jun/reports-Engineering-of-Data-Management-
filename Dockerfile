FROM python:3.12-slim

WORKDIR /app

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    curl \
    wget \
    git \
    openssh-client \
    libatomic1 \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# requirements.txtをコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 作業ディレクトリを作成
RUN mkdir -p /app/src /app/data

# MySQLクライアントのデフォルト接続設定を追加
RUN printf "[client]\nhost=mysql\nssl=FALSE\n" > /root/.my.cnf

CMD ["bash"]

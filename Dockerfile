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
    gnupg \
    && curl -fsSL https://repo.mysql.com/RPM-GPG-KEY-mysql-2025 | gpg --dearmor -o /usr/share/keyrings/mysql-keyring.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/mysql-keyring.gpg] http://repo.mysql.com/apt/debian/ bookworm mysql-8.0" > /etc/apt/sources.list.d/mysql.list \
    && apt-get update && apt-get install -y --no-install-recommends \
        mysql-community-client \
    && rm -rf /var/lib/apt/lists/*

# requirements.txtをコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 作業ディレクトリを作成
RUN mkdir -p /app/src /app/data

# MySQLクライアントのデフォルト接続設定を追加
RUN printf "[client]\nhost=mysql\nssl-mode=DISABLED\n" > /root/.my.cnf

CMD ["bash"]

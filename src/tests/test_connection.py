"""
MySQL接続テスト用スクリプト
Pythonコンテナ内で実行: python /app/src/tests/test_connection.py
"""

import os

from dotenv import load_dotenv
import mysql.connector

# .envファイルを読み込む（コンテナ外で実行する場合に必要）
load_dotenv("/app/.env", override=True)


def main():
    config = {
        "host": os.environ.get("MYSQL_HOST", "mysql"),
        "port": int(os.environ.get("MYSQL_PORT", 3306)),
        "user": os.environ.get("MYSQL_USER", "root"),
        "password": os.environ.get("MYSQL_PASSWORD", "rootpassword"),
        "database": os.environ.get("MYSQL_DATABASE", "test01").strip(),
    }

    print(f"Connecting to MySQL at {config['host']}:{config['port']}...")

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"Connected successfully! MySQL version: {version[0]}")

        cursor.execute("SELECT DATABASE()")
        current_db = cursor.fetchone()[0]
        print(f"\nCurrent database: {current_db}")

        cursor.execute("SHOW TABLES")
        print("\nTables:")
        for (table,) in cursor:
            print(f"  - {table}")

        cursor.close()
        conn.close()
        print("\nConnection test passed!")

    except mysql.connector.Error as err:
        print(f"Connection failed: {err}")
        raise


if __name__ == "__main__":
    main()

import mysql.connector as mydb
import os
from dotenv import load_dotenv

# .envファイルを読み込む (2つ上の階層にあるもの)
env_path = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(env_path)

try:
    cnx = mydb.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
    )
    
    # 接続確認用のシンプルなクエリ
    sql = "SHOW DATABASES"
    cursor = cnx.cursor()
    cursor.execute(sql)
    print(cursor.fetchall())
    
    cnx.close()
except Exception as e:
    print(f"Error: {e}")

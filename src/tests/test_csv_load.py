import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# .envの最新設定を読み込む
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.env"))
load_dotenv(env_path, override=True)

def main():
    try:
        # 環境変数から情報を取得
        host = os.environ.get("MYSQL_HOST", "mysql")
        # コンテナ外から実行された場合は 127.0.0.1 にフォールバックする簡単なチェック
        # (すでに db_connector.py に実装したのと同様の配慮)
        if host == "mysql" and not os.path.exists("/.dockerenv") and not os.path.exists("/run/secrets/kubernetes.io"):
            host = "127.0.0.1"

        port = os.environ.get("MYSQL_PORT", "3306")
        user = os.environ.get("MYSQL_USER", "root")
        password = os.environ.get("MYSQL_PASSWORD", "pass")
        database = os.environ.get("MYSQL_DATABASE", "test01").strip()

        # SQLAlchemy エンジンの作成 (PyMySQL ドライバを使用)
        db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(db_url)

        # CSVファイルの読み込み (ヘッダーがないため header=None, カラム名を明記)
        csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/test03.csv"))
        print(f"Reading CSV from: {csv_path}")
        df = pd.read_csv(
            csv_path, 
            skipinitialspace=True, 
            header=None, 
            names=['id', 'gender', 'height', 'weight', 'bmi']
        )
        print("CSV Data Preview:")
        print(df)

        # MySQLへのデータ挿入 (テーブルが存在する場合は上書き)
        table_name = "test03"
        print(f"Loading data into MySQL table '{table_name}'...")
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        print("Data loaded successfully!")

        # 挿入されたデータの確認
        from sqlalchemy import text
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT * FROM {table_name}"))
            print("\nLoaded Data in Database:")
            for row in result:
                print(row)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

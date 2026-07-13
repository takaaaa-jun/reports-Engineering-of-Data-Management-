import os
from dotenv import load_dotenv
import mysql.connector

# .envファイルを読み込む (2つ上の階層にあるもの)
env_path = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(env_path, override=True)


def main():
    try:
        print("Connecting to MySQL...")
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "mysql"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", "pass"),
            database=os.getenv("MYSQL_DATABASE", "test01").strip(),
        )
        print("Connected successfully!")
        
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"MySQL version: {version[0]}")

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


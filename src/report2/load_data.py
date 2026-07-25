import os
import mysql.connector as mydb
from pathlib import Path
from dotenv import load_dotenv

def check_path(path: Path) -> None:
    if not path.exists():
        raise FileExistsError(f"(ERROR)Path Error: {path}")
    else:
        print(f"(SUCCESS): {path}")

def main() -> None:
    current_file_path = Path(__file__).resolve()
    root_dir_path = current_file_path.parent.parent.parent
    env_file_path = root_dir_path / ".env"
    check_path(current_file_path)
    check_path(root_dir_path)
    check_path(env_file_path)
    load_dotenv(env_file_path, override=True)

    host = os.environ.get("MYSQL_HOST")
    user = os.environ.get("MYSQL_USER")
    port = os.environ.get("MYSQL_PORT")
    password = os.environ.get("MYSQL_PASSWORD")
    database = os.environ.get("MYSQL_DATABASE")
    
    cnx = mydb.connect(
        host=host,
        user=user,
        port=port,
        password=password,
        database=database
    )
    
    cur = cnx.cursor()
    cur.execute("SHOW DATABASES;")

if __name__ == "__main__":
    main()
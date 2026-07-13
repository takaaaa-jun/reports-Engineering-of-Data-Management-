# データマネジメント工学

## 環境の起動・停止（ホスト側で実行）
*   **起動**: `docker compose up -d`
*   **停止**: `docker compose down`

---

## 開発・実行方法

### 1. 統合開発環境（workspace）に入る
```bash
docker exec -it workspace bash
```

### 2. コンテナ内部での操作
`workspace` コンテナ内に入った後は、ローカル環境と同様に以下のコマンドで実行できます。

*   **Pythonファイルの実行**:
    ```bash
    python src/tests/test_connection.py
    python src/tests/test_csv_load.py
    ```
*   **MySQL CLIへの接続** (パスワード: `pass`):
    ```bash
    mysql -u root -p
    ```

---

## 簡易ランチャーの利用 (Windowsホスト用)
コマンド入力を省略したい場合は、プロジェクトルートの `run.bat` を実行してください。
- 起動: `.\run.bat` (またはダブルクリック)
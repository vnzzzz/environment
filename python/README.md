# env-python

## 初期設定

    ```bash
    docker-compose up -d --build
    docker-compose exec env-python sh start.sh 
    ```

## 次回以降

    - ターミナルで`poetry shel`を実行する
    - インタープリターを`.venv/bin/python3`に設定する
    - コンテナの`/src/src`が作業ディレクトリとなる

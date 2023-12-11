# splunk データ分析環境

## 利用手順

1. コンテナの起動

   下記のコマンドを実行

   ```bash
   docker-compose up -d --build
   ```

1. ログイン確認

   `http:///localhost:8090`で Splunk Web コンソールにアクセスし、`admin/[.envに記載したパスワード]`でログインできることを確認します。

1. index とユーザーを作成

   ローカルホスト上の PJ ディレクトリの一番上の階層で、下記コマンドを実行し、index とユーザーを作成します。

   ```bash
   ansible-playbook -i ansible/inventory/hosts ansible/prep.yml -e '{"admin":"admin","password":"password", "index":"index1", "user":"user1", "user_password":"user_password"}'
   ```

   環境変数として`-e`で渡している変数には下記を指定してください。

   - `index` : 作成したい index 名
   - `admin` : 管理者権限ユーザー名
   - `password` : 管理者権限ユーザーのパスワード
   - `user`: 作成したいユーザーの名前
   - `user_password`: 作成したいユーザーのパスワード

   なお、index を削除するときは下記コマンドを実行してください。

   ```bash
   ansible-playbook -i ansible/inventory/hosts ansible/terminate.yml -e '{"admin":"admin","password":"password", "index":"index1"}'
   ```

1. データ取り込み

   1. `docker-compose.yml`と同じ階層に`data`ディレクトリを作成し、中に csv を格納します。
      data 内に格納されているファイルはすべて取り込まれることに注意してください。

   1. ansible コマンドを実行します

      ```bash
      ansible-playbook -i ansible/inventory/hosts ansible/data_uploader.yml -e '{"admin":"admin","password":"password", "index":"index1"}'
      ```

   1. splunk web コンソールから、指定の index が作成され、index 内にデータが追加されていることを確認してください。

# test-go

## 目的

- Go 言語のお試し開発環境を用意する
- 今回 Go 言語の参考書として用いるのは下記 2 冊
  - スターティング Go 言語
  - Go プログラミング実践入門

## ディレクトリ構成

構成

- お試し環境構築時のディレクトリ構成

  ```bash
  .
  ├── .devcontainer # remote container用の設定
  │   ├── devcontainer.json
  │   └── docker-compose.yml
  ├── Dockerfile
  ├── README.md
  ├── docker-compose.yml
  └── work # ローカルマウント、この下にGoプロジェクトをぶら下げていく
      ├── first_run
      │   └── main.go
      └── first_webapp
          └── main.go
  ```

## リモート実行コマンド

基本的には、devcontainer の中で開発をすすめる

- Go のインストール確認

  ホスト側から下記を実行してコンテナ上に Go がインストールされているか確認する

  ```bash
  docker-compose exec app go version
  ```

- お試し実行

  ローカル側からコマンドで実行する(`go run` はビルドプロセスを隠蔽している)

  ```bash
  docker-compose exec app go run first_run/main.go
  ```

- ビルド -> 実行

  1. バイナリを作成する

     ```bash
     docker-compose exec -w /go/src/work/first_webapp app go mod init first_webapp
     docker-compose exec -w /go/src/work/first_webapp app go install .
     ```

  1. バイナリファイルを確認する

     ```bash
     docker-compose exec app ls -la $GOPATH/bin
     ```

  1. バイナリファイルを実行する

     ```bash
     docker-compose exec -w /go/bin app first_webapp
     ```

     `Ctrl + C` で中止

  1. ブラウザで`http://test-go.localhost/`にアクセスする

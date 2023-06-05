# 　 fastapi

- fastapi の開発環境をつくる

## 起動時

### dev/prod

dev 環境の起動時は`docker compose -f docker-compose.dev.yml up -d --build`を実行する。
dev 環境のビルド時には`Dockerfile.dev`が利用される。

### devcontaier

1. コマンドパレットで`Remote-Containers: Open Folder in Container...`を選択し、`api`を dev container で開く

   - 設定で、DB も自動で起動される

1. remote container を閉じると、コンテナは自動で Stop される

## 構築メモ

- python コードを書くときは、dev 環境で devcontainer の中で実施する
  - lint, format, 型なども見てくれるのでメリットが大きい
  - dev 環境は hot reload が有効
    - devcontainer の中でスクリプト修正・保存すると、fastapi の docs などを開いているブラウザをリロードすれば反映される
- 本番相当の環境で最新版を反映させるときは devcontainer の中で`rebuild container`する（そもそも devcontainer は使わない想定）

## Test

devcontainer の中で`poetry run pytest`

## TODO

- コンテナ・パスの dev/prod 分離の設計を考える

## References

- [FastAPI でテスト用のクリーンな DB を作成して pytest で API の Unittest を行う](https://qiita.com/bee2/items/ff9c86d8d345dbcab497)

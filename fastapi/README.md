# env-fastapi

- fastapiの開発環境をつくる

## 起動時

1. コマンドパレットで`Remote-Containers: Open Folder in Container...`を選択し、`api`をdev containerで開く

   - 設定で、DBも自動で起動される

1. remote containerを閉じると、コンテナは自動でStopされる

## 構築メモ

- pythonコードを書くときは、devcontainerの中で実施する
    lint, format, 型なども見てくれる

- 最新版を反映させるときはdevcontainerの中で`rebuild container`する

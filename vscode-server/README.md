# vscode server

## introduction

- vscode server の構築
- ローカル環境を汚さないように、vagrant で linux を立て、その上で vscode server を実行させる
- systemd で daemon 化
- token 利用あり

## command

```bash
# create nodes
vagrant up

# delete node
vagrant destory

# ssh
vagrant ssh
```

## memo

- token は openssl で生成し、/etc/vscode-server/token に格納したものを利用
- 各 VM のネットワークは各環境に合わせて修正する必要あり
- port は衝突しないように 9000 に設定

## 参考資料

- [VS Code Server の使い方](https://zenn.dev/kato_k/articles/6301d35b3d8d3c)

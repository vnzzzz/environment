# kubernetes

## introduction

`vagrant up`一発で k8s クラスターを準備する

## command

```bash
# create nodes
vagrant up

# delete node
vagrant destory

# ssh
vagrant ssh master
```

## memo

- 各 VM のネットワークは各環境に合わせて修正する必要あり
- `sshpass`+`scp`を使って join コマンドをやり取りするのは微妙か？
- `docker`や`kubectl`の sudo なしでの実行権限付与は、VM 再起動の必要あり

## 参考資料

- [Vagrant で kubeadm で Kubernetes を起動する](https://qiita.com/sotoiwa/items/67fbb50915a8eba5a4ce) ← ほとんどそのまま

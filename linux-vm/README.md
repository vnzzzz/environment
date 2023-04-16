# env-ubuntu

## 目的

- テスト用の VM を virtualbox + vagrant で作成する

## 環境

- mac
- virtual box + vagrant
- linux

## ディレクトリ構成

概説

- vagrant 設定は `./vagrant` 配下に用意する

構成

- 最終的なディレクトリ構成

  ```bash
  .
  ├── README.md
  └── vagrant
      ├── centos
      │   └── 7
      │       ├── .vagrant # vagrantコマンドで自動生成 (サブディレクトリは省略)
      │       └── Vagrantfile # vagrantコマンドで自動生成
      └── ubuntu
          └── focal64
              ├── .vagrant # vagrantコマンドで自動生成 (サブディレクトリは省略)
              └── Vagrantfile # vagrantコマンドで自動生成
  ```

## 手順

### 諸々のインストール

- virtual box

  ```terminal
  brew install --cask virtualbox
  ```

- vagrant

  ```terminal
  brew install --cask vagrant
  ```

### vagrant を利用し、virtual box 上に VM を作成する

- vagrant box を追加する
  <https://app.vagrantup.com/>から box を検索する

  - centos/7

    ```bash
    vagrant box add centos/7
    ```

    provider を何にするか聞かれるので、`3) virtualbox`を選択する

  - ubuntu

    ```bash
    vagrant box add ubuntu/focal64
    ```

    2023/2 時点で上記の box は virualbox にしか対応していないので、provider は聞かれない

- インストールした box を確認する

  ```bash
  vagrant box list
  ```

- ディレクトリ作成&移動する

  仮想マシン作成用のディレクトリ(`centos7`など)を作成し、Vagrantfile を作成する。

  ```bash
  mkdir vagrant/centos/7
  ```

  以下、`vagrant`コマンドはすべて Vagrantfile が存在するディレクトリで実行する

- Vagrantfile を作成する

  add してきた box の名前を指定し、`vagrant init`を実行して`Vagrantfile`を作成する

  ```bash
  vagrant init centos/7
  ```

  Vagrantfile の`config.vm.network "private_network"`に、バッティングしないよう適切な IP アドレスを設定する

- VM を起動する

  ```bash
  vagrant up
  ```

- VM の状態を確認する

  ```bash
  vagrant status
  ```

  Virtual Box を起動し、GUI から確認することも可能

- ssh で VM に接続する

  ```bash
  vagrant ssh
  ```

  素の ssh でログインするときは、下記を実行する

  ```bash
  ssh -i [vagrantfileがあるディレクトリ]/.vagrant/machines/default/virtualbox/private_key vagrant@[VMのIPアドレス]
  ```

  例えば Ansible や VSCode Remote で VM につなぎに行くときに利用するかもしれない

- VM をシャットダウンする

  ```bash
  vagrant halt
  ```

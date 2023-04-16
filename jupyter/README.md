# jupyter

## jupyter notebook を vscode で実行する手順のメモ

### 目的

Mac の vscode で、環境を汚さずに jupyternotebook を実行したい

### 環境

- Mac, vscode, jupyter notebook

### 手順

1. vscode をインストール

   - vscode をインストール
   - vscode 拡張で Jupyter 関連の拡張をインストール

1. pipenv をインストール

   - pipenv をインストールする

     `brew install pipenv`

   - ローカルプロジェクト内に`.venv`を作るため、環境変数で`PIPENV_VENV_IN_PROJECT = 1`を設定する

1. プロジェクトの設定

   - プロジェクトを作成する

     `mkdir [project]`

   - プロジェクトに移動する

     `cd [project]`

   - python のバージョンを指定する

     `pipenv --python 3`

1. スクリプトの実行

   - pipenv で作成した virtualenv に必要なパッケージをインストールする

     `pipenv install numpy matplotlib`

   - プロジェクト内に`.ipynb`ファイルを配置し、カーネルに venv(Pipenv Env)を選択して実行する

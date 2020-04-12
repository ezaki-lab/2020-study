# Docker Tutorial

## Installation

### Dockerのインストール

- [Docker - Installation](https://docs.docker.com/install/)
- [DockerをMacにインストールする - Qiita](https://qiita.com/kurkuru/items/127fa99ef5b2f0288b81)
- [【備忘録】【Docker奮闘記:1】Docker for Windows インストール - Qiita](https://qiita.com/manamiTakada/items/c1394e5e3358802a9446)

### ディレクトリ移動

``` change directory
cd ~/Downloads/2020-study/docker-tutorial
```

## Simple Calculator

シンプルな計算機API。

### Simple Calculator を実行

#### ビルドしてdocker imageを作る

``` build simple calculator
docker build -t simple-calculator ./simple-calculator
```

`-t`でイメージ名を指定

#### docker containerを作る

``` run simple calculator
docker run -p 4000:80 simple-calculator
```

`-p`でポート番号を指定。コンテナ内の80番をlocalhostの4000番に対応させている。

#### POSTリクエスト

``` request /sum
curl -X POST http://localhost:4000/sum \
-H 'Content-Type: application/json' \
-d '{
    "values": [1, 2, 3]
}'
```

#### レスポンス

``` response /sum
{
    "result":6
}
```

## 基礎学習

- [Dockerを基本から理解する - Qiita](https://qiita.com/yosemite2307/items/96deef2ece54dc73827c)
- [いまさらだけどDockerに入門したので分かりやすくまとめてみた - Qiita](https://qiita.com/gold-kou/items/44860fbda1a34a001fc1)
- [【図解】Dockerの全体像を理解する -前編- - Qiita](https://qiita.com/etaroid/items/b1024c7d200a75b992fc)

## 参考

- [Docker](https://www.docker.com/)
- [DockerHub](https://hub.docker.com/)

# Machine Learning Tutorial

Googleの開発した機械学習ツールのTensorflow・Kerasを使い、簡単な機械学習のモデルを理解する。

## 実施日

2020/04/06

## Installation

### 環境構築

#### Dockerのインストール

- [Docker - Installation](https://docs.docker.com/install/)
- [DockerをMacにインストールする - Qiita](https://qiita.com/kurkuru/items/127fa99ef5b2f0288b81)

#### Dockerfileを使ってTensorFlowの環境構築

- [Tensorflow - Docker](https://www.tensorflow.org/install/docker?hl=ja)

``` Pull Docker
docker pull tensorflow/tensorflow
```

## サンプルを動かしてみよう

### 線形回帰

`y = 0.1x + 0.3`をトレーニングデータとして線形回帰を行う。

- [多分もっともわかりやすいTensorFlow 入門 (Introduction) - Qiita](https://qiita.com/junichiro/items/8886f3976fc20f73335f)

#### 実行

``` 2020-study/machine-learning-tutorial
cd Users/ユーザー名/Downloads/study/machine-learning-tutorial
docker run -it --rm -v $PWD:/tmp -w /tmp tensorflow/tensorflow python ./linear-regression.py
```

### MNIST

手書き数字認識

- [tensorflow MNIST for Beginners　超初心者向け用 - Qiita](https://qiita.com/knight0503/items/a8bc13a734277e6f79a8)
- [TensorFlowに組み込まれたKerasを使う方法](https://dev.infohub.cc/use-tensorflow-keras/)

#### 実行

``` Run
cd Users/ユーザー名/Downloads/study/machine-learning-tutorial
docker run -it --rm -v $PWD:/tmp -w /tmp tensorflow/tensorflow python ./mnist.py
```

## 基礎学習

- [一から始める機械学習 - Qiita](https://qiita.com/taki_tflare/items/42a40119d3d8e622edd2)
- [機械学習の超初心者が、みんなが良いと言う記事を読んでまとめてみた - Qiita](https://qiita.com/2ko2ko/items/bae866695dfdd4a4b5b5)
- [DL4US - Lesson 0](https://github.com/matsuolab-edu/dl4us)
- [ニューラルネットワークの基礎解説：仕組みや機械学習・ディープラーニングとの関係は](https://www.sbbit.jp/article/cont1/33345)
- [畳み込みニューラルネットワークとは - Qiita](https://qiita.com/hatt0519/items/ac2ea6f9e1c993816821)

### 用語

| 用語 | 説明 | 参考 |
|---|---|---|
| Conv2D | 畳み込み層 |   |
| MaxPooling2D | プーリング層 | [【入門者向け解説】プーリング処理入門(TensorFlowで説明)](https://qiita.com/FukuharaYohei/items/73cce8f5707a353e3c3a) |
| Dropout | ドロップアウト層 | [【Deep Learning with Python】ドロップアウト](https://liaoyuan.hatenablog.jp/entry/2018/02/19/195637) |
| Dense | 通常の結合層 |   |
| Reshape | データの変形（任意次元に） |   |
| Flatten | データの変形（1 次元に） |   |

## 参考

- [TensorFlow](https://www.tensorflow.org/)
- [TensorFlow - GitHub](https://github.com/tensorflow/tensorflow)
- [Docker](https://www.docker.com/)
- [DockerHub](https://hub.docker.com/)

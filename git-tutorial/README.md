# Git Tutorial

Gitの基本的な使い方について理解する。

## 実施日

2020/04/13

## 環境構築

- [Gitの環境構築](https://prog-8.com/docs/git-env)

## 学習の流れ

- [サルでもわかるGit入門](https://backlog.com/ja/git-tutorial/)このサイトに沿って学習していく。

## 練習

### リモートリポジトリを作成

Githubにログインして、新しいリポジトリを作成する。

![img](https://github.com/Tsuyoshi16416/GitTutorial/blob/master/img/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202020-04-12%2015.59.48.png?raw=true)

以下の様にリポジトリ名、説明、公開か非公開かなどを入力します。

![img](https://github.com/ezaki-lab/2020-study/blob/master/git-tutorial/img/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202020-04-12%2015.59.48.png?raw=true)

### リモートリポジトリをクローンする

リポジトリのURLをコピーする。

![img](https://github.com/Tsuyoshi16416/GitTutorial/blob/master/img/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202020-04-12%2016.40.1.png?raw=true)


ターミナルで以下のコマンドを入力して、リモートリポジトリをクローンする。

```
git clone [リモートリポジトリのURL]
```

### ファイルを作成・編集してリモートリポジトリにプッシュする

ローカルリポジトリ内でファイルでファイルを作成・編集し、以下の内容にする。

```test.txt
test1
```

リポジトリのディレクトリへ移動して以下のコマンドを入力する。

```
git add .
```

これで、変更したファイルを追跡対象にする。次に以下のコマンドを入力する。

```
git commit -m "first commit"
```

これで、ファイルの変更はリポジトリに反映される。そして、以下のコマンドを入力する。

```
git push
```

これで、リモートリポジトリにも、反映される。

![img](https://github.com/Tsuyoshi16416/GitTutorial/blob/master/img/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202020-04-12%2017.26.01.png?raw=true)

### ローカルリポジトリとリモートリポジトリを編集

まずローカルリポジトリを変更する。

先ほど作成したファイルに以下の一文を追加し、commitする。

```
ローカルリポジトリから変更
```

次に、リモートリポジトリから先ほどのファイルに以下の一文を追加する。

```
リモートリポジトリから変更
```

次に、ローカルリポジトリからリモートリポジトリへpushする。
そしたら、以下のエラーが出る

```
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Tsuyoshi16416/tutorial.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

これは、「リモートリポジトリとローカルリポジトリの内容が違っているので、同じにしてからpushして」という意味。

だからリモートリポジトリとローカルリポジトリの内容を一緒にするために以下のコマンドを入力する

```
git pull
```

するとこの様な内容が表示される。これは、「競合が起きたので修正しといて」という意味。

```
Auto-merging test.txt
CONFLICT (content): Merge conflict in test.txt
Automatic merge failed; fix conflicts and then commit the result.
```

### 競合の解決

競合が起きるとファイルは以下の様になる

```
test1
<<<<<<< HEAD
ローカルリポジトリから変更
=======
リモートリポジトリから変更
>>>>>>> a033c2897a5fb4c99403f52ecc000e4f350553cf
```

<<<<<<< HEAD >>>>>>>で囲まれた部分で競合が起きている。

=======より上か下かを選択すると競合が解決できる。いらない部分を消せばいい。

そしてpushすれば、ローカルリポジトリの内容が反映される。



## 基本コマンド
| コマンド | 説明 |
|---|---|
| init | 新しいリポジトリを作成する |
| clone | リモートリポジトリと一緒の内容のローカルリポジトリを作成する |
| add | ファイルを履歴の追跡対象にする |
| commit | ファイルの変更をリポジトリに反映させる |
| push | ローカルリポジトリの内容をリモートリポジトリに反映させる|
| pull | ローカルリポジトリをリモートリポジトリと一緒の内容にする|

## 参考
- [サルでもわかるGit入門](https://backlog.com/ja/git-tutorial/)

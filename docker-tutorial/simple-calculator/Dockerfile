# 公式 Python ランタイムを親イメージとして使用
FROM python:3.7-slim

# 作業ディレクトリを /app に設定
WORKDIR /app

# 現在のディレクトリの内容を、コンテナ内の /app にコピー
COPY . /app

# requirements.txt で指定された必要なパッケージを全てインストール
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# ポート 80 番を他のコンテナから見たこのコンテナのポートに設定（localhostには影響しない）
EXPOSE 80

# コンテナ起動時に app.py を実行
CMD ["python", "app.py"]

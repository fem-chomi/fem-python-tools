# Copyright (C) 2023 fem. All rights reserved.
from setuptools import setup, find_packages

setup(
    name='full-text-search',  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="全文テキスト検索",  # 説明
    author='fem',  # 作者名
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license='MIT'  # ライセンス
)
#!/bin/bash

pip install tqdm==4.41.1
pip install pandas==1.1.4
pip install konlpy==0.5.2
pip install Mecab
pip install kss==3.3.1.1
pip install tweepy==3.10.0
apt-get install curl git
curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh

mkdir ../data
mkdir ../data/original-data
mkdir ../data/crawling-data
mkdir ../output
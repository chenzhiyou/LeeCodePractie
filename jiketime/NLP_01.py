"""
1、读取文件
2、去除所有标点符号和换行符，并把所有大写变成小写
3、合并相同的词，统计出每个词出现的频率，并按照词频从大到小排序
4、将结果文件按行输出到文件out.txt
"""

import re


def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w]]', ' ', text)
    # 转为小写
    text = text.lower()
    # 生成所有单词的列表
    word_list = text.split(' ')
    # 去除空白单词
    word_list = filter(None, word_list)
    # 统计单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] =0
        word_cnt[word] +=1

    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_word_cnt


with open('in.txt', 'r') as fin:
    text = fin.read()
word_and_freq = parse(text)

with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))











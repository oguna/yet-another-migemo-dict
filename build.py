import re
import csv
from typing import Optional

# カタカナをひらがなに変換する
def kata2hira(hira: str) -> str:
    s = ''
    for c in list(hira):
        if ord('ァ') <= ord(c) and ord(c) <= ord('ン'):
            s += chr(ord(c) - ord('ァ') + ord('ぁ'))
        else:
            s += c
    return s

# 「漢字+(ひらがな)*」の単語を処理
p1 = re.compile('([一-鿐]+)([ぁ-ん]*)')
def convertKanjiHiraganaWord(word: str, reading: str):
    r = p1.fullmatch(word)
    if r:
        kanji = r[1]
        okurigana = r[2]
        kana = kata2hira(reading)
        if okurigana:
            if kana.endswith(okurigana):
                kana = kana[:len(kana)-len(okurigana)]
        if kana=='' or kana=='*':
            return None
        return (kana, kanji)
    else:
        return None

# 「英字+」の単語を処理
p2 = re.compile('([A-Za-z]+)')
def convertAlphabeticWord(word: str, reading: str):
    r = p2.fullmatch(word)
    if r:
        w = word.lower()
        kana = kata2hira(reading)
        return (w, kana)
    else:
        return None

if __name__ == '__main__':
    dictionary = dict()

    # 単漢字ファイルを読み込み
    with open('single_kanji.tsv', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        key = line.split('\t')[0]
        words = list(line.split('\t')[1])
        if key in dictionary:
            dictionary[key].concat(words)
        else:
            dictionary[key] = words

    # UniDicのファイルを読み込み
    with open('lex_3_1.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            word = row[0]
            reading = row[24]
            pair = convertKanjiHiraganaWord(word, reading)
            if pair:
                kana = pair[0]
                kanji = pair[1]
                if kana in dictionary:
                    dictionary[kana].append(kanji)
                else:
                    dictionary[kana] = [kanji]
            pair = convertAlphabeticWord(word, reading)
            if pair:
                kana = pair[0]
                kanji = pair[1]
                if kana in dictionary:
                    dictionary[kana].append(kanji)
                else:
                    dictionary[kana] = [kanji]
                if kanji in dictionary:
                    dictionary[kanji].append(kana)
                else:
                    dictionary[kanji] = [kana]

    # 出力
    sortedKeys = sorted(dictionary.keys())
    with open('migemo-dict', mode='w', encoding='utf-8') as f:
        for k in sortedKeys:
            f.write(k + '\t' + '\t'.join(sorted(list(set(dictionary[k])))) + '\n')
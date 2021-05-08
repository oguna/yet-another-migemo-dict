import re
import csv

dictionary = dict()

# カタカナをひらがなに変換する
def kata2hira(hira: str) -> str:
    s = ''
    for c in list(hira):
        if ord('ァ') <= ord(c) and ord(c) <= ord('ン'):
            s += chr(ord(c) - ord('ァ') + ord('ぁ'))
        else:
            s += c
    return s

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
p = re.compile('([一-鿐]+)([ぁ-ん]*)')
with open('lex_3_1.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        word = row[0]
        reading = row[24]
        r = p.fullmatch(word)
        if r:
            kanji = r[1]
            okurigana = r[2]
            kana = kata2hira(reading)
            if okurigana:
                if kana.endswith(okurigana):
                    kana = kana[:len(kana)-len(okurigana)]
                else:
                    continue
            if kana=='' or kana=='*':
                continue
            if kana in dictionary:
                dictionary[kana].append(kanji)
            else:
                dictionary[kana] = [kanji]

# 出力
sortedKeys = sorted(dictionary.keys())
with open('migemo-dict', mode='w', encoding='utf-16') as f:
    for k in sortedKeys:
        f.write(k + '\t' + '\t'.join(sorted(list(set(dictionary[k])))) + '\n')
# yet-another-migemo-dict

ライセンスの緩いMigemo用辞書を提供するプロジェクト。

C/Migemoで用いられているMigemo用辞書は、SKKプロジェクトの辞書から生成しているため、ファイルはGPLライセンス下であると考えられます。
この場合、Migemoを利用するプロジェクトでは、辞書ファイルをプログラムに同梱して配布しづらくなります。

そこで本プロジェクトでは、BSDライセンスであるMozcと、GPL/LGPL/BSDライセンスであるUniDicからMigemo用辞書を生成することで、ライセンス的に利用しやすい辞書を提供します。

## 辞書元

| ファイル | プロジェクト | ライセンス |
|---|---|---|
| single_kanji.tsv | [Mozc](https://github.com/google/mozc) | 3-clause BSD |
| lex*.csv | [UniDic](https://clrd.ninjal.ac.jp/unidic/) | GPL / LGPL / 3-clause BSD |

## 生成方法

1. [UniDic](https://clrd.ninjal.ac.jp/unidic/)から現代書き言葉フルパッケージ（例：`unidic-cwj-202302_full.zip`）をダウンロード
2. ダウンロードしたZIPに格納されている`lex*.csv` (`*`は任意の0文字以上の文字列)を、このフォルダ内にコピー
3. `python build.py`を実行し、`migmeo-dict`ファイルを生成

生成されたファイルの単語は、読みの辞書順に並んでいます。

## 格納対象の単語

`single_kanji.tsv` に格納されている漢字と読みの対応はすべて格納対象としています。

一方、`lex*.csv` からは、漢字のみか、漢字にひらがなが並んだ単語、英字のみの単語を対象としています。
（例：朝、謝まる）

## ライセンス

辞書元はどちらもBSDで配布されているため、本プロジェクトで生成した辞書もBSDとなります。
ライセンスの条項に従いご利用ください。

## TODO
- 漢字の間にひらがながある単語のサポート（例：歩み行く）
- [mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd/)の適用による最新用語のサポート

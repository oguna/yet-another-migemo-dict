import urllib.request
import os
import subprocess

UNIDIC_URL = 'https://clrd.ninjal.ac.jp/unidic_archive/2302/unidic-cwj-202302_full.zip'
MOZCDICT_URL = 'https://raw.githubusercontent.com/google/mozc/master/src/data/single_kanji/single_kanji.tsv'


def download_unidic():
    zip_filename = UNIDIC_URL.split('/')[-1]

    if not os.path.exists('lex.csv'):
        # download file from UNIDIC_URL. and save it to unidic-cwj-YYYYMM.zip
        if not os.path.exists(zip_filename):
            print(f'[unidic] downloading {zip_filename}')
            urllib.request.urlretrieve(UNIDIC_URL, zip_filename)

        # extract lex*.csv files from unidic-cwj-YYYYMM.zip
        print(f'[unidic] extracting lex*.csv files')
        subprocess.run(['unzip', '-j', zip_filename, 'lex*.csv'], check=True)

        # remove unidic-cwj-YYYYMM.zip
        print(f'[unidic] removing {zip_filename}')
        os.remove(zip_filename)
    else:
        print(f'[unidic] lex.csv already exists')


def download_mozc_dict():
    # if there's no single_kanji.tsv, download it from MOZCDICT_URL
    if not os.path.exists('single_kanji.tsv'):
        print(f'[mozc] downloading single_kanji.tsv')
        urllib.request.urlretrieve(MOZCDICT_URL, 'single_kanji.tsv')
    else:
        print(f'[mozc] single_kanji.tsv already exists')


if __name__ == '__main__':
    download_mozc_dict()
    download_unidic()

from build import convertAlphabeticWord, convertKanjiHiraganaWord, kata2hira
import unittest

class TestMethods(unittest.TestCase):
    def test_hira2kana(self):
        self.assertEqual(kata2hira('カタカナ'), 'かたかな')
        self.assertEqual(kata2hira('かたかな'), 'かたかな')

    def test_kanjiHiraganaWord(self):
        yomigana, kanji = convertKanjiHiraganaWord('漢字ひらがな', 'カンジヒラガナ')
        self.assertEqual(kanji, '漢字')
        self.assertEqual(yomigana, 'かんじ')
        pair = convertKanjiHiraganaWord('ひらがな漢字ひらがな', 'カンジヒラガナ')
        self.assertIsNone(pair)

    def test_AlphabeticWord(self):
        yomi, word = convertAlphabeticWord('ABC', 'エービーシー')
        self.assertEqual(word, 'えーびーしー')
        self.assertEqual(yomi, 'abc')
        pair = convertAlphabeticWord('あいう', 'エービーシー')
        self.assertIsNone(pair)

if __name__ == '__main__':
    unittest.main()
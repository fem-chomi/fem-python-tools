import re
import unicodedata

class NGram:
    def __init__(self):
        self.CHAR_TYPE_OTHER = 0
        self.CHAR_TYPE_ASCII = 1
        self.CHAR_TYPE_HIRAGANA = 2
        self.CHAR_TYPE_KATAKANA = 3
        self.CHAR_TYPE_ALPHA = 4
        self.CHAR_TYPE_NUMBER = 5

        self.ascii = re.compile('^[\u0020-\u007E]$')
        self.hiragana = re.compile('^[\u3041-\u3094\u3095-\u3096\u309B-\u309E]$')
        self.katakana = re.compile('^[\u30A1-\u30FA\u30FB-\u30FC]$')
        self.alpha = re.compile('^[\uFF21-\uFF3A\uFF41-\uFF5A]$')
        self.number = re.compile('^[\uFF10-\uFF19]$')

    def getCharType(self, char):
        if self.ascii.fullmatch(char):
            return self.CHAR_TYPE_ASCII
        elif self.hiragana.fullmatch(char):
            return self.CHAR_TYPE_HIRAGANA
        elif self.katakana.fullmatch(char):
            return self.CHAR_TYPE_KATAKANA
        elif self.alpha.fullmatch(char):
            return self.CHAR_TYPE_ALPHA
        elif self.number.fullmatch(char):
            return self.CHAR_TYPE_NUMBER
        else:
            return self.CHAR_TYPE_OTHER

    def zen_to_han(self, text):
        return unicodedata.normalize('NFKC', text)

    def getWordList(self, text):
        pre_char = None
        word = None
        wordList = []
        for char in text:
            if self.getCharType(char) == self.CHAR_TYPE_ASCII:
                if pre_char == self.CHAR_TYPE_ASCII:
                    word += char
                else:
                    if word != None and word.strip() != '':
                        wordList.append(word.strip())
                    word = char
                pre_char = self.CHAR_TYPE_ASCII
            elif self.getCharType(char) == self.CHAR_TYPE_HIRAGANA:
                if pre_char == self.CHAR_TYPE_HIRAGANA:
                    word += char
                else:
                    if word != None and word.strip() != '':
                        wordList.append(word.strip())
                    word = char
                pre_char = self.CHAR_TYPE_HIRAGANA
            elif self.getCharType(char) == self.CHAR_TYPE_KATAKANA:
                if pre_char == self.CHAR_TYPE_KATAKANA:
                    word += char
                else:
                    if word != None and word.strip() != '':
                        wordList.append(word.strip())
                    word = char
                pre_char = self.CHAR_TYPE_KATAKANA
            elif self.getCharType(char) == self.CHAR_TYPE_ALPHA:
                if pre_char == self.CHAR_TYPE_ALPHA:
                    word += self.zen_to_han(char)
                else:
                    if word != None and word.strip() != '':
                        wordList.append(word.strip())
                    word = self.zen_to_han(char)
                pre_char = self.CHAR_TYPE_ALPHA
            elif self.getCharType(char) == self.CHAR_TYPE_NUMBER:
                if pre_char == self.CHAR_TYPE_NUMBER:
                    word += self.zen_to_han(char)
                else:
                    if word != None and word.strip() != '':
                        wordList.append(word.strip())
                    word = self.zen_to_han(char)
                pre_char = self.CHAR_TYPE_NUMBER
            else:
                if word != None and word.strip() != '':
                    wordList.append(word.strip())
                pre_char = self.CHAR_TYPE_OTHER
                word = char
        if word != None and word.strip() != '':
            wordList.append(word.strip())
        return wordList

    def getNGramWord(self, wordList, uniMode):
        pre_word = None
        word = ''
        biGramWordList = []
        for word in wordList:
            if pre_word != None and uniMode == False:
                biGramWordList.append(pre_word + word)
            biGramWordList.append(word)
            pre_word = word
        return biGramWordList

    def getBiGram(self, text):
        biGramText = ''
        first = True
        wordList = self.getWordList(text)
        biGramWordList = self.getNGramWord(wordList, uniMode=False)
        for word in biGramWordList:
            if first:
                first = False
            else:
                biGramText += " "
            biGramText += word
        return biGramText

    def getUniGram(self, text):
        biGramText = ''
        first = True
        wordList = self.getWordList(text)
        biGramWordList = self.getNGramWord(wordList, uniMode=True)
        for word in biGramWordList:
            if first:
                first = False
            else:
                biGramText += " "
            biGramText += word
        return biGramText

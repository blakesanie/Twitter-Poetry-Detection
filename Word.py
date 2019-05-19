import nltk
from nltk.corpus import cmudict

cmu = cmudict.dict()

class Word:

    def __init__(self, text):
        self.text = text
        self.word = self.getWord(text)
        self.numSyllables = self.getNumSyllables(self.word)

    def getWord(self, text):
        for i, char in enumerate(text):
            if not char.isalpha():
                return text[0:i].lower()#might not work with hyphenated words
        return text

    def getNumSyllables(self, word):
        try:
            return [len(list(y for y in x if y[-1].isdigit())) for x in cmu[word]][0]
        except:
            return 0 #not found

    # def getSyllables(self, word):
    #     entries = cmudict.entries()
    #     return [(word, syl) for word, syl in entries if word == self.word]

    def rhymesWith(self, wordObj):
        entries = cmudict.entries()
        syllables = [(word, syl) for word, syl in entries if word == self.word]
        rhymes = []
        for (word, syllable) in syllables:
            rhymes += [word for word, pron in entries if pron[-1:] == syllable[-1:]]
        return wordObj.word in rhymes

    def __str__(self):
        return str((self.text,self.word,self.numSyllables))

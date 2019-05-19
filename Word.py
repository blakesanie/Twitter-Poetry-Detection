import nltk
from nltk.corpus import cmudict

cmu = cmudict.dict()

class Word:

    def __init__(self, text):
        self.text = text.replace('\n','')
        self.word = self.getWord(self.text)
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

    def rhymesWith(self, wordObj):
        entries = cmudict.entries()
        syllables1 = [(word, syl) for word, syl in entries if word == self.word]
        #syllables2 = [(word, syl) for word, syl in entries if word == wordObj.word]
        rhymes1 = []
        #rhymes2 = []
        for (word, syllable) in syllables1:
            rhymes1 += [word for word, pron in entries if pron[-2:] == syllable[-2:]]
        #for (word, syllable) in syllables2:
            #rhymes2 += [word for word, pron in entries if pron[-2:] == syllable[-2:]]
        return wordObj.word in rhymes1# and self.word in rhymes2

    def __str__(self):
        return str((self.text,self.word,self.numSyllables))

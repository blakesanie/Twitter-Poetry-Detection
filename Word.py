import nltk
nltk.download('cmudict')
from nltk.corpus import cmudict
cmu = cmudict.dict()
entries = cmudict.entries()
level = 2 #1 = semi rhyme, 2 = exact rhyme

class Word:

    def __init__(self, text):
        self.text = text.replace('\n',' ')
        self.word = self.getWord(self.text)
        self.numSyllables = self.getNumSyllables(self.word)
        self.rhymes = None #only compute these when needed, expensive process
        self.syllables = None

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
        if self.syllables is None:
            syllables = [(word, syl) for word, syl in entries if word == self.word]
            self.syllables = syllables
        if self.rhymes is None:
            rhymes = []
            for (word, syllable) in self.syllables:
                rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
            self.rhymes = rhymes
        return wordObj.word in self.rhymes

    def setRhymes(self, rhymes):
        self.rhymes = rhymes

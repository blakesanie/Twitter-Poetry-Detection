from Word import Word

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = self.getWords(text)
        self.totalSyllables = self.getTotalSyllables(self.words)

    def getWords(self, text):
        segments = []
        startingIndex = 0
        currentlyWord = True
        for i, char in enumerate(text):
            if char == ' ':
                currentlyWord = False
            if char.isalpha() and not currentlyWord:
                segments.append(text[startingIndex:i])
                startingIndex = i
                currentlyWord = True
        segments.append(text[startingIndex:])
        return list(map(lambda segment: Word(segment), segments))

    def getTotalSyllables(self, words):
        count = 0
        for word in words:
            count += word.numSyllables
        return count

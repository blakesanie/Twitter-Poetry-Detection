from Sentence import Sentence

def syllablesCompatable(totalSyllables):
    return totalSyllables % 4 == 0 and (totalSyllables / 4) >= 4

def syllablesContained(words, totalSyllables):
    meter = totalSyllables / 4
    syllablesCount = 0
    for word in words:
        syllablesCount += word.numSyllables
        if syllablesCount % meter < word.numSyllables and syllablesCount % meter > 0:
            return False
    return True

def getWordsToRhyme(words, totalSyllables):
    out = []
    meter = totalSyllables / 4
    syllablesCount = 0
    for word in words:
        syllablesCount += word.numSyllables
        if syllablesCount % meter == 0:
            out.append(word)
    return out

def aabbRhymes(wordsToRhyme):
    for i in range(0, len(wordsToRhyme), 2):
        print([wordsToRhyme[i].word, wordsToRhyme[i+1].word])
        if not wordsToRhyme[i].rhymesWith(wordsToRhyme[i+1]):
            return False
    return True

def ababRhymes(wordsToRhyme):
    for i in range(len(wordsToRhyme) - 2):
        if not wordsToRhyme[i].rhymesWith(wordsToRhyme[i+2]):
            return False
    return True

def isPoem(sent):
    words = sent.words
    if any(word.numSyllables is 0 for word in words):
        return False
    totalSyllables = sent.totalSyllables
    if not syllablesCompatable(totalSyllables):
        return False
    if not syllablesContained(words, totalSyllables):
        return False
    wordsToRhyme = getWordsToRhyme(words, totalSyllables)
    print(list(word.word for word in wordsToRhyme))
    return aabbRhymes(wordsToRhyme) or ababRhymes(wordsToRhyme)

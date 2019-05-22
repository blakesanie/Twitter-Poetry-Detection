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
        if not wordsToRhyme[i].rhymesWith(wordsToRhyme[i+1]):
            return False
        print("\n{}\n".format([wordsToRhyme[i].word, wordsToRhyme[i+1].word]))
    #print("aabb good")
    return True

def ababRhymes(wordsToRhyme):
    for i in range(len(wordsToRhyme) - 2):
        if not wordsToRhyme[i].rhymesWith(wordsToRhyme[i+2]):
            return False
        print("\n{}\n".format([wordsToRhyme[i].word, wordsToRhyme[i+2].word]))
    #print("abab good")
    return True

def abbaRhymes(wordsToRhyme):
    return wordsToRhyme[0].rhymesWith(wordsToRhyme[3]) and wordsToRhyme[1].rhymesWith(wordsToRhyme[2])

def repeatingWords(wordsToRhyme):
    for i in range(len(wordsToRhyme) - 1):
        for j in range(i+1, len(wordsToRhyme)):
            word1 = wordsToRhyme[i].word
            word2 = wordsToRhyme[j].word
            if word1 == word2:
                return True
    return False

def isPoem(sent):
    words = sent.words
    totalSyllables = sent.totalSyllables
    if any(word.numSyllables is 0 for word in words) or (not syllablesCompatable(totalSyllables)) or (syllablesContained(words, totalSyllables)):
        return False
    wordsToRhyme = getWordsToRhyme(words, totalSyllables)
    if not len(wordsToRhyme) == 4 or repeatingWords(wordsToRhyme):
        return False
    print(list(word.word for word in wordsToRhyme))
    return aabbRhymes(wordsToRhyme) or ababRhymes(wordsToRhyme) or abbaRhymes(wordsToRhyme)

def formatPoem(sent):
    out = ""
    syllableCount = 0
    meter = sent.totalSyllables / 4
    for word in sent.words:
        out += word.text
        syllableCount += word.numSyllables
        if syllableCount % meter == 0:
            out += "\n"
    return out

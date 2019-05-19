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
    #sent = Sentence(sentence)
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


#print(isPoem("I want to ride my bicycle"))
# import nltk
# from nltk.corpus import cmudict
#
# cmu = cmudict.dict()
#
# def getSyl(word):
#     return [len(list(y for y in x if y[-1].isdigit())) for x in cmu[word.lower()]]
#
# poemText = "We we we we free we we we we need we we we we we we we we we need"
#
# def getJustAlpha(text):
#     return ''.join([char for char in text if char.isalpha() or char == ' ']).lower()
#
# def getTotalSyllables(sylList):
#     out = 0
#     for syls in sylList:
#         out += syls
#     return out
#
# def getSyllableList(wordList):
#     out = []
#     for word in wordList:
#         out.append(getSyl(word)[0])
#     return out
#
# def rhymes(word1, word2):
#      entries = cmudict.entries()
#      syllables = [(word, syl) for word, syl in entries if word == word1]
#      rhymes = []
#      for (word, syllable) in syllables:
#              rhymes += [word for word, pron in entries if pron[-1:] == syllable[-1:]]
#      return word2 in rhymes
#
# def aabbValid(wordList):
#     for i in range(0,len(wordList)-1,2):
#         if not rhymes(wordList[i], wordList[i+1]):
#             return False
#     return True
#
# def ababValid(wordList):
#     for i in range(len(wordList)-2):
#         print(i)
#         if not rhymes(wordList[i], wordList[i+2]):
#             return False
#     return True
#
# def isPoem(text):
#     justAlpha = getJustAlpha(text)
#     wordList = justAlpha.split(' ')
#     sylList = getSyllableList(wordList)
#     totalSyls = getTotalSyllables(sylList)
#     print(totalSyls)
#     print(sylList)
#     #check lines
#     if not (totalSyls % 4 == 0 and (totalSyls / 4) >= 4):
#         return False
#     print("okay")
#     #check syllable wrap
#     sylsCount = 0
#     lineEnders = []
#     for i, syls in enumerate(sylList):
#         sylsCount += syls
#         if syls > 1 and sylsCount % (totalSyls / 4) < syls and sylsCount % (totalSyls / 4) > 0:
#             print("returning false")
#             return False
#         if sylsCount % (totalSyls / 4) == 0:
#             lineEnders.append(i)
#     endingWords = list(map(lambda i: wordList[i], lineEnders))
#     print(endingWords)
#     return aabbValid(endingWords) or ababValid(endingWords)
#
# print(isPoem(poemText))

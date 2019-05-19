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

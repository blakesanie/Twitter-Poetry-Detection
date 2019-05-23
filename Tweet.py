class Tweet:

    def __init__(self, status):
        self.text = status.text
        self.truncated = status.truncated
        self.id = status.id
        self.user = status.user.screen_name
        self.cleaned = self.cleaned()

    def isAcceptable(self):
        return not any(char.isdigit() for char in self.cleaned) and not self.text[0:2] == "RT" and not self.truncated

    def cleaned(self):
        indexOfAt = self.text.find("@")
        indexOfHash = self.text.find("#")
        indexOfLink = self.text.find("http")
        forcedEnd = max(indexOfHash, indexOfLink)
        endIndex = min(forcedEnd, len(self.text)) if forcedEnd > -1 else len(self.text)
        startIndex = 0
        if indexOfAt > -1:
            for i in range(indexOfAt,len(self.text)):
                if self.text[i] == " ":
                    startIndex = i + 1
                    break
        return self.text[startIndex:endIndex]

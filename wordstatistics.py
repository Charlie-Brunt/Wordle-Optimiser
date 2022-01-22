def letterFrequency(words):
    # intialise alphabet dictionary
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequencyDict = {}
    for letter in alphabet:
        frequencyDict[letter] = 0
    
    for word in words:
        word = word[:-1]  # gets rid of \n in words
        for letter in word:
            frequencyDict[letter] += 1

    return frequencyDict

def letterProbability(frequencyDict):
    probabilityDict = {}
    total = sum(frequencyDict.values())
    for key in frequencyDict:
        probabilityDict[key] = frequencyDict[key]/total
    
    return probabilityDict 

def wordScoresNoDuplicates(words, probabilityDict):
    """deprecated"""
    wordScoreDict = {}
    for word in words:
        word = word[:-1]  # gets rid of \n in words
        wordScoreDict[word] = 0
        lettercount = []
        for letter in word:
            if letter in lettercount:
                duplicates = True
                break
            else:
                duplicates = False
                lettercount.append(letter)
                wordScoreDict[word] += probabilityDict[letter]
        if duplicates==True:
            wordScoreDict.pop(word)

    sortedWordList = sorted(wordScoreDict.items(), key=lambda x: x[1], reverse=True)
    # remove words with repeated letters

    return sortedWordList


def wordScores(words, probabilityDict):
    wordScoreDict = {}
    for word in words:
        word = word[:-1]  # gets rid of \n in words
        wordScoreDict[word] = 0
        lettercount = []
        for letter in word:
            if letter in lettercount:
                pass
            else:
                wordScoreDict[word] += probabilityDict[letter]
                lettercount.append(letter)

    sortedWordList = sorted(wordScoreDict.items(), key=lambda x: x[1], reverse=True)
    # remove words with repeated letters

    return sortedWordList


def normalisedScores(sortedWordList):
    normalisedWordList = []
    maxScore = sortedWordList[0][1]
    minScore = sortedWordList[-1][1]
    for i in sortedWordList:
        normalisedWordList.append((i[0], (100 *(i[1] - minScore)) / (maxScore - minScore)))
    
    return normalisedWordList


def main():
    import matplotlib.pyplot as plt

    with open('answers_wordlist.txt') as f:
        words = f.readlines()

    letters = letterFrequency(words)
    sortByFrequency = sorted(letters.items(), key=lambda x: x[1], reverse=True)

    letterList = [i[0] for i in sortByFrequency]
    frequencies = [i[1] for i in sortByFrequency]

    plt.bar(letterList, frequencies)
    plt.show()

if __name__ == '__main__':
    main()

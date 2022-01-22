"""
Script to read .txt file of five-letter words and assign a score to 
each word based on the letter frequency in the same or file.

"""

import matplotlib.pyplot as plt
import numpy as np

def letterFrequency(words):
    """Takes list of strings and returns letter frequency dictionary"""
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
    """Takes letter frequency dictionary and returns probability dictionary"""
    probabilityDict = {}
    total = sum(frequencyDict.values())
    for key in frequencyDict:
        probabilityDict[key] = frequencyDict[key]/total
    
    return probabilityDict 


def wordScores(words, probabilityDict):
    """Takes list of strings and letter probabilities, and returns list of tuples (word, score)"""
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

    # sort by score
    sortedWordList = sorted(wordScoreDict.items(), key=lambda x: x[1], reverse=True)

    return sortedWordList


def normalisedScores(sortedWordList):
    """Takes score list and normalises scores based on max and min scores"""
    normalisedWordList = []
    maxScore = sortedWordList[0][1]
    minScore = sortedWordList[-1][1]
    for i in sortedWordList:
        normalisedWordList.append((i[0], (100 *(i[1] - minScore)) / (maxScore - minScore)))
    
    return normalisedWordList


def main():
    with open('answers_wordlist.txt') as f:
        answers = f.readlines()
    with open('complete_wordlist.txt') as f:
        words = f.readlines()

    frequencies = letterFrequency(answers)
    probabilities = letterProbability(frequencies)
    wordScoreList = normalisedScores(wordScores(words, probabilities))

    sortByFrequency = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    letterList = [i[0] for i in sortByFrequency]
    frequencyList = [i[1] for i in sortByFrequency]

    plt.bar(letterList, frequencyList)
    plt.title("letter vs. frequency")
    plt.show()

    wordsList = np.linspace(0, 12972, 12972)
    scoreList = [i[1] for i in wordScoreList]
    plt.plot(wordsList, scoreList)
    plt.title("word rank vs. score")
    plt.show()

if __name__ == '__main__':
    main()

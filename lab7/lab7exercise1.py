'''
Author: Aiden Barnard
KUID: 3108416
Start date: Friday, October 27, 2023
Due: Friday, November 3, 2023
Lab: Lab7Exercise1
Last modified: Friday, November 3, 2023
Purpose: To build a word counter that handles tricky punctuation
'''


#This cleans the word
def cleanLine(lineOfText):
    return lineOfText.strip().lower().replace('--',' ').replace('!',' ').replace('?',' ').replace(':',' ').replace(',',' ').replace('|',' ').replace('.',' ').replace('[',' ').replace(']',' ').replace('(',' ').replace(')',' ').replace(';',' ')


def surroundQuoteDetector(word):
    detector=False
    #The first statement in the if block ensures that the word is not an empty string
    if word and word[-1] == "'" and word[0] == "'":
        detector=True
    return detector


#Takes a dictionary and spits out a list of unique words with no numbers
def uniqueWords(word_counts_dict):
    uniqueList=[]
    for key in word_counts_dict:
        if word_counts_dict[key] == 1:
            uniqueList.append(key)
    return uniqueList


#Here is where the dictionary is made
def buildCount(text):
    documentFile=open(text, 'r')
    wordDictionary={}
    lineList=[]

    #This portion of code turns each line into its own list and adds them to a list of lists. It also strips each line and removes punctuation.
    for line in documentFile:
        #All occurrences of '!', '?', ':', ';', ',', '|', '.', '[', ']','(',')' and '--' are removed
        #I did this here because instead of in word clean because there are some weird words that have typos like ",and" or "word;--anotherWord"
        line=cleanLine(line)
        wordList=line.split(' ')
        lineList.append(wordList)

    #This part puts all the words into a dictionary
    #It also ensures that words with surrounding single quotes get treated as if there weren't any surrounding it
    for lineIndex in range(len(lineList)):
        for wordIndex in range(len(lineList[lineIndex])):
            word=lineList[lineIndex][wordIndex].strip()
            if word in wordDictionary:
                wordDictionary[word] +=1
            elif surroundQuoteDetector(word) == True and word.strip("'") in wordDictionary:
                 wordDictionary[word.strip("'")]+=1
            elif surroundQuoteDetector(word) == True:
                wordDictionary[word.strip("'")]=1
            else: 
                wordDictionary[word]=1
    documentFile.close()
    return wordDictionary


#Here is where the magic happens
def main():
    print('Welcome to the word counter!'.center(60,'='))
    #Input file retrieved from user input and dictionary is made
    documentInput=input('Enter a file name: ')
    wordDictionary=buildCount(documentInput)
    uniqueWordsList=uniqueWords(wordDictionary)

    #Output files
    wordCountFile=open('WordCount.txt','w')
    uniqueWordsFile=open('UniqueWords.txt','w')

    #wordCountFile stuff under here
    for key in wordDictionary:
        wordCountFile.write(str(wordDictionary[key])+'\t'+key+'\n')
    #uniqueWordsFile stuff under here
    for word in uniqueWordsList:
        uniqueWordsFile.write(word+'\n')

    print('The file', documentInput ,'has been processed\nOutput stored in word_data.txt and unique_words.txt\nExiting...')
    uniqueWordsFile.close()
    wordCountFile.close()
    return

main()
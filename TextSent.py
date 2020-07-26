import spacy
import csv
import pandas as pd
nlp = spacy.load('en_core_web_sm')
from textblob import TextBlob
from collections import Counter
import praw
import random






filename = "test.csv"
# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

#print(rows)
# printing the field names





top25 = []
for list in rows:
    textSP = nlp(list[2])
    for ent in textSP.ents:
        top25.append(ent.text)

#remove duplicates and count
def getDuplicatesWithCount(listOfElems):
    dictOfElems = dict()
    for elem in listOfElems:
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1
    dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
    return dictOfElems

dictOfElems = getDuplicatesWithCount(top25)
k = Counter(dictOfElems)

# Finding 3 highest values
finaltop25 = k.most_common(25)


values = ','.join(str(v) for v in finaltop25)
tempList = []
for item in finaltop25:
    tempList.append(item[0])


finalLines = []

for list in rows:
    textTB = TextBlob(list[2])
    #if objective line, then ignore
    #if(textTB.sentiment.subjectivity<0.25):
        #continue
    for check in tempList:
        if(check in list[2]):
            finalLines.append(list)

#now finalLines contains all strings with top25 entities

subredditAccuracyScore = 0

file = open('InputData.txt')
fileList = file.readlines()
newList = []
for sentence in fileList:
    newList.append(sentence.rstrip())

comparisonList = []

intlen = len(newList)
for i in range(intlen):
    if i == 1:
        continue
    doc = nlp(newList[i])
    for eye in doc.sents:
        #if(TextBlob(eye.text).sentiment.subjectivity<0.25):
            #continue
        comparisonList.append(eye.text)


#COMPARISONLIST IS COMPARISON DATA sentences
#FINALLINES ARE SUBREDDIT DATA sentences
#
origData = { i : 0 for i in tempList }
compData = { i : 0 for i in tempList }


for final in comparisonList:
    sent = TextBlob(final)
    for checker in check:
        if check in final:
            print(sent.sentiment.polarity)
            if(compData[check]==0):
                compData[check]+=sent.sentiment.polarity
            else:
                compData[check]+=sent.sentiment.polarity
                compData[check]/=2
            continue

for starter in comparisonList:
    sent = TextBlob(starter)
    for checker in check:
        if check in starter:
            print(sent.sentiment.polarity)
            if(origData[check]==0):
                origData[check]+=sent.sentiment.polarity
            else:
                origData[check]+=sent.sentiment.polarity
                origData[check]/=2
#    print(textTB.sentiment.polarity)



print(origData)
print(compData)

import spacy
import csv
import pandas as pd
nlp = spacy.load('en_core_web_sm')
from textblob import TextBlob
from collections import Counter
import matplotlib.pyplot as plt





filename = "nba.csv"
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
for kek in rows:
    textSP = nlp(kek[2])
    for ent in textSP.ents:
        if(ent.label_=='PERSON' or ent.label_=='NORP' or ent.label_=='ORG' or ent.label_=='GPE' or ent.label_=='LOC' or ent.label_=='product' or ent.label_=='EVENT' or ent.label_=='WORK_OF_ART'):
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
finaltop25 = k.most_common(100)
#print("finaltop25")
#print(finaltop25)

#finaltop25 contains [0] every most mentioned ent and [1] the amount of mentions, Ordered
#rows contains every sentence


#values = ','.join(str(v) for v in finaltop25)
tempList = []
for item in finaltop25:
    tempList.append(item[0])

#templist now contains top entities

finalLines = []

for kek in rows:
    textTB = TextBlob(kek[2])
    #if objective line, then ignore
    #if(textTB.sentiment.subjectivity<0.25):
        #continue
    for check in tempList:
        if(check in kek[2]):
            finalLines.append(kek)

#print("final Lines")
#print(finalLines)
#now finalLines contains all strings with top25 entities

subredditAccuracyScore = 0

file = open('InputData.txt')
fileList = file.readlines()
newList = []
for sentence in fileList:
    newList.append(sentence.rstrip())

#print("newlist")
#print(newList)
comparisonList = []

#finaltop25 contains all top entities
#finalLines contains all subreddit strings with top entities
#newList contains all inputted strings

subredditList = []
intCheck = len(finalLines)
for i in range(intCheck):
    if i == 1:
        continue
    doc = nlp(finalLines[i][2])
    for eye in doc.sents:
        #if(TextBlob(eye.text).sentiment.subjectivity<0.25):
            #continue
        subredditList.append(eye.text)


intlen = len(newList)
for i in range(intlen):
    if i == 1:
        continue
    doc = nlp(newList[i])
    for eye in doc.sents:
        #if(TextBlob(eye.text).sentiment.subjectivity<0.25):
            #continue
        comparisonList.append(eye.text)


#subredditList ARE SUBREDDIT DATA sentences
#COMPARISONLIST IS COMPARISON DATA sentences

origData = { i : 0 for i in tempList }
compData = { i : 0 for i in tempList }

'''
#print(origData) #subreddit data
#print(compData) #input data
print("comparison list: should be every comp input sentence")
print(subredditList)
print("templList: should be every top entity")
print(tempList)
'''

for final in comparisonList: #every inputted sentence
    sent = TextBlob(final)
    for checker in tempList: # every top entity
        if checker in final: #if the top entity is in the sentence
            if(compData[checker]==0):
                compData[checker]+=sent.sentiment.polarity
            else:
                compData[checker]+=sent.sentiment.polarity
                compData[checker]/=2
            break



for starter in subredditList:
    sent = TextBlob(starter)
    for checker in tempList:
        if checker in starter:
            if(origData[checker]==0):
                origData[checker]+=sent.sentiment.polarity
            else:
                origData[checker]+=sent.sentiment.polarity
                origData[checker]/=2
            break
#    print(textTB.sentiment.polarity)


differenceInData = {} #for measuring subredditAccuracyScore


for ticker in tempList:
    differenceInData[ticker] = origData[ticker] - compData[ticker]

print("the differenceInData graph displays how accurate based on entity the reddit is")
print("this is the subredditAccuracyScore: the number dispayed is the difference in prediction")

plt.bar(range(len(differenceInData)), list(differenceInData.values()), align='center')
plt.xticks(range(len(differenceInData)), list(differenceInData.keys()))

plt.show()

'''
averageData = {}
for ticker in tempList:
    differenceInData[ticker] = origData[ticker] + compData[ticker]
    differenceInData[ticker] = /2

print("the averageData graph displays the average prediction for you to make predictions")
print("this is the prediction score")
'''

'''
#REQUIRES THE AVERAGEDATA FUNCTION TO WORK
onlyAccurateScores = {}
for ticker in tempList:
    numStore = origData[ticker] + compData[ticker]
    if(numStore<0.25)
        onlyAccurateScores[ticker] = compData[ticker]
'''

print("The subreddit's data:")
print(origData)
print("The text's data:")
print(compData)

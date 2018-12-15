import re
import nltk
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def preprocess():
    #preprocessing
    questions = open("Questions.txt","r", encoding="utf8")
    answers = open("Answers.txt", "r", encoding="utf8")
    topics = open("Topics.txt", "r", encoding="utf8")

    newquestions = open("newquestions.txt", "w", encoding="utf8")
    newanswers = open("newanswers.txt", "w", encoding="utf8")
    newtopics = open("newtopics.txt", "w", encoding="utf8")

    array = [questions, answers, topics]
    newarray = [newquestions, newanswers, newtopics]

    for q in range(len(array)):
        for aline in array[q]:
            for i in range(len(aline)):
                if aline[i].isalpha():
                    newline = aline[i:]
                    newarray[q].write(newline)
                    break

    for file in newarray:
        file.close()
        

        
def logisticClassifier(inpQuest):
    preprocess()
    
    #putting input in right format for count vectorizer
    test = [inpQuest.lower()]
    
    quest = open("newquestions.txt", "r", encoding="utf8")
    topic = open("newtopics.txt", "r", encoding="utf8")

    classDict = {}

    questArray = quest.readlines()
    topicArray = topic.readlines()

    for i in range(len(questArray)):
        if topicArray[i].strip().lower() not in classDict:
            classDict[topicArray[i].strip().lower()] = []
        classDict[topicArray[i].strip().lower()].append(questArray[i].strip().lower())

    allquests = []
    alllabels = []
    for key in classDict:
        allquests += classDict[key]
        for question in classDict[key]:
            alllabels.append(key)
            
    #creating the count vectorizer to extract the features needed
    vectorizer = CountVectorizer(
        analyzer = 'word',
        lowercase = False,
        max_features = 300
    )
    
    features = vectorizer.fit_transform(allquests+test)

    features_nd = features.toarray()
    
    testfeats = [features_nd[-1]]
    features_nd = features_nd[:len(features_nd)-1]
    
    log_model = LogisticRegression(random_state=0, solver='sag', 
                                   multi_class='multinomial', max_iter=200)
    
    
    logModel = log_model.fit(features_nd, alllabels)
    
    
    prediction = log_model.predict(testfeats)
    return str(prediction)

    
    
def regress(afile):
    inp = open(afile,"r")
    out = open("topic_results.txt", "w")
    for aline in inp:
        out.write(logisticClassifier(aline)+"\n")
        
        
        
import sys
regress(sys.argv[1])
        

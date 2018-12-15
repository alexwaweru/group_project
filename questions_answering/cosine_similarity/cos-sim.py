import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import argparse


#Data processing 
filename1 = "Answers.txt"
filename2 = "Questions.txt"

f =  open(filename2)
f2 =  open(filename1)


q_list = []
a_list =[]

for i in f:
    q_list.append(i)

for j in f2:
    a_list.append(j)

def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('question', help='ask')
    parser = parser.parse_args()

    return parser


def cos_sim(a, b):
    """Takes 2 vectors a, b and returns the cosine similarity according 
	to the definition of the dot product
	"""
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    a = dot_product / (norm_a * norm_b)
    return a
    

# print(df2)  

def main():
    #Taking argument on command line using test question
    args = argument()
    quest = args.question
    test_question =[quest]

    #vectorizing test question
    count_vect = CountVectorizer()
    counts = count_vect.fit_transform(q_list)

    counts2 = count_vect.transform(test_question)

    vectorized = counts.toarray()
    vectorized2 = counts2.toarray()

    arrays = []
    for i in range(len(q_list)):
        arrays.append(np.array(vectorized[i]))

    output = []

    results = np.zeros((len(q_list),len(q_list)))
    max_val = 0
    cors_ans_index = 0

    #calculating the most similar vector
    for i in range(len(q_list)):
        if max_val < cos_sim(arrays[i], np.array(vectorized2[0])):
            max_val = cos_sim(arrays[i], np.array(vectorized2[0]))
            sim_sent = vectorized[i]
            cors_ans_index = i
    

    
    print("Expected Answer: ")
    print(a_list[cors_ans_index])

if __name__=="__main__":
    main()







    



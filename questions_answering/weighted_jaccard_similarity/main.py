import logging 
import numpy as np
from collections import Counter

# The files containing clean training data
questions_file_name = "../../training_data/cleaned_data/Questions.txt"
answers_file_name = "../../training_data/cleaned_data/Answers.txt"
topics_file_name = "../../training_data/cleaned_data/Topics.txt"


def answer(document, questions_filename, answers_filename):
    documents, matrix = create_word_vector(questions_filename)
    a = vectorize(document, matrix)
    max_sim = 0
    max_doc_idx = 0
    
    for i in range(len(documents)):
        b = vectorize(documents[i], matrix)
        sim = jaccard_similarity(a, b)
        if sim > max_sim:
            max_sim = sim
            max_doc_idx = i
    answers = []
    try:
        answers_file = open(answers_filename, 'r')
        for answer in (answers_file.readlines()):
            answers.append(answer)
        answers_file.close()
        answers_file.close()
    except IOError:
        logging.exception('')
    print(max_doc_idx)
    return answers[max_doc_idx]


def vectorize(document, matrix):
    """ Takes a document, a word vector and the total number of documents as inputs.
    Returns a tf-idf vector.
    """
    unique_words = list(set(matrix.elements()))
    output = []
    """ This section gets each word in the document, strips it, makes it lowercase and removes all puntuations from it"""
    document = document.strip().lower().split(' ')      #Strip and lowercase the document
    noise = " \"+*@#$%&^.,!?;:/()<>|[]"     #All possible punctuations and noise
    for word in document:
        for mark in noise:
            word = word.replace(mark,'')
    """ This section inserts the index of the """
    for i in range(len(unique_words)):
        if unique_words[i] in document:
            output.append(i)  
    return output 


def create_word_vector(input_filename):
    """ Takes a filename as input.
    Returns the the number of documents in the file, a list of all documents and a counter all uniques words.
    """
    documents = []
    unique_words = []
    noise = " \"+*@#$%&^.,!?;:/()<>|[]"     #All possible pi=unctuations and noise 
    try:
        inputfile = open(input_filename, 'r')
        for doc in (inputfile.readlines()):
            documents.append(doc)
            doc = doc.strip().lower()   #Strip and lowercase all docs in the file
            words = doc.split(' ')      #Split the doc with the space deliminiter to get all words in the doc
            for word in words:
                for mark in noise:
                    word = word.replace(mark,'')    #Replace punctuations and noise with space in each word in the doc
            unique_words = unique_words + words
        inputfile.close()
    except IOError:
        logging.exception('')
    return documents, Counter(unique_words)


def jaccard_similarity(a, b):
    """ returns the jaccard similarity between two lists """
    intersection_cardinality = len(set.intersection(*[set(a), set(b)]))
    union_cardinality = len(set.union(*[set(a), set(b)]))
    return intersection_cardinality/float(union_cardinality)


if __name__ == "__main__":
    print(answer(" Who is the head of state of Ghana?", questions_file_name, answers_file_name))
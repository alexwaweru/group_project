import logging 
import numpy as np
from collections import Counter

# The files containing clean training data
questions_file_name = "../../training_data/cleaned_data/Questions.txt"
answers_file_name = "../../training_data/cleaned_data/Answers.txt"
topics_file_name = "../../training_data/cleaned_data/Topics.txt"


def k_nearest_neighbour(document, k, questions_filename, topics_filename):
    """ Takes a document, a integer k, questions filename and topics filename as inputs.
    Returns a topic which the document belongs to.
    """
    N, documents, matrix = create_word_vector(questions_filename)
    similarities = {}
    """ This section calculates the similarity index between the test doc and each doc in the training set"""
    a = tf_idf(document, matrix, N)     #Generate a tf-idf vector for the test document
    for doc in documents:
        b = tf_idf(doc, matrix, N)   #Generate a tf-idf vector for a document in the training set
        similarity = cosine_similarity(a, b)    #Calculate the cosine similarity 
        key = doc
        value = similarity
        similarities[key] = value   #Store the similarities in a dictionary
    """ This section gets the k-nearests neighbours based on cosine similarity"""
    sorted_similarities = sorted(similarities.items(), key=lambda t: t[1], reverse=True)    #Sort the similarities dict
    k_nearest_neighbours1 = sorted_similarities[:k]     #Get the k most similar neighbours
    k_nearest_neighbours = []
    for item in k_nearest_neighbours1:
        k_nearest_neighbours.append(item[0])
    """ This section gets the topics that the k-nearest questions belong to"""
    k_nearest_topics = []
    questions = []
    topics = []
    try:
        questions_file = open(questions_filename, 'r')
        topics_file = open(topics_filename, 'r')
        for query in (questions_file.readlines()):
            questions.append(query)
        for topic in (topics_file.readlines()):
            topics.append(topic)
        questions_file.close()
        topics_file.close()
    except IOError:
        logging.exception('')
    for i in range(len(questions)):
        if questions[i] in  k_nearest_neighbours:
            k_nearest_topics.append(topics[i])
    k_nearest_topics = Counter(k_nearest_topics)
    return k_nearest_topics.most_common(1)[0][0]    #Return the topic that is most common among the k neighbors


def tf_idf(document, matrix, N):
    """ Takes a document, a word vector and the total number of documents as inputs.
    Returns a tf-idf vector.
    """
    unique_words = list(set(matrix.elements()))
    output = [0] * len(unique_words)
    """ This section gets each word in the document, strips it, makes it lowercase and removes all puntuations from it"""
    document = document.strip().lower().split(' ')      #Strip and lowercase the document
    noise = " \"+*@#$%&^.,!?;:/()<>|[]"     #All possible punctuations and noise
    for word in document:
        for mark in noise:
            word = word.replace(mark,'')
    """ This section calculates the tf-idf of each term and create a vector of the tf-idfs"""
    unique_words = list(set(matrix.elements()))     #Creates a list of uniques words 
    for i in range(len(unique_words)):
        if unique_words[i] in document:
            tf = (Counter(document))[unique_words[i]]   #Calculate the term frequency
            ni = matrix[unique_words[i]]    #Calculate number of times ith word occurs
            tfidf = tf * (N/ni)     # Calculate the term frequency - inverse document frequency of the ith word
            output[i] = tfidf   #Insert the tf-idf value in its respective index in the vector
    
    return output 


def create_word_vector(input_filename):
    """ Takes a filename as input.
    Returns the the number of documents in the file, a list of all documents and a counter all uniques words.
    """
    N = 0
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
            N = N + 1
        inputfile.close()
    except IOError:
        logging.exception('')
    return N, documents, Counter(unique_words)


def cosine_similarity(a, b):
    """ Takes 2 vectors a, b.
    Returns the cosine similarity according to the definition of the dot product
    """
    dot_product = np.dot(a,b)   #Calculate the dot product of vector a and b
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)


if __name__ == "__main__":
    print(k_nearest_neighbour(" Can you write a smart contract for \"Hello Word\" in solidity?", 10, questions_file_name, topics_file_name))
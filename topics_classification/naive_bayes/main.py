from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB 

# initialize the count vectorizer and tfidf transformer
count_vectorizer = CountVectorizer()
tfidf = TfidfTransformer()
multinomialNB = MultinomialNB()

# converts data file to array representation
def to_array(filename):
    # read input data from file
    fo = open(filename, 'r')
    # read data from file into array
    X = []
    for line in fo:
        X.append(line)
    return X

# Train the naive bayes classifier
def train(documents, classes):
    # retrieve datasets in array format
    documents = to_array(documents)
    classes = to_array(classes)

    # split dataset to training and testing
    # x_train, x_test, y_train, y_test = train_test_split(documents, classes, random_state=19)

    # convert documents to vectorized form and transform to tfidf
    x_train_counts = count_vectorizer.fit_transform(documents)
    x_train_tfidf = tfidf.fit_transform(x_train_counts)

    mNB = multinomialNB.fit(x_train_tfidf, classes)
    
    return mNB

    # # initialize vectorizer
    # tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')

def predict(x_train, y_train, input_file):
    
    # train the model with the provided document and labelled classes
    mNB = train(x_train, y_train)
    test_doc = to_array(input_file)

    # predict the respective classes for the test documents.
    y_pred = mNB.predict(count_vectorizer.transform(test_doc))

    fw = open("../../topic_results.txt", 'w+')
    for pred in  y_pred:
        fw.write(pred)
    fw.close()






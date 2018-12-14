import re

def clean_str(string):
    """
    Tokenization/string cleaning for dataset
    Every dataset is lower cased except
    """
    string = re.sub(r"\n", "", string)    
    string = re.sub(r"\r", "", string) 
    string = re.sub(r"[0-9]", "digit", string)
    string = re.sub(r"\'", "", string)    
    string = re.sub(r"\"", "", string)    
    return string.strip().lower()

def main():
    X = []
    file = open('./cleaned_data/Questions.txt', 'r', encoding="utf-8")
    for line in file:
        X.append(clean_str(line))
    
    file.close()
    for i in range(250, 278):
        print(X[i])

main()

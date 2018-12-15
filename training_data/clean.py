import re

def clean_str(string):
    """
    Tokenization/string cleaning for dataset
    Every dataset is lower cased except
    """
    string = re.sub(r"\n", "", string)    
    string = re.sub(r"\r", "", string) 
    string = re.sub(r"\'", "", string)    
    string = re.sub(r"\"", "", string)    
    return string.strip().lower()

def main():
    read_files = ['./cleaned_data/Questions.txt', './cleaned_data/Answers.txt', './cleaned_data/Topics.txt']
    write_files = ['questions.txt', 'answers.txt', 'topics.txt']

    for i in range(3):
        fopen = open(read_files[i], 'r', encoding="utf-8")
        file_write = open(write_files[i], 'w+')

        for line in fopen:
            file_write.write(clean_str(line)+"\n")
        fopen.close()
        file_write.close()

main()

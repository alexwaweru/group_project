import logging

def remove_numbers_on_the_lines():
    """
    brief:
        Cleans up original files to remove incosistencies in data format
    Raises:
        IOError: Unable to read file
    """
    # A list of original files with inconsistencies in line formats
    original_files = ["./original_data/Questions.txt",
                      "./original_data/Answers.txt",
                      "./original_data/Topics.txt"]
    
    # Cleaned data files with consistent line formats for easy processing
    cleaned_files = ["./cleaned_data/Questions.txt",
                     "./cleaned_data/Answers.txt",
                     "./cleaned_data/Topics.txt"]

    for i in range(len(original_files)):
        try:
            inputfile = open(original_files[i], 'r')
            outputfile = open(cleaned_files[i], 'w')
            n1 = list(map(lambda x:str(x), range(1,200)))
            n2 = list(map(lambda x: x+'.', n1))
            numbers = n1 + n2
            for line in (inputfile.readlines()):
                data = line.split('\t')
                if (len(data) == 1):
                    data = line.split(' ')
                    if ((len(data) > 1) and (data[0] in numbers)):
                        string = list_to_string(data[1:])
                        outputfile.write(string)
                    else:
                        string = list_to_string(data)
                        outputfile.write(string)
                elif data[0] in numbers:
                    string = list_to_string(data[1:])
                    outputfile.write(string)
                else:
                    string = list_to_string(data)
                    outputfile.write(string)
            inputfile.close()
            outputfile.close()
        except IOError:
            logging.exception('')


def list_to_string(input_list):
    string = ''
    for item in input_list:
        string = string + " " + item
    #print(string)
    return string


if __name__ == "__main__":
    remove_numbers_on_the_lines()

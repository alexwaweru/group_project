import sys
from topics_classification import topics_classifier
from questions_answering import answer_questions


def main(task, questions_file):
	if (task == "topic"):
		topis_classifier(questions_file)
	elif (task == "qa"):
		asnwer_questions(questions_file)
	else:
		print("the task \"%s\" is not supported", task) 

if __name__ == "__main__":
	input_size = len(sys.argv)
	if (ipnput_size == 3):
		# Get the terminal parameters
		task = sys.argv[1]
		questions_file = sys.argv[2]
		
		# Call the main function
		main(task, questions_file)
	else:
		input_size = input_size - 1
		print("Expected 2 inputs but %d inputs given", input_size)

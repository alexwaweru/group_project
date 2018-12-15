import sys
import topics_classification.naive_bayes.main as nb
import questions_answering.weighted_jaccard_similarity.main as wjs

# initialize dataset
dataset = {'questions':'./training_data/answers.txt', 'topics':'./training_data/topics.txt', 'answers':'./training_data/answers.txt'}

def main(task, questions_file):
	if (task == "topic"):
		nb.predict(dataset['questions'],dataset['topics'],questions_file)
	elif (task == "qa"):
		wjs.answer(questions_file,dataset['questions'],dataset['answers'])
	else:
		print("the task \"%s\" is not supported", task) 

if __name__ == "__main__":
	input_size = len(sys.argv)
	if (input_size == 3):
		# Get the terminal parameters
		task = sys.argv[1]
		questions_file = sys.argv[2]
		
		# Call the main function
		main(task, questions_file)
	else:
		input_size = input_size - 1
		print("Expected 2 inputs but %d inputs given", input_size)

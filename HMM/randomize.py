import json
import numpy

def randomize(size):
	return numpy.random.dirichlet(numpy.ones(size),size=1) #returns a list of len = size and probabilities summing upto 1

def randomize_prob(model, prob, event=''):
	if event != '':
		list_keys = initial_model[model][prob][event].keys()
		size = len(initial_model[model][prob][event])
		random_nos =  randomize(size)#list within a list

		for i in range(size):
			initial_model[model][prob][event][list_keys[i]] = random_nos[0][i]

	else:
		list_keys = initial_model[model][prob].keys()
		size = len(initial_model[model][prob])
		random_nos = randomize(size)

		for i in range(size):
			initial_model[model][prob][list_keys[i]] = random_nos[0][i]


if __name__ == '__main__':
	model_file_path = './models/recognizer.json'
	try:
		jsonfile = open(model_file_path, 'r')
		initial_model = json.load(jsonfile)
		print initial_model

		randomize_prob('hmm', 'A', 'out')
		randomize_prob('hmm', 'A', 'four')
		randomize_prob('hmm', 'A', 'six')
		randomize_prob('hmm', 'B', 'out')
		randomize_prob('hmm', 'B', 'four')
		randomize_prob('hmm', 'B', 'six')
		randomize_prob('hmm', 'pi')

		jsonfile.close()

		print initial_model

		with open(model_file_path, 'w') as jsonfile:
			json.dump(initial_model, jsonfile, indent = 4)

	except Exception as e:
		print e



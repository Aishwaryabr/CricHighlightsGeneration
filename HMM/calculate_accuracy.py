import os
from collections import Counter

output_path = './test_output/'

def accuracy():
	for dirpath, dirs, files in os.walk(output_path):
		count = 0
		no_training = 0
		for name in files:
			no_training = no_training + 1
			list_outputs = [i.strip().split()[1] for i in open(os.path.join(dirpath, name), 'r')]
			counts = Counter(list_outputs)
			max_event = max(counts, key = counts.get)
			print name, max_event
			if ("six" in name and "six" in max_event) or ("four" in name and "four" in max_event) or ("out" in name and "out" in max_event):
				count = count + 1

		return float(count) / no_training * 100


print "Accuracy" , accuracy()
from os.path import isfile, join
from scaled_hmm_sir import *
import os
import pickle

traindir = r'./training'
basedir = r'.'

train_out= join(traindir,'concatenated_outs.txt')
# train_not_out= join(traindir,'concatenated_notouts.txt')
train_four = join(traindir, 'concatenated_fours.txt')
train_six = join(traindir, 'concatenated_sixes.txt')
train_initial = join(basedir,'models/recognizer.json')

print "initialising hmm's"
hmm_out=MyHmmScaled(train_initial)
# hmm_not_out= MyHmmScaled(train_initial)
hmm_four = MyHmmScaled(train_initial)
hmm_six = MyHmmScaled(train_initial)
print "done initialising"
hmms=[hmm_out, hmm_four, hmm_six]


def generate_sequence(filename):
	input_file = file(filename,"r")
	all = input_file.read()
	lines = all.split("\n")
	lines[:]= [ line for line in lines if line!="" ]
	sequences_list = []
	index = 0
	while index < len(lines):
		sequences_list.append(lines[index:index+10])
		index = index + 10
	return sequences_list
	

if __name__ == '__main__':
	print("Generating sequences")
	# Generate sequences for training each HMM
	out_observations_list=generate_sequence(train_out)
	# print("out"+str(len(out_observations_list)))
	#print silent_observations_list
	# not_out_observations_list=generate_sequence(train_not_out)
	# print("not out "+str(len(not_out_observations_list)))
	# print single_observations_list

	four_observations_list=generate_sequence(train_four)
	# print("four"+str(len(four_observations_list)))
	six_observations_list=generate_sequence(train_six)
	# print("six"+str(len(six_observations_list)))

	# multi_observations_list=generate_sequence(train_multi)
	# print("multi"+str(len(multi_observations_list)))
	# print multi_observations_list
	hmm_save = {}
	hmm_save["out"] = dict()
	# hmm_save["not_out"] = dict()
	hmm_save["four"] = dict()
	hmm_save["six"] = dict()
	print("Training out HMM")
	# Train all the 3 HMMs with the sequences 
	print out_observations_list[0]
	print "**************"
	hmm_out.forward_backward_multi_scaled(out_observations_list)
	hmm_save["out"]["A"] = hmm_out.A
	hmm_save["out"]["B"] = hmm_out.B
	hmm_save["out"]["pi"] = hmm_out.pi

	# print("Training not out HMM")

	# hmm_not_out.forward_backward_multi_scaled(not_out_observations_list)
	# hmm_save["not_out"]["A"] = hmm_not_out.A
	# hmm_save["not_out"]["B"] = hmm_not_out.B
	# hmm_save["not_out"]["pi"] = hmm_not_out.pi

	print "Training four HMM"

	hmm_four.forward_backward_multi_scaled(four_observations_list)
	hmm_save["four"]["A"] = hmm_four.A
	hmm_save["four"]["B"] = hmm_four.B
	hmm_save["four"]["pi"] = hmm_four.pi

	print 'Training six HMM'

	hmm_six.forward_backward_multi_scaled(six_observations_list)
	hmm_save["six"]["A"] = hmm_six.A
	hmm_save["six"]["B"] = hmm_six.B
	hmm_save["six"]["pi"] = hmm_six.pi

	pickle.dump(hmm_save, open("saved_hmms.p", "wb"))

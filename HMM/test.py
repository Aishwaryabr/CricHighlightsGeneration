# from ml.hmm.myhmm_log import *;
from scaled_hmm_sir import *
import os
from os import listdir
from os.path import isfile, join
import pickle

		
outdir = r'./output'
testdir = r'./testing'
summary_file = join(outdir,"summary")
basedir = r'.'

train_initial = join(basedir,'models/recognizer.json')

hmm_out=MyHmmScaled(train_initial)
# hmm_not_out= MyHmmScaled(train_initial)
hmm_four = MyHmmScaled(train_initial)
hmm_six = MyHmmScaled(train_initial)
hmms=[hmm_out, hmm_four, hmm_six]


def get_files_list(mypath):    
    onlyfiles = [ join(mypath,f) for f in listdir(mypath) if (isfile(join(mypath,f)) and (".txt" in f))]
    return onlyfiles

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
	
def single_test(infile):
	global hmms
	states=[]
	testing_list=generate_sequence(infile)
	# state=["silent","single","multi"]
	state = ["out", "fours", "sixes"]
	hmm_save = pickle.load(open("saved_hmms.p", "rb"))
	hmm_out.A = hmm_save["out"]["A"]
	hmm_out.B = hmm_save["out"]["B"]
	hmm_out.pi = hmm_save["out"]["pi"]

	# hmm_not_out.A = hmm_save["not_out"]["A"]
	# hmm_not_out.B = hmm_save["not_out"]["B"]
	# hmm_not_out.pi = hmm_save["not_out"]["pi"]

	hmm_four.A = hmm_save["four"]["A"]
	hmm_four.B = hmm_save["four"]["B"]
	hmm_four.pi = hmm_save["four"]["pi"]

	hmm_six.A = hmm_save["six"]["A"]
	hmm_six.B = hmm_save["six"]["B"]
	hmm_six.pi = hmm_save["six"]["pi"]



	for obs in testing_list:
		results=[]
		for hmm in hmms:
			results.append(hmm.forward_scaled(obs))
			#print results
		maxval=max(results)
		# print maxval
		argmax=results.index(maxval)
		# print argmax
		states.append(state[argmax])
	return states

def loop_test(outdir,infile_list):
	accuracy_list = []
	for f in infile_list:
		fcomps = os.path.split(f) #file components path, filename
		# print 'predicting file:',fcomps[-1]
		states=[]
		states = single_test(f)
		# print states
		# print "**************************************8"
		#states_seconds = output_based_seconds(states)
		#accuracy_percent = accuracy(fcomps[-1], states_seconds)
		#print "accuracy : ",str(accuracy_percent)," %"
		#accuracy_list.append(fcomps[-1]+" : "+str(accuracy_percent)+"%")
		fn = fcomps[-1].split('.')[0] + '_op.txt'
		#print(fn)
		fn = os.path.join(outdir, fn)
		of = open(fn, 'wb')
		time = 0
		for state in states:
			of.write(str(time) + '\t' + str(state) + '\n')
			time += 50
		#print 'output file:  ', of, ' written'
		of.close()
	#of = open(summary_file,'a')
	#of.write(str(testdir.split("/")[-1])+" :\n")
	#for result in accuracy_list:
	#	of.write(result+"\n")
	#of.write("------------------------------\n")
	#of.close()
	return


if __name__ == "__main__" :
	
	# print("Training multi HMM")
	# # hmm_multi.forward_backward_multi(multi_observations_list)

	# print("Getting list of testfiles")

	# testFiles_list = get_files_list(testdir)
	# print("Testing begins")
	# loop_test(outdir, testFiles_list)
	infile = []
	for dirpath, dirname, filename in os.walk(testdir):
		infile = filename

	infile = [os.path.join(testdir, i) for i in infile]

	loop_test("test_output",infile)
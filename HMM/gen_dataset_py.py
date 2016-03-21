import scipy.io.wavfile as wav
from features import mfcc
from features import logfbank
from sklearn.cluster import KMeans
import pickle
import os
from os import listdir
from os import walk
from os.path import isfile, join
from shutil import copy2




mypath_outs = r'./inputs/outs'
mypath_fours = r'./inputs/fours'
mypath_sixes = r'./inputs/sixes'



#Function to get all the wav files given a root directory
def get_files_list(root):
    files_list = []
    for dirpath, dirnames, files in walk(root):
        for name in files:
            if name.lower().endswith(".wav"):
                files_list.append(join(dirpath,name))
    return files_list   



def vector_quantize(myfiles, type_): #given a list of files transform them to spectral vectors and compute the KMeans VQ
    for f in myfiles:
        print "Generating MFCC vectors for: ", f
        (rate, sig) = wav.read(f)
        #print rate, sig.shape
        #get the spectral vectors
        mfcc_feat = mfcc(sig,rate)
        print mfcc_feat.shape
        fcomps = f.split("/")
        file_name = fcomps[-1].split('.')[0]

        if not os.path.exists("./MFCC"):
            os.makedirs("./MFCC")

        if not os.path.exists("./MFCC/"+type_):
            os.makedirs("./MFCC/"+type_)


        pickle.dump(mfcc_feat,open("./MFCC/"+type_+"/"+file_name+"_mfcc.p","wb"))

    return
    

if __name__ == '__main__':
    
    
    myfiles = get_files_list(mypath_outs)
    vector_quantize(myfiles, "outs")

    myfiles = get_files_list(mypath_fours)
    vector_quantize(myfiles, "fours")

    myfiles = get_files_list(mypath_sixes)
    vector_quantize(myfiles, "sixes")

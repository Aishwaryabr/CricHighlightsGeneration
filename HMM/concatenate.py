import os



out_files = os.listdir("outputs/vqfiles/outs")
# notout_files = os.listdir("outputs/vqfiles/not_outs")
fours_files = os.listdir("outputs/vqfiles/fours")
sixes_files = os.listdir("outputs/vqfiles/sixes")

outs = []

not_outs = []

fours = []

sixes = []

for f in out_files:
	#print f
	outs.extend([i.strip() for i in open("outputs/vqfiles/outs/"+f,"r").readlines()])

# for f in notout_files:
# 	not_outs.extend([i.strip() for i in open("outputs/vqfiles/not_outs/"+f,"r").readlines()])

for f in fours_files:
	#print f
	fours.extend([i.strip() for i in open("outputs/vqfiles/fours/"+f,"r").readlines()])

for f in sixes_files:
	#print f
	sixes.extend([i.strip() for i in open("outputs/vqfiles/sixes/"+f,"r").readlines()])




### Note that the files are opened in append mode.
### I have sent the files containing concatenated vector values for my set of wav files
### Club that with yours or just open that file itelf here in append mode and run on your files.

o = open("./training/concatenated_outs.txt","w")
o.write("\n".join(outs) + "\n")
o.close()
# no = open("outputs/vqfiles/not_outs/concatenated_notouts.txt","a")
# no.write("\n".join(not_outs) + "\n")
# no.close()

no = open("./training/concatenated_sixes.txt","w")
no.write("\n".join(sixes) + "\n")
no.close()
no = open("./training/concatenated_fours.txt","w")
no.write("\n".join(fours) + "\n")
no.close()
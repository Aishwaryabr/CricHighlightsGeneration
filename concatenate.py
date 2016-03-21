import os



out_files = os.listdir("outputs/vqfiles/outs")
fours_files = os.listdir("outputs/vqfiles/fours")
sixes_files = os.listdir("outputs/vqfiles/sixes")

outs = []

fours = []

sixes = []

for f in out_files:
	#print f
	outs.extend([i.strip() for i in open("outputs/vqfiles/outs/"+f,"r").readlines()])

for f in fours_files:
	fours.extend([i.strip() for i in open("outputs/vqfiles/fours/"+f,"r").readlines()])

for f in sixes_files:
	sixes.extend([i.strip() for i in open("outputs/vqfiles/sixes/"+f,"r").readlines()])

### Note that the files are opened in append mode.
### I have sent the files containing concatenated vector values for my set of wav files
### Club that with yours or just open that file itelf here in append mode and run on your files.

o = open("outputs/vqfiles/outs/concatenated_outs.txt","a")
o.write("\n".join(outs) + "\n")
o.close()

fo = open("outputs/vqfiles/fours/concatenated_fours.txt","a")
fo.write("\n".join(fours) + "\n")
fo.close()

s = open("outputs/vqfiles/sixes/concatenated_sixes.txt","a")
s.write("\n".join(sixes) + "\n")
s.close()
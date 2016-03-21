#!/bin/bash

python generate_mfcc.py
python concatenate.py

file="./saved_hmms.p"
if ! [ -f "$file" ]
then
	python train.py
fi

python test.py
python calculate_accuracy.py

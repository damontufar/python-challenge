# Import os module
# Allows different operating systems to create file path
#Import sys to redirect print output to a txt file
import os
import sys

#Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#Defining Variables
nr_votes = []
candidates = []


#Open the file in read mode and store it in te variable csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile, None)

    #Columns data as lists
    for row in csvreader:
        nr_votes.append(row[0])

        if row [2] not in candidates:
            candidates.append(row[2])


         

    print(len(nr_votes))
    print(list(candidates))
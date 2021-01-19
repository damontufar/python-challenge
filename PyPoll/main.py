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
candidates_votes= []


#Open the file in read mode and store it in te variable csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile, None)

    #Columns data as lists
    for row in csvreader:
        nr_votes.append(row[0])
        candidates_votes.append(row[2])

        if row [2] not in candidates:
            candidates.append(row[2])

    #Count votes for each candidate

    khan_votes = candidates_votes.count(candidates[0])
    correy_votes = candidates_votes.count(candidates[1])
    li_votes = candidates_votes.count(candidates[2])
    otooley_votes = candidates_votes.count(candidates[3])

    #Calculate percentage of votes

    khan_percentage_votes = (khan_votes/len(nr_votes))*100
    correy_percentage_votes = (correy_votes/len(nr_votes))*100
    li_percentage_votes = (li_votes/len(nr_votes))*100
    otooley_percentage_votes = (otooley_votes/len(nr_votes))*100

    

         

    print(len(nr_votes))
    print(list(candidates))
    print(khan_percentage_votes)

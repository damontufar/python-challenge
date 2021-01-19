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

    #List of percentage votes
    percentage_votes = [khan_percentage_votes, correy_percentage_votes, li_percentage_votes, otooley_percentage_votes]
    
    #Assign the winner based on popular vote
    winner_vote = candidates[percentage_votes.index(max(percentage_votes))]

    #print and save results as txt format
    #Resource formating: https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python#:~:text=Use%20str.,float%20with%20two%20decimal%20places&text=format(number)%20with%20%22%7B,number%20with%20two%20decimal%20places.
    #Resource sys module: https://www.kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python#:~:text=Use%20sys.,output%20to%20a%20text%20file&text=stdout%20.,print%20output%20to%20the%20file.
    sys.stdout = open('pypoll_results.txt', 'w')
    print(f'''
    Election Results
    --------------------------
    Total Votes: {len(nr_votes)}
    --------------------------
    {candidates[0]}: {"{:.3f}".format(khan_percentage_votes)}% ({khan_votes})
    {candidates[1]}: {"{:.3f}".format(correy_percentage_votes)}% ({correy_votes})
    {candidates[2]}: {"{:.3f}".format(li_percentage_votes)}% ({li_votes})
    {candidates[3]}: {"{:.3f}".format(otooley_percentage_votes)}% ({otooley_votes})
    --------------------------
    Winner: {winner_vote}
    ''')

    sys.stdout.close()
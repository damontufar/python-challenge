# Import os module
# Allows different operating systems to create file path
import os

#Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Defining Variables
nr_months = 0
total_amount = 0

#Open the file in read mode and store it in te variable csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile, None)
   
    for row in csvreader:
        
        nr_months = nr_months + 1
        total_amount += int(row[1])


    #Check the results
    #print(nr_months)
    #print(total_amount)


    
    
    



    
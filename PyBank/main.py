# Import os module
# Allows different operating systems to create file path
import os

#Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Defining Variables
nr_months = 0
net_amount = []
amount_change = []

#Open the file in read mode and store it in te variable csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile, None)
   
    for row in csvreader:
        
        #+= add and asign, Reference: https://medium.com/@rinu.gour123/different-types-of-operators-in-python-a2dde168f0a8
        nr_months += 1
        net_amount.append(int(row[1]))
        
    for amount in range(1, len(net_amount)):
        amount_change.append(net_amount[amount] - net_amount[amount-1])
        avg_change = sum(amount_change)/len(amount_change)
        





    #Check the results
    #print(nr_months)
    #print(sum(net_amount))
    #print(amount_change), Resource: https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python#:~:text=Use%20str.,float%20with%20two%20decimal%20places&text=format(number)%20with%20%22%7B,number%20with%20two%20decimal%20places.
    #print("{:.2f}".format(avg_change))


    
    
    



    
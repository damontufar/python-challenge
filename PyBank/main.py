# Import os module
# Allows different operating systems to create file path
#Import sys to redirect print output to a txt file
import os
import sys

#Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Defining Variables
months = []
net_amount = []
#enter a 0 on the list because the first month does not have a change
amount_change = [0]

#Open the file in read mode and store it in te variable csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile, None)
   
    #Columns data as lists
    for row in csvreader:
        months.append(row[0])
        net_amount.append(int(row[1]))

    
    #Calculations for month over month AVG change
    for amount in range(1, len(net_amount)):
        amount_change.append(net_amount[amount] - net_amount[amount-1])
    #Len of amount_change minus the first 0 that we entered to the list
        avg_change = sum(amount_change)/(len(amount_change)-1)
    
    #Assign month and value for de greatest increase & decrease
        
        date_greatest_increase = months[amount_change.index(max(amount_change))]
        greatest_increase = max(amount_change)
        date_greatest_decrease = months[amount_change.index(min(amount_change))]
        greatest_decrease = min(amount_change)
        
    #Print the results
    #Resource formating: https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python#:~:text=Use%20str.,float%20with%20two%20decimal%20places&text=format(number)%20with%20%22%7B,number%20with%20two%20decimal%20places.
    #Resource sys module: https://www.kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python#:~:text=Use%20sys.,output%20to%20a%20text%20file&text=stdout%20.,print%20output%20to%20the%20file.
    sys.stdout = open('pybank_results.txt', 'w')
    print(f'''
    Financial Analysis
    ---------------------------------
    Total Months: {len(months)}
    Total: ${sum(net_amount)}
    Average Change: ${"{:.2f}".format(avg_change)}
    Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})
    Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})
    ''')

    sys.stdout.close()
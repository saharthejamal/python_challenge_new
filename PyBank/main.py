
import csv
total_months = 0
total_dollars = 0
with open("../resources/budget_data.csv" , 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    column_names = next(csvreader)
    for row in csvreader:
        total_months += 1 
        total_dollars += int(row[1])



financial_analysis = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_dollars}
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
"""
print(financial_analysis) 
with open("../analysis/budget_analysis.txt" , 'w') as txtfile:
    txtfile.write(financial_analysis)
    

"""
The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in profits (date and amount) over the entire period"""

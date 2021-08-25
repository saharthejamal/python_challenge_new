import csv
total_months = 0
total_dollars = 0
dollars_list = []
changes_list = []
date_list = []

with open("../resources/budget_data.csv" , 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    csvreader_copy = csvreader 
    column_names = next(csvreader)
    for row in csvreader:
        total_months += 1 
        total_dollars += int(row[1])
        dollars_list.append(int(row[1]))
        date_list.append(row[0]) 

    for i, dollar in enumerate(dollars_list):
        if i > 0:
            changes_list.append(int(dollars_list[i])-int(dollars_list[i - 1]))
        else: 
            changes_list.append(0)
        avg_change = (sum(changes_list)/len(changes_list)) 

zip_list = list(zip(date_list,changes_list))
date_max = " "
value_max = 0
date_min = " "
value_min = 0
for i in zip_list:
    if i[1] > value_max:
       value_max = i[1]
       date_max = i[0]
    if i[1] < value_min:
       value_min = i[1]
       date_min = i[0]

financial_analysis = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_dollars}
Average  Change: ${avg_change}
Greatest Increase in Profits: {date_max} ${value_max}
Greatest Decrease in Profits: {date_min} ${value_min}
"""
print(financial_analysis) 
with open("../analysis/budget_analysis.txt" , 'w') as txtfile:
    txtfile.write(financial_analysis)
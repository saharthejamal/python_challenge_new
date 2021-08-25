import csv
from typing import List
total_votes = 0
with open("../resources/election_data.csv" , 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    csvreader_copy = csvreader
    column_names = next(csvreader)
    for row in csvreader:
        total_votes += 1




   
    


        
        


election_results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
"""

print(election_results) 
with open("../analysis/election_analysis.txt" , 'w') as txtfile:
    txtfile.write(election_results)
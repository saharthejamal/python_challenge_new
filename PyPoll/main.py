import csv
from typing import List
total_votes = 0
vote_count = {}
percent_count = {}
vote_count["Khan"] = 0
vote_count["Correy"] = 0
vote_count["Li"] = 0
vote_count["O'Tooley"] = 0
percent_count["Khan"] = 0
percent_count["Correy"] = 0
percent_count["Li"] = 0
percent_count["O'Tooley"] = 0

with open("../resources/election_data.csv" , 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    csvreader_copy = csvreader
    column_names = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        vote_count[candidate] += 1
        percent_count["Khan"] = (((vote_count["Khan"])/(total_votes)) * 100)
        percent_count["Correy"] = (((vote_count["Correy"])/(total_votes)) * 100)
        percent_count["Li"] = (((vote_count["Li"])/(total_votes)) * 100)
        percent_count["O'Tooley"] = (((vote_count["O'Tooley"])/(total_votes)) * 100)
    # print(round(percent_count["Khan"]))
    # print(round(percent_count["Correy"]))
    # print(round(percent_count["Li"]))
    # print(round(percent_count["O'Tooley"]))

# print(vote_count["Khan"])


election_results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: {(round(percent_count["Khan"]))}% {vote_count["Khan"]}
Correy: {(round(percent_count["Correy"]))}% {vote_count["Correy"]}
Li: {(round(percent_count["Li"]))}% {vote_count["Li"]}
O'Tooley: {(round(percent_count["O'Tooley"]))}% {vote_count["O'Tooley"]}
-------------------------
Winner: Khan
-------------------------
"""

print(election_results) 
with open("../analysis/election_analysis.txt" , 'w') as txtfile:
    txtfile.write(election_results)
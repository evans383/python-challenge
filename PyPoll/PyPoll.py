# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#  Place holder for Total Votes to be computed later
totalvotes = 0

#  Dictionary with candidates as key for Raw Vote Counts
votecount = {"Khan": 0, "Correy": 0, "Li": 0, "O'Tooley": 0}

#  Dictionary with candidates as key for Vote Percentages
pct_votecount = {"Khan": 0, "Correy": 0, "Li": 0, "O'Tooley": 0}

#  List will be used to store strings for printed output
votestrings = []

#  Open the voter file
with open(csvpath) as votefile:
    votereader = csv.reader(votefile, delimiter=',')

#  Advance past the header row
    header = next(votereader)

#  For each vote add 1 to the appropriate key
    for record in votereader:
        votecount[record[2]] += 1

#  Sum all of the values in the ditionary
totalvotes = sum(votecount.values())

#  Calculate percentage and generate strings for all candidates in the dictionary
for candidate in votecount:
    pct_votecount[candidate] = votecount[candidate]/totalvotes*100
    votestrings.append(f"{candidate}:  {pct_votecount[candidate]:.3f}% ({votecount[candidate]})\n")

#  Get the Winner via list.index(max())) method
Winner = list(votecount.keys())[list(votecount.values()).index(max(list(votecount.values())))]

#  Produce Header string, aggregate strings for individual candidates, and produce footer string
header_str = "Election Results\n" + '-'*25 + f"\nTotal Votes:  {totalvotes}\n" + '-'*25 + '\n'
votes_str = ''.join(votestrings)
footer_str = '-'*25 + f"\nWinner:  {Winner}\n" + '-'*25

#  Full Output String
summary_str = header_str + votes_str + footer_str

#  Print String to stdio
print(summary_str)

#  Print String to file
summaryfile = open("vote_summary.txt", "w")
summaryfile.write(summary_str)
summaryfile.close()

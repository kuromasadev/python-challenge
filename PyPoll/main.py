import os
import csv

osdirectory = os.getcwd()
election_data_csv = os.path.join(osdirectory,"PyPoll","Resources","election_data.csv")

# INITIAL VARIABLE CONFIG
ballot_counts = 0
candidates = {}
winner_counts = 0
winner_candidate = ""

# Reading Import CSV file
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,
                           delimiter=',')
    election_headers = next(csvreader)

    for row in csvreader:
        # count the votes 
        ballot_counts += 1
        # aggregate the list of candidates 
        if row[2] not in candidates:
            candidates[row[2]] =0
        candidates[row[2]] +=1 

# Summary Table Items Block 1
sum_title = "Election Results" 
sum_spacer = "-------------------------"
sum_finalcts = "Total Votes:    " + str(ballot_counts)

print(sum_title)
print(sum_spacer)
print(sum_finalcts)
print(sum_spacer)

# Preparing Summary Table Block 1 for outfile print
summary_string = sum_title + "\n" + sum_spacer + "\n" + sum_finalcts + "\n" + sum_spacer + "\n"

#Summary Table Block 2
for candidate, votes in candidates.items():
    percentage = round((votes / ballot_counts) * 100, 3)
    summaryline = candidate + " : " + str(percentage) + "%" + "  (" + str(("{:,}".format(votes))) + ")"
    print(summaryline)
    # adding vote count to Summary Table Block 2 for outfile print
    summary_string += summaryline + "\n"

# calculation to find the winner
    if votes > winner_counts:
        winner_counts = votes
        winner_candidate = candidate

#Summary Table Block 3
sum_winner = "Winner:  " + winner_candidate

print(sum_spacer)
print(sum_winner)
print(sum_spacer)

# Preparing Summary Table Block 3 for outfile print
summary_string += sum_spacer + "\n" + sum_winner + "\n" + sum_spacer + "\n"

# Summary Table Final Prints all Blocks to txt file

printPyPoll = os.path.join(osdirectory,"PyPoll", "analysis", "Election_Analysis.txt")

with open(printPyPoll, 'w') as outfile:
    outfile.write(summary_string)


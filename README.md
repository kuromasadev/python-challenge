# python-challenge
 *PyBank and PyPoll*   RICE_RDA_AlbertoPonce

## PyBank Challenge

***Intent***: Provide quick financial analysis by reading into csv's, performing loops to analyze and extract data into terminal and a .txt file. 

###### Proposed Code for the challenge

```python
import os
import csv

osdirectory = os.getcwd()
budget_data_csv = os.path.join(osdirectory,"PyBank","Resources","budget_data.csv")

# Variables to be define per challenge

total_mo = 0
net_total = 0
prev_profit = 0
change_list = []
grt_increase = {"date": "", "amount": 0}
grt_decrease = {"date": "", "amount": 0}

# Reading into csv
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,
                           delimiter=',')
    next(csvreader)

    # establishing loop, counting the number of months and the net total
    for row in csvreader:
        total_mo += 1
        net_total += int(row[1])

        #calc the change in profit or loss since the previous row
        if prev_profit != 0:
            change = int(row[1]) - prev_profit
            change_list.append(change)

            #calc check to see if its the greatest increase/decrease over the period
            if change > grt_increase["amount"]:
                grt_increase["date"] = row[0]
                grt_increase["amount"] = change
            elif change < grt_decrease["amount"]:
                grt_decrease["date"] = row[0]
                grt_decrease["amount"] = change

        #storing the active profit/loss for the next loop
        prev_profit = int(row[1])
    
    #calculating the average of all Profit/Losses
    avg_change = round(sum(change_list) / len(change_list),2)

# setting up variables to print 
summary_title = "Financial Analysis"
summary_mo = "Total Months:                   " + str(total_mo)
summary_tot = "Total:                          " + str("${:,}".format(net_total))
summary_avg = "Average Change:                 " + str("${:,}".format(avg_change))
summary_grti = "Greatest Increase in Profits:   " + str(grt_increase["date"]) + " " + str("${:,}".format(grt_increase["amount"]))
summary_grtd = "Greatest Decrease in Profits:   " + str(grt_decrease["date"]) + " " + str("${:,}".format(grt_decrease["amount"]))

# writting financial analysis to terminal                                                                               
print(summary_title)
print("-----------------------------")
print(summary_mo)
print(summary_tot)
print(summary_avg)
print(summary_grti)
print(summary_grtd)

# saving file to txt
printPyBank = os.path.join(osdirectory,"PyBank", "Analysis", "Financial_Analysis.txt")

with open(printPyBank, 'w') as outfile:
    outfile.write(summary_title + "\n")
    outfile.write("-----------------------------\n")
    outfile.write(summary_mo + "\n")
    outfile.write(summary_tot + "\n")
    outfile.write(summary_grti + "\n")
    outfile.write(summary_grtd + "\n")
```

 ###### Tweaks, personalization to challenge

- added ***os.getcwd()*** to obtain the file's true directory. Path in solved exercises were unable to read the file due to having the directory as a root folder higher up. 
- formatted the totals and added tabs to the print results  for better readability 

*Original Requested format*

```text
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

***Proposed Format*** 

```text
Financial Analysis
-----------------------------
Total Months:                   86
Total:                          $22,564,198
Average Change:                 $-8,311.11
Greatest Increase in Profits:   16-Aug $1,862,002
Greatest Decrease in Profits:   14-Feb $-1,825,558
```



## PyPoll Challenge

***Intent***: Provide quick election analysis by reading into csv's, performing loops to analyze and extract data into terminal and a .txt file. 

###### Proposed Code for the Challenge

```python
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


```

 ###### Tweaks, personalization to challenge

- added ***os.getcwd()*** to obtain the file's true directory. Path in solved exercises were unable to read the file due to having the directory as a root folder higher up. 
- taking advantage of string concatenation to store the summary table information and  formatting and be able to reduce the outfile code to one line. 

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

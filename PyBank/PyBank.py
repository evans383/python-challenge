# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# path for budget data
csvpath = os.path.join('Resources', 'budget_data.csv')

# Variables that will be needed for the summary
runningprofit = 0
currentprofit = 0
initialprofit = 0
lastprofit = 0
changeinprofit = 0
changeinprofit_sum = 0
changeinprofit_avg = 0
changeinprofit_list = []
months_list = []

with open(csvpath) as budgetfile:

    budgetreader = csv.reader(budgetfile, delimiter=',')

#  Move to next line past the header
    next(budgetreader)

#  Initialize variables with the first value in the record
    record = next(budgetreader)

#  Profit for current month
    currentprofit = int(record[1])

#  Record Change in profit from previous month
    changeinprofit = currentprofit - lastprofit

#  This will store a running sum of all the changes in profit
    changeinprofit_sum += changeinprofit

#  Keep a list of all of the changes in profit.  This will be used later for statistics on profit changes
    changeinprofit_list.append(changeinprofit)

#  Individual List of Months
    months_list.append(record[0])

#  First Month's profit only collected from first record
    initialprofit = currentprofit

#  Set this months profit to previous month before going to next record
    lastprofit = currentprofit

    for record in budgetreader:

#  All variables here have the same meaning as above, but initial profit is not recorded
        currentprofit = int(record[1])
        changeinprofit = currentprofit-lastprofit
        changeinprofit_sum += changeinprofit
        changeinprofit_list.append(changeinprofit)
        months_list.append(record[0])
        lastprofit = currentprofit

#  Average Change in Profit
changeinprofit_avg = changeinprofit_sum/len(changeinprofit_list)

#  String Construction for stdio and file
header = "Financial Analysis\n"+'-'*28+'\n'
months_str = f"Total Months: {len(months_list)}\n"
total_str = f"Total: ${initialprofit-lastprofit}\n"
avg_str = f"Average Change: ${changeinprofit_avg}\n"
max_str = f"Greatest Increase in Profits:  {months_list[changeinprofit_list.index(max(changeinprofit_list))]} (${max(changeinprofit_list)})\n"
min_str = f"Greatest Decrease in Profits:  {months_list[changeinprofit_list.index(min(changeinprofit_list))]} (${min(changeinprofit_list)})\n"

#  Consolidated string
summary_str = header + months_str + total_str + avg_str + max_str + min_str

#  Print to stdio
print(summary_str)

#  Print to file
summaryfile = open("budget_summary.txt", "w")
summaryfile.write(summary_str)
summaryfile.close()


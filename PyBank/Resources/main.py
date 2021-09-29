# import the csv and os modules
import csv
import os

# load the file to read budget data
inputfile = os.path.join("budget_data.csv")

# file to hold the out of the budget analysis
outputfile = os.path.join("budget_analysis.txt")

# set variables
# initialize the variables to zero
totalMonths = 0
totalBudget = 0 

# read the csv file
with open(inputfile) as budget_data:
    # create a csv reader object
    csvreader = csv.reader(budget_data)

    # read the header row
    header = next(csvreader)

    for row in csvreader:
        totalMonths += 1

        totalBudget += float(row[1])
        

# start generating the output
output = (
    f"Financial Anaylsis \n"
    f"------------------------- \n"
    f"Total Months: {totalMonths} \n"
    f"Total Budget: ${totalBudget}"
    )

# print the output
print(output)

# export the output to the output text file
with open(outputfile, "w") as textfile:
    textfile.write(output)
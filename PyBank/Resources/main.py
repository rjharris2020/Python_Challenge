# import the csv and os modules
import csv
import os

# load the file to read budget data
inputfile = os.path.join("budget_data.csv")

# file to hold the out of the budget analysis
outputfile = os.path.join("budget_analysis.txt")

# set variables and initialize to zero
totalMonths = 0
totalBudget = 0 

# set variable and initialize the list of monthly changes
monthlyChanges = []
months = []

# read the csv file
with open(inputfile) as budget_data:
    # create a csv reader object
    csvreader = csv.reader(budget_data)

    # read the header row
    header = next(csvreader)
    # move to the next row (first row)
    firstRow = next(csvreader)

    # establish the previous budget and note that budget is in index 1
    previousBudget = float(firstRow[1])
    # increment the total months and add on to the total amount of budget
    totalMonths += 1
    totalBudget += float(firstRow[1])


    for row in csvreader:
        totalMonths += 1

        totalBudget += float(row[1])

        # calculate the net change
        netChange = float(row[1]) - previousBudget
        # add on to the list of monthly changes
        monthlyChanges.append(netChange)

        # add the first month that a change occurred, note that the month is in index 0
        months.append(row[0])

        # update the previous budget
        previousBudget = float(row[1])

# calculate the average change 
averageChange = sum(monthlyChanges) / len(monthlyChanges)

# set variables to hold the month and value of the greatest increase and decrease in profits
greatestIncrease = [months[0], monthlyChanges[0]]
greatestDecrease = [months[0], monthlyChanges[0]]

# create loop to calculate the index of the greatest and least monthly change
for m in range(len(monthlyChanges)):
    if (monthlyChanges[m] > greatestIncrease[1]):
        greatestIncrease[1] = monthlyChanges[m]
        greatestIncrease[0] = months[m]

    if (monthlyChanges[m] < greatestDecrease[1]):
        greatestDecrease[1] = monthlyChanges[m]
        greatestDecrease[0] = months[m]    

# start generating the output
output = (
    f"Financial Anaylsis \n"
    f"------------------------- \n"
    f"Total Months: {totalMonths} \n"
    f"Total Budget: ${totalBudget} \n"
    f"Average Change: ${averageChange} \n"
    f"Greatest Increase in Profit: {greatestIncrease[0]} ({greatestIncrease[1]}) \n"
    f"Greatest Dncrease in Profit: {greatestDecrease[0]} ({greatestDecrease[1]})"
    )

# print the output
print(output)

# export the output to the output text file
with open(outputfile, "w") as textfile:
    textfile.write(output)
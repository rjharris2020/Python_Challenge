# import modules
import csv
import os

# load the file to read
inputFile = os.path.join("election_data.csv")

# output file for the election data analysis
outputFile = os.path.join("electionDataAnalysis.txt")

# set variables
totalVotes = 0
candidates = []
candidatesVotes = {}
voteOutput = ""
winningCount = 0
winningCandidate = ""

# read the file
with open(inputFile) as electionData:
    csvreader = csv.reader(electionData)

    # read the header
    header = next(csvreader)

    # loop through rows
    for row in csvreader:
        totalVotes += 1

        # check to see if the candidate is in the list of candidates then add the count
        if row[2] not in candidates:
            candidates.append(row[2])

            candidatesVotes[row[2]] = 1

        else:
            candidatesVotes[row[2]] += 1

for candidates in candidatesVotes:
    votes = candidatesVotes.get(candidates)
    votePercentage = (float(votes) / float(totalVotes)) * 100
    voteOutput += f"{candidates}: {votePercentage:.2f}% \n"

    # compare the winning count to candidate
    if votes > winningCount:
        winningCount = votes
        winningCandidate = candidates 

winningCandidateOutput = f"Winner: {winningCandidate} \n"

# create an output variable to hold the output
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {totalVotes}\n"
    f"-------------------------\n"
    f"{voteOutput}\n"
    f"-------------------------\n"
    f"{winningCandidateOutput}"
)

# displays the output to the terminal
print(output)

#print the results and export the data to a txt file
with open(outputFile, "w") as textFile:
    textFile.write(output)
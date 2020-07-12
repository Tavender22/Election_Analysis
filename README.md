# Election_Analysis

## Project Overview
The Colorado Board of Elections has asked for a report to determine the winning candidate of a recent election. They were seeking the following:
 1. The total number of votes cast
 2. A complete list of candidates who received votes
 3. The percentage of votes for each canditate won
 4. The total number of votes each candidate won
 5. The winner of the election based on popular vote

## Resources Used:
- Data Source: election_results.csv
- Software: Python, Visual Studio

## Summary of Results
Total votes cast in the election were 369,711.

Candidate Results:
Charles Casper Stockham: 23.0% (85,213 votes)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

The winning candidate was Diana DeGette with 73.8% of the vote, receiving 272,892 votes.

## Challenge Overview
The Colorado Board of Elections has requested additional detail on the election results. They would like to know:
- the voter turnout in each county
- percentage votes of each county
- Written analysis of the election audit.

## Resources Used:
- Data Source: election_results.csv
- Software: Python, Visual Studio
- Starter Code = PyPoll_starter_challenge_code.py

## Challenge Summary
The election audit results for the county votes are:

County Results:
Jefferson: 38,855 (10.5% of total vote)
Denver: 306,055 (82.8% of total vote)
Arapahoe: 24, 801 (6.7% of total vote)

The county with the largest voter turnout was Denver with 306,055 votes cast, representing 82.8% of the total vote in the election.

## Future Use of the Code
This code can be used for future elections and to output results. We would need to change a bit of the code to make it would. First, we would need to change the reference to the source data, in this case our file_to_load path to the election_results.CSV file would need to change. Secondly, we should create a new output file for each election result we want to create to avoid overwriting other election results. This would be done by changing the file_to_save path to a new file name to receive the output.



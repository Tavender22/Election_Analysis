# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes for each canditate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. path to election_results.csv
    # Resources/election_results.csv

#import the datetime class from the datetime module
import datetime as dt

#Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()

#Print the present time
print ("the time right now is ", now)

import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = ('Resources\election_results.csv',r)

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: Perform Analysis.
    print(election_data)

# Close the File.

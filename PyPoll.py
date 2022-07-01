# What do we need to retrieve?
# 1. Total number of votes cast.
# 2.List of candidates with votes.
# 3.percentage of votes per candidate.
# 4.total number of votes per candidate.
# 5.winner of election based on popular vote.




# # Import the datetime class from the datetime module.
# import datetime
# now=datetime.datetime.now()
# print("The time right now is ", now)


# Assign a variable for the file to load and the path.

file_to_load = 'Resources/election_results.csv'

# Open the election results file and read it.

with open(file_to_load) as election_data:
    print(election_data)

# Dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election_results and read the file:
with open(file_to_load) as election_data:

# Print the file object
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
         # Write three counties to the file.
     txt_file.write("Counties in the Election\n----------\nArapahoe\nDenver\nJefferson")


# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    print(headers)

    
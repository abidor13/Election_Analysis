# What do we need to retrieve?
# 1. Total number of votes cast.
# 2.List of candidates with votes.
# 3.percentage of votes per candidate.
# 4.total number of votes per candidate.
# 5.winner of election based on popular vote.




# Import the datetime class from the datetime module.
# import datetime
# now=datetime.datetime.now()
# print("The time right now is ", now)


# Assign a variable for the file to load and the path.



# file_to_load = 'Resources/election_results.csv'

# # Open the election results file and read it.

# with open(file_to_load) as election_data:
#     print(election_data)

# # Dependencies
# import csv
# import os

# # Assign a variable for the file to load and the path
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Open the election_results and read the file:
# with open(file_to_load) as election_data:

# # Print the file object
#     print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file.
# with open(file_to_save, "w") as txt_file:

# # Write some data to the file.
#          # Write three counties to the file.
#      txt_file.write("Counties in the Election\n----------\nArapahoe\nDenver\nJefferson")





# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a vsariable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Total vote counter.
total_votes = 0

# Candidate options 
candidate_options = []
# Candidate Votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

# Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
    

    # Print Candidates name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
   
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results,end="")
    # Save the final vote to the text file
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        print(candidate_results)
        
        # Save the final candidate vote count to the text fil.
        txt_file.write(candidate_results)

        # Print each candidate, their voter count, and percentage to the
        # terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")



        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_candidate = candidate_name
            # And, set the winning_candidate equal to the candidate's name.
            winning_percentage = vote_percentage


        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
    winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
       

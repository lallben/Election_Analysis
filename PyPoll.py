import csv
import os

# Assign a variable for the file to load and the path.
file_to_load =os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")


#Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
#    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson\n")
#    print("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson\n")

# Initialize a total vote counter.
total_votes = 0

# Initialize the List of Candidates
candidate_list = []

# Initialize a Doctionary to hold candidate names & votes
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load,"r") as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
  
    # Skip the header row.
    next(file_reader)
    
    
    #Count the number of rows to get the number of votes cast
    for row in file_reader:
        total_votes=total_votes+1

# Get the candidate name from each row.
        candidate_name = row[2]
        
        if candidate_name not in candidate_list:
        
        # Add the candidate name to the candidate list.
            candidate_list.append(candidate_name)
        
        # To track candidate votes
            candidate_votes[candidate_name]= 0
        candidate_votes[candidate_name]+= 1

# Print the candidate list.
# print (f"The candidates in the election were: {candidate_list}")   

# Determine the percentage of votes for each candidate by looping through the counts.

# Iterate through the candidate list.
for candidate_name in candidate_votes:
    
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    
    #Print the candidate name and percentage of votes.  
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#Print Winning Candidate Summary
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
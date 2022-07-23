import csv
import os

# Assign a variable for the file to load and the path.
file_to_load =os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize the List of Candidates
candidate_list = []

# Initialize a Doctionary to hold candidate names & votes
candidate_votes={}

# Initializing variable to enable tracking Winning Candidate and relevant stats
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

#Write the results to the text file
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)    

    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        
        #Prepare the results for writing to the text file.  
        election_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        #print results to the terminal
        print(election_results)

        #write the results to the text file
        txt_file.write(election_results)

    #Print Winning Candidate Summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
   
    #print results to the terminal
    print(winning_candidate_summary)

    #print results to the text file
    txt_file.write(winning_candidate_summary)
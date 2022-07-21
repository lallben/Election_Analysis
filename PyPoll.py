import csv
import os

# Assign a variable for the file to load and the path.
file_to_load =os.path.join("Resources","election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: perform analysis.
    #print(election_data)

    # Create a filename variable to a direct or indirect path to the file.
    file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    #txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson\n")
    #print("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson\n")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file.
    # for row in file_reader:
    #     for i in range(len(row)):
    #         print(row[0])
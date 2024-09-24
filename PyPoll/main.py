# Import necessary modules
import csv
import os

# Files and file paths for input and output
election_input = os.path.join("Resources", "election_data.csv") # Input file path
analysis_output = os.path.join("analysis", "election_analysis.txt") # Output file path

# Define variables to track the election data
total_votes = 0

# Define lists and dictionaries to track candidate names and vote counts
candidate_list = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open and read the csv
with open(election_input) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it
    for row in reader:
        
        # Print a loading indicator (large dataset)
        # print(". ", end="")
        
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 0  # Initialize candidate vote count at 0

        # Add a vote to the candidate's count
        candidate_votes[candidate] += 1

# Open a text file to save the output
with open(analysis_output, "w") as txt_file:
    
    # Print text header
    header_output = ("Election Results\n"
                    "--------------------------\n")
    print(header_output)
    txt_file.write(header_output)
        
    # Print the total vote count (to terminal)
    count_output = (f"Total Votes: {total_votes}\n"
                    "--------------------------\n")
    print(count_output)

    # Write the total vote count to the text file
    txt_file.write(count_output)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_list:

        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate]
        percentage = round((votes / total_votes) * 100, 3)

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        candidate_output = (f"{candidate}: {percentage}% ({votes})\n")
        print(candidate_output)
        txt_file.write(candidate_output)

    # Generate and print the winning candidate summary
    winning_output = ("--------------------------\n"
                    f"Winner: {winning_candidate}\n"
                    "--------------------------\n")
    print(winning_output)

    # Save the winning candidate summary to the text file
    txt_file.write(winning_output)


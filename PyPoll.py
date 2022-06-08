# Add dependencies
import csv
import os



# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join(
    "Analysis", "election_analysis.txt")


# 1. The total number of votes cast

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load, 'r') as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
      
    # Print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total row count
        total_votes += 1
    
        candidate_name = row[2]

        # Add the candidate name to the list, only add new names
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)


            # Begin tracking that candidate's vote count

            candidate_votes[candidate_name] = 0

            # Add a vote for each count 
        candidate_votes[candidate_name] += 1


# Create the Save File to print to text
    with open(file_to_save, "w") as txt_file:

        election_results = (
            f"\nElection Results\n"
            f"-----------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-----------------------------\n"
        )

        print(election_results, end="")

        # Save the final vote count to the text file
        txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts
        for candidate_name in candidate_votes:
            # Retrieve vote count from a candidate
            votes = candidate_votes[candidate_name]

            # Calculate percentage for each candidate
            vote_percentage = float(votes) / float(total_votes) * 100

            # Print candidate name and percentage of voters
            # The :.1f  formats the decimal to round to one decimal place
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            print(candidate_results)
            txt_file.write(candidate_results)

            # 1. Determine if the votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # 2. If true, then set the winning_count = votes and winning percent = vote_percentage

                winning_count = votes
                winning_percentage = vote_percentage

                # 3. Set the winning candidate equal to the candidate's name 
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------------\n")

        print(winning_candidate_summary)
        # Write summary data to the file
        txt_file.write(winning_candidate_summary)
    


# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates
# 3. A percentage of votes each canditate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote



# Add dependencies
import csv
import os


# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join(
    "Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load, 'r') as election_data:
    # Perform analysis
    # Read and Analyze the data here:

    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    # for row in file_reader:

    #     print(row)

#with open(file_to_save, "w") as txt_file:

    # Write some data to the file

    


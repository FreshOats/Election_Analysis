# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates
# 3. A percentage of votes each canditate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


# Assign a variable for the file to load and the path

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load, 'r') as election_data:
    # Perform analysis
    print(election_data)


# Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# # Using the open() function with the "w" mode, we will write the data to the file.
# outfile = open(file_to_save, "w")

# # Write some data to the file
# outfile.write("Eat cheese and smile")

# # Close the file
# outfile.close()

# Using the with statement, open the file as a text file

with open(file_to_save, "w") as txt_file:

    # Write some data to the file

    txt_file.write("Arapahoe \nDenver \nJefferson")


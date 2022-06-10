# Election Analysis
***An audit of election results using Python.***
####by Justin R. Papreck
---

## Overview
A Colorado Board of Education employee has tasked us to complete the election audit of a recent local congressional election. This audit is to include a count and percentage of votes per candidate, as well as a breakdown of the votes by county, determining which county was the greatest contributor of votes, and of course, the winner of the election.  

### Purpose:
    Using Python scripting, a series of tasks were needed to determine the results of the election winner as well as the contributions to the vote per county in the state of Colorado. The process taken is as follows:
1. Winning Candidate Audit
    1. Calculate the total number of votes cast.
    2. Get a complete list of candidates.
    3. Calculate the total number of votes each canditate won.
    4. Calculate the percentage of votes each candidate won.
    5. Determine the winner of the election based on popular vote.
2. Leading County Audit
    1. Get a complete list of contributing counties.
    2. Calculate the number of votes cast in each county.
    3. Calculate the percentage of all votes per county. 
    4. Determine the county that contributed the most votes in the election.
3. Export a document with the results to present to the client. 

---
## Results and Analysis
    Based on the audit, Diana DeGette won the election with 73.8% of all votes, and the county with the highest contributing voters was Denver county. 
---   
### The Candidates
The analysis of the election:
- There were 369,711 votes cast in the election.
- The candidates:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results: 
    - Charles Casper Stockham received 23.0% of the vote with 85,213 votes. 
    - Diana DeGette received 73.8% of the votes with 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the votes with 11,606 votes.
 - The winner of the election:
    - Diana Gette, who received 73.8% of the votes with 272,892 votes
---
### The Counties
The analysis of contributing counties: 
- Three counties contributed to the election: 
    - Jefferson
    - Denver
    - Arapahoe
- The county vote contributions: 
    - Jefferson county provided 10.5% of the votes with 38,855 voters.
    - Denver county provided 82.8% of the votes with 306,055 voters.
    - Arapahoe county provided 6.7% of the votes with 24,801 voters.
- The county with the highest voter contribution: 
    - Denver county voters cast 306,055 of the 369,711 total votes, yielding 82.8% of all votes.  
---
### Code Analysis
  The process used to analyze the election results started with data acquisition from a csv file, using the python 'csv' package. The file included a header, so this was skipped in the analysis. 
  
```
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
```
  To determine count the votes, determine the candidates, and to determine the counties, a for loop was employed using conditional statements to determine whether the candidate or county had been accounted for, and if not would be appended to the list of either candidates or counties, respectively. The distinct candidates were recorded in a list, and likewise the counties. The votes per candidate or per county were recorded in dictionaries. The general process is as follows:
  
```
for row in reader:
    total_votes = total_votes + 1
    
    candidate_name = row[2]
    county_name = row[1]

    # The conditional statement to find the candidates and count their votes

    if candidate_name not in candidate_options:  
        candidate_options.append(candidate_name)
        candidate_votes[candidate_name] = 0
    
    candidate_votes[candidate_name] += 1


    # The conditional statement to find the counties and count their voters

    if county_name not in county_options:
         county_options.append(county_name)
         county_votes[county_name] = 0

    county_votes[county_name] += 1
```

In determing the final results, another loop was employed to present the votes in each county and the percentage of the total, and similarly for each of the candidates. Again, a conditional was used to determine if the county observed had the highest votes, and if not, replace the current. Similarly, this was done with the voters, since the results were not previously sorted. 

```
for county_name in county_options:
    votes = county_votes[county_name]

    county_percentage = float(votes) / float(total_votes) * 100
    county_results = (f"{county_name}: {county_percentage:.1f}% ({votes:,})\n")
    print(county_results)

    # Determine county with the highest turnout, the percentage of voters, and the contributing county.
    if (votes > largest_turnout) and (county_percentage > largest_percentage):
        largest_turnout = votes
        largest_percentage = county_percentage
        largest_county = county_name


for candidate_name in candidate_votes:

    votes = candidate_votes.get(candidate_name)
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(candidate_results)

    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
```
Finally, the results were formatted and returned as a text file: 

```
with open(file_to_save, "w") as txt_file:
    
    election_results = (
        f"\nElection Results\n"
        f"----------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------------------\n\n"
        f"County Votes: \n")
    txt_file.write(election_results)
    
    county_results = (f"{county_name}: {county_percentage:.1f}% ({votes:,})\n")
    txt_file.write(county_results)
    
    largest_county_summary = (
        f"\n----------------------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"----------------------------------------\n\n"
    )
    txt_file.write(largest_county_summary)
    
    candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    txt_file.write(candidate_results)
    
    winning_candidate_summary = (
        f"----------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------------\n")
    txt_file.write(winning_candidate_summary)
```

Ultimately, the results were printed both to the terminal as well as in the election_results text file. There are minor differences in the appearance of the Terminal printout

![Terminal](https://user-images.githubusercontent.com/33167541/172964993-a6233f26-07d5-434a-b0b2-e925e3d88135.png)

and the election_analysis.txt output
![TextFile](https://user-images.githubusercontent.com/33167541/172965383-b753e241-d368-4f27-a52b-2b52ce6aec78.png)

---
## Discussion
Using Python to analyze these data is much more robust than using something like Excel to do so, as from the start, it was possible to declare the election file as "read-only", so that the data were not changed during the processing, something that is clearly important in evaluating election results. The automation of loops in Python also don't require a definition of length, so the code is simple and robust to changes in the data. Where problems may arise would be when there are blank fields or duplicates. 
  By simply utilizing single for-loops with conditional statements, the program was able to process 369,000 votes and deliver reliable results - and this could just as easily work in a case with additional candidates and counties without needing any modification to the program. 

---
## Resources
- Data Source: election_results.csv
- Software: Python 3.10.4, Visual Studio Code, 1.67.2
- Dependencies:  "csv", "os"


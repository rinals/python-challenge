import csv

csv_file_path = "PyPoll/Resources/election_data.csv"
results_file_path = "PyPoll/analysis/result.txt"

with open(csv_file_path, mode='r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    # variable to count all the votes
    # every row is a vote
    vote_count = 0

    # Empty dictionary to keep all the candidates
    # and increment number of votes they get
    # Candidate  |  num_votes
    #------------------------
    # Charles    |  85213
    # Diana      |  272892
    # Raymon     |  11606
    vote_results = {}

    # Read each row in the CSV file as a dictionary
    # Each row will have 3 key-value pairs
    # row[Ballot ID]
    # row[County]
    # row[Candidate]
    for row in csv_reader:
        vote_count += 1

        # Get the name of candidate in this row
        candidate = row['Candidate']

        # If name of candidate is already in the vote_results
        # then increment the vote count for that candidate
        if(candidate in vote_results):
            vote_results[candidate] += 1
        
        # Else add the candidate name to the vote_results
        # and set their vote count to 1
        else:
            vote_results[candidate] = 1

    with open(results_file_path, mode='w') as file:
        print("Election Results")
        file.write("Election Results\n")
        print("-------------------------")
        file.write("-------------------------\n")
        print(f"Total Votes: {vote_count}")
        file.write(f"Total Votes: {vote_count}\n")
        print("-------------------------")
        file.write("-------------------------\n")
        # To get the winner we will keep 2 empty variables
        # winning_votes will keep track of the greatest number of votes
        # winning_candidate will store the name when we get the greatest number of votes
        winning_votes = 0
        winning_candidate = ""
    
        # vote_results is a dictionary
        # vote_results.items() will return all rows
        # Loop through all the vote_results.items()
        # each row in vote_results will contain
        # candidate name and number of votes for each candidate
        for candidate_name, num_votes in vote_results.items():
            percentage = num_votes / vote_count * 100
            # Round off percentage to 3 decimal points
            percentage = round(percentage, 3)
            print(f"{candidate_name}: {percentage}% ({num_votes})")
            file.write(f"{candidate_name}: {percentage}% ({num_votes})\n")
            if num_votes > winning_votes:
                winning_votes = num_votes
                winning_candidate = candidate_name
        print("-------------------------")
        file.write("-------------------------\n")
        print(f"Winner: {winning_candidate}")
        file.write(f"Winner: {winning_candidate}\n")
        print("-------------------------")
        file.write("-------------------------\n")


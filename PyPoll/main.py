import csv

file_path = "PyPoll/Resources/election_data.csv"

with open(file_path, mode='r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    # variable to count all the votes
    # every row is a vote
    vote_count = 0

    # Empty dictionary to keep all the candidates
    # and increment number of votes they get
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

    print(f"Total Votes: {vote_count}")
    print(vote_results)



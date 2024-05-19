import csv

file_path = "PyPoll/Resources/election_data.csv"

with open(file_path, mode='r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    vote_count = 0
    for row in csv_reader:
        vote_count += 1

    print(f"Total Votes: {vote_count}")



import csv

budget_file_path = "PyBank/Resources/budget_data.csv"
with open(budget_file_path, "r") as file:
    csv_reader = csv.DictReader(file)

    rows_done = 0

    total_months = 0
    total = 0
    previous_profit = 0
    total_change = 0

    for row in csv_reader:
        total_months += 1
        current_profit = int(row['Profit/Losses'])
        total += current_profit

        if rows_done > 0:
            change_in_profit = current_profit - previous_profit
            total_change += change_in_profit


        rows_done += 1
        previous_profit = current_profit

    average_change = total_change / (rows_done - 1)
    average_change = round(average_change, 2)
    

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average_change}")
import csv

budget_file_path = "PyBank/Resources/budget_data.csv"
results_file_path = "PyBank/analysis/result.txt"
with open(budget_file_path, "r") as file:
    csv_reader = csv.DictReader(file)

    rows_done = 0

    total_months = 0
    total = 0
    previous_profit = 0
    total_change = 0
    greatest_increase_in_profit = 0
    month_of_greatest_increase = ""
    greatest_decrease_in_profit = 0
    month_of_greatest_decrease = ""

    for row in csv_reader:
        total_months += 1
        current_profit = int(row['Profit/Losses'])
        current_date = row['Date']
        total += current_profit

        if rows_done > 0:
            change_in_profit = current_profit - previous_profit
            total_change += change_in_profit

            if change_in_profit > greatest_increase_in_profit:
                greatest_increase_in_profit = change_in_profit
                month_of_greatest_increase = current_date
            if change_in_profit < greatest_decrease_in_profit:
                greatest_decrease_in_profit = change_in_profit
                month_of_greatest_decrease = current_date


        rows_done += 1
        previous_profit = current_profit

    average_change = total_change / (rows_done - 1)
    average_change = round(average_change, 2)
    
    with open(results_file_path, "w") as result:
        print("Financial Analysis")
        result.write("Financial Analysis\n")
        print("----------------------------")
        result.write("----------------------------\n")
        print(f"Total Months: {total_months}")
        result.write(f"Total Months: {total_months}\n")
        print(f"Total: ${total}")
        result.write(f"Total: ${total}\n")
        print(f"Average Change: ${average_change}")
        result.write(f"Average Change: ${average_change}\n")
        print(f"Greatest Increase in Profits: {month_of_greatest_increase} (${greatest_increase_in_profit})")
        result.write(f"Greatest Increase in Profits: {month_of_greatest_increase} (${greatest_increase_in_profit})\n")
        print(f"Greatest Decrease in Profits: {month_of_greatest_decrease} (${greatest_decrease_in_profit})")
        result.write(f"Greatest Decrease in Profits: {month_of_greatest_decrease} (${greatest_decrease_in_profit})\n")


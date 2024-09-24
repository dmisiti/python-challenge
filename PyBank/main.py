# Import necessary modules
import csv
import os

# Files and file paths for input and output
budget_input = os.path.join("Resources", "budget_data.csv") # Input file path
analysis_output = os.path.join("analysis", "budget_analysis.txt") # Output file path

# Define variables to track the financial data
total_months = 0
net_total = 0
previous_profit_loss = None

# Create lists for net change and dates
net_change_list = []
dates_list = []

# Initialize variables for tracking profit increase and decrease
greatest_increase = float("-inf")
greatest_decrease = float("inf")
greatest_increase_date = ""
greatest_decrease_date = ""

# Open and read the csv
with open(budget_input) as budget_data:
    reader = csv.reader(budget_data)
    
    # Skip the header row
    header = next(reader)
    
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    
    # Track the total and net change
    total_months += 1
    net_total += int(first_row[1])
    previous_profit_loss = int(first_row[1])
    
    # Store the date of the first row
    dates_list.append(first_row[0])
    
    # Process each row of data
    for row in reader:
    
        # Track the total
        total_months += 1
        current_profit_loss = int(row[1])
        net_total += current_profit_loss
        
        # Store the date
        dates_list.append(row[0])
        
        # Track the net change
        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            net_change_list.append(change)
        
        # Calculate the greatest increase in profits (month and amount)
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]
        
        # Calculate the greatest decrease in losses (month and amount)
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]
        
        # Update previous_profit_loss for next iteration
        previous_profit_loss = current_profit_loss
        
# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0

# Generate the output summary
output = ("Financial Analysis\n"
        "--------------------------\n"
        f"Total Months: {total_months}\n"
        f"Net Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Print the output
print(output)

# Write the results to a text file
with open(analysis_output, "w") as txt_file:
    txt_file.write(output)

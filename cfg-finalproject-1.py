"""
Required Tasks

These are the required tasks for this project.
You should aim to complete these tasks before adding your own ideas to the project.
Read the data from the spreadsheet
Collect all of the sales from each month into a single list
Output the total sales across all months

Ideas for Extending the Project
Here are a few ideas for extending the project beyond the required tasks.
These ideas are just suggestions, feel free to come up with your own ideas and extend the program however you want.

Output a summary of the results to a spreadsheet
Calculate the following:
- Monthly changes as a percentage
- The average
- Months with the highest and lowest sales
Use a data source from a different spreadsheet (see Useful Resources)
"""

import csv
import pandas as pd

# Collect all of the sales from each month into a single list

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    sales_list = [int(row['sales']) for row in spreadsheet]

print(f"List of monthly sales: {sales_list}.")

#Output the total sales across all months
total_sales = sum(sales_list)
print("The total sales across all months came to: £{:,.2f}".format(total_sales))

#Calculate monthly changes as a percentage
percentage_change_list = []
for i in range(len(sales_list) - 1):
    change_from_previous_month = int(sales_list[i + 1]) - int(sales_list[i])
    percentage_change = "{:.2%}".format(change_from_previous_month/int(sales_list[i]))
    percentage_change_list.append(percentage_change)
print(f"List of monthly changes as a percentage: {percentage_change_list}.")

#Calculate the average sales
average = total_sales/len(sales_list)
print("The average total sales per month is: £{:,.2f}".format(average))

#Calculate the months with the highest and lowest sales

max_month = ''
min_month = ''

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        if int(row['sales']) == max(sales_list):
            max_month = row['month']
        if int(row['sales']) == min(sales_list):
            min_month = row['month']

print(f"The month with the highest sales was {max_month.title()}.")
print(f"The month with the lowest sales was {min_month.title()}.")

#Output a summary of the results to a spreadsheet

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    month_list = [row['month'] for row in spreadsheet]

percentage_change_list.insert(0,0)
data = pd.DataFrame({'Month': month_list,
                     'Monthly Sales': sales_list,
                     'Percentage Change': percentage_change_list})

data.to_csv('data.csv', index = False)
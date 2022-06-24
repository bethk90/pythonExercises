"""
Required Tasks

These are the required tasks for this project. You should aim to complete these tasks before adding your own ideas to the project.
Read the data from the spreadsheet
Collect all of the sales from each month into a single list
 Output the total sales across all months

Ideas for Extending the Project
Here are a few ideas for extending the project beyond the required tasks. These ideas are just suggestions, feel free to come up with your own ideas and extend the program however you want.

Output a summary of the results to a spreadsheet
Calculate the following:
Monthly changes as a percentage
The average
Months with the highest and lowest sales
Use a data source from a different spreadsheet (see Useful Resources)
"""

import csv

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    sales_list = []
    total_sales = 0
    for row in spreadsheet:
        sales_list.append(row['sales'])
        total_sales += float(row['sales'])
    print(sales_list)
    print("The total sales across all months came to: £{:,.2f}".format(total_sales))
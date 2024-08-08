#Title: Company Profit Listing
#Author: Kyle / Scarlett Budgell
#Date: August 7th -
#Description: Based off the ERD for HAB TAXI SERVICES, this is a program to show the company profits in a list, and as a bonus have the option to save them to a text file.

def compProfListing():
    import datetime
    import time
    import sys
    import ConvLib

    #Define Constants
    f = open('Defaults.dat', 'r')
    TRANSACTION_ID = int(f.readline())
    DRIVER_ID = int(f.readline())
    MONTHLY_STAND_FEE = float(f.readline())
    DAILY_RENTAL_FEE = float(f.readline())
    WEEKLY_RENTAL_FEE = float(f.readline())
    HST_RATE = float(f.readline())
    f.close()
    
    # Function to read data from .dat files and return a list of lists
    def ReadDat(filename):
        data = []
        try:
            with open(filename, 'r') as file:
                headers = file.readline().strip().split(',')
                for line in file:
                    values = line.strip().split(',')
                    data.append(values)
        except FileNotFoundError:
            print(f"Error: The file {filename} does not exist.")
        except Exception as e:
            print(f"An error occurred while reading the file {filename}: {e}")
        return data
    
    # function to sum a specific column in a list of lists
    def sum_column(data, column_index):
        total = 0.0
        for record in data:
            total += float(record[column_index])
        return total
    
    # Load data from .dat files
    revenues = ReadDat('CompanyRevs.dat')
    expenses = ReadDat('CompanyExpenses.dat')
    
    # Data load check
    if not revenues or not expenses:
        print("No data available from the required files. Please check the files and try again.")
    else:
        # Calculate time
        TotRevs = sum_column(revenues, 6)  # Assuming 'Total' is at index 6 in revenues
        TotExps = sum_column(expenses, 8) + sum_column(expenses, 8) * HST_RATE # Since the Total value is repeated across columns, the total expences needs to be processed in-program.
        TotProfs = TotRevs - TotExps
    
        # Calculate control totals
        ctr_total_revenue_entries = len(revenues)
        ctr_total_expense_entries = len(expenses)
    
        # accuracy checks :p
        acc_total_transactions = ctr_total_revenue_entries + ctr_total_expense_entries
    
        # print the receipt:)
        print()
        print("HAB TAXI SERVICES")
        print("Company Profit Listing")
        print(f"Revenues from {revenues[0][1]} to {revenues[-1][1]}")
        print()
        print(f"{'ID':<5} {'Date':<12} {'Desc.':<35} {'Driver ID':<10} {'Amount':<10} {'HST':<10} {'Total':<10}")
        print("=" * 140)
    
        for revenue in revenues:
            print(f"{revenue[0]:<5} {revenue[1]:<12} {revenue[2]:<34} {revenue[3]:<10} {ConvLib.DollarToStrConv(revenue[4]):<10} {ConvLib.DollarToStrConv(revenue[5]):<10} {ConvLib.DollarToStrConv(revenue[6]):<10}")
    
        print("=" * 140)
        print(f"{'':<67} {'Subtotal:':<10} ${TotRevs:<10.2f}")
        print(f"{'':<67} {'HST:':<10} ${sum_column(revenues, 5):<10.2f}")
        print(f"{'':<67} {'Total:':<10} ${TotRevs:<10.2f}")
        print()
        print("Expenses")
        print("=" * 140)
        print(f"{'Invoice ID':<11} {'Item ID':<9} {'Date':<12} {'Description':<30} {'Driver ID':<10} {'Cost':<10} {'Quantity':<10} {'Item Total':<10} {'Subtotal':<10} {'HST':<10} {'Total':<10}")
        print("=" * 140)
    
        for expense in expenses:
            print(f"{expense[0]:<10} {expense[1]:<9} {expense[3]:<12} {expense[5]:<30} {expense[4]:<10} {ConvLib.DollarToStrConv(expense[6]):<10} {expense[7]:<10} {ConvLib.DollarToStrConv(expense[8]):<10} {ConvLib.DollarToStrConv(expense[9]):<10} {ConvLib.DollarToStrConv(expense[10]):<10} {ConvLib.DollarToStrConv(expense[11]):<10}")
    
        print("=" * 140)
        print(f"{'':<67} {'Subtotal:':<10} ${sum_column(expenses, 8):<10.2f}")
        print(f"{'':<67} {'HST:':<10} ${(sum_column(expenses, 8)*HST_RATE):<10.2f}")
        print(f"{'':<67} {'Total:':<10} ${TotExps:<10.2f}")
        print("=" * 140)
        print(f"Total Revenues:         ${TotRevs:<10.2f}")
        print(f"Total Expenses:         ${TotExps:<10.2f}")
        print(f"Total Profit (Loss):    ${TotProfs:<10.2f}")
        print("=" * 140)
        print()
        print("Control Totals (Ctr's):")
        print(f"Total Revenue Entries: {ctr_total_revenue_entries}")
        print(f"Total Expense Entries: {ctr_total_expense_entries}")
        print()
        print("Accuracy Checks (Acc's):")
        print(f"Total Number of Transactions: {acc_total_transactions}")
    
        # Save to file
        with open('CompanyProfitListing.txt', 'w') as file:
            file.write("HAB TAXI SERVICES\n")
            file.write("Company Profit Listing\n")
            file.write(f"Revenues from {revenues[0][1]} to {revenues[-1][1]}\n")
            file.write("\n")
            file.write(f"{'ID':<5} {'Date':<12} {'Desc.':<25} {'Driver ID':<10} {'Amount':<10} {'HST':<10} {'Total':<10}\n")
            file.write("=" * 100 + "\n")
    
            for revenue in revenues:
                file.write(f"{revenue[0]:<5} {revenue[1]:<12} {revenue[2]:<25} {revenue[3]:<10} {revenue[4]:<10} {revenue[5]:<10} {revenue[6]:<10}\n")
    
            file.write("=" * 100 + "\n")
            file.write(f"{'':<67} {'Subtotal:':<10} ${TotRevs:<10.2f}\n")
            file.write(f"{'':<67} {'HST:':<10} ${sum_column(revenues, 5):<10.2f}\n")
            file.write(f"{'':<67} {'Total:':<10} ${TotRevs:<10.2f}\n")
            file.write("\n")
            file.write("Expenses\n")
            file.write("=" * 100 + "\n")
            file.write(f"{'Invoice Number':<15} {'Date':<12} {'Description':<25} {'Driver ID':<10} {'Cost':<10} {'Quantity':<10} {'Item Total':<10} {'Subtotal':<10} {'HST':<10} {'Total':<10}\n")
            file.write("=" * 100 + "\n")
    
            for expense in expenses:
                file.write(f"{expense[0]:<15} {expense[1]:<12} {expense[2]:<25} {expense[3]:<10} {expense[4]:<10} {expense[5]:<10} {expense[6]:<10} {expense[7]:<10} {expense[8]:<10} {expense[9]:<10}\n")
    
            file.write("=" * 100 + "\n")
            file.write(f"{'':<67} {'Subtotal:':<10} ${TotExps:<10.2f}\n")
            file.write(f"{'':<67} {'HST:':<10} ${sum_column(expenses, 8):<10.2f}\n")
            file.write(f"{'':<67} {'Total:':<10} ${TotExps:<10.2f}\n")
            file.write("=" * 100 + "\n")
            file.write(f"Total Revenues:         ${TotRevs:<10.2f}\n")
            file.write(f"Total Expenses:         ${TotExps:<10.2f}\n")
            file.write(f"Total Profit (Loss):    ${TotProfs:<10.2f}\n")
            file.write("=" * 100 + "\n")
            file.write("\n")
            file.write("Control Totals (Ctr's):\n")
            file.write(f"Total Revenue Entries: {ctr_total_revenue_entries}\n")
            file.write(f"Total Expense Entries: {ctr_total_expense_entries}\n")
            file.write("\n")
            file.write("Accuracy Checks (Acc's):\n")
            file.write(f"Total Number of Transactions: {acc_total_transactions}\n")
    
        # Blinking message
        message = "CompanyProfitListing.txt has been saved!"
        for _ in range(5):
            sys.stdout.write('\r' + message)
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write('\r' + ' ' * len(message))
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write('\r' + message + '\n')
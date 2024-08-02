#DESCRIPTION: Program for HAB Taxi Services to enter company revenue entries.
#AUTHOR:      Robot Group 5 (Zachary Collier)
#DATE:        August 2nd 2024

def companyRevEnter():
    #Import libraries
    import ConvLib
    import NotifLib
    import ProgressBars
    import datetime

    #Define Constants
    f = open('Defaults.dat', 'r')
    TRANSACTION_ID = int(f.readline())
    DRIVER_ID = int(f.readline())
    MONTHLY_STAND_FEE = float(f.readline())
    DAILY_RENTAL_FEE = float(f.readline())
    WEEKLY_RENTAL_FEE = float(f.readline())
    HST_RATE = float(f.realine())
    f.close()

    #Define Functions

    #Main Program
    while True:
        #Gather user inputs
        while True:
            driverIDdsp = input("Enter Driver ID (or END to exit the program): ")
            if driverIDdsp == "END":
                print("Returning to menu...")
                break
            else:
                try:
                    driverID = int(driverIDdsp)
                except:
                    NotifLib.ErrorMessage("Please enter a valid 4-digit integer.")
                else:
                    if len(driverIDdsp) != 4:
                        NotifLib.ErrorMessage("Please enter a valid 4-digit integer.")
                    else:
                        break
        if driverIDdsp == "END":
            break

        while True:
            try:
                transactionDatedsp = input("Enter Transaction Date (YYYY-MM-DD): ")
                transactionDate = ConvLib.StrToDateConv(transactionDatedsp)
            except:
                NotifLib.ErrorMessage("Please enter the date in the format YYYY-MM-DD.")
            else:
                break

        transactionDesc = input("Enter the transaction description: ")

        while True:
            try:
                transactionAmtdsp = input("Enter transaction amount: ")
                transactionAmt = float(transactionAmtdsp)
            except:
                NotifLib.ErrorMessage("Please enter a valid number.")
            else:
                break
        
        #Perform calculations
        transactionAmtdsp = ConvLib.DollarToStrConv(transactionAmt)
        
        transactionHST = HST_RATE * transactionAmt
        transactionHSTdsp = ConvLib.DollarToStrConv(transactionHST)

        transactionTotal = transactionAmt + transactionHST
        transactionTotaldsp = ConvLib.DollarToStrConv(transactionTotal)

        entry = f'{TRANSACTION_ID}, {transactionDatedsp}, {transactionDesc}, {driverIDdsp}, {transactionAmt}, {transactionHST}, {transactionTotal}\n'

        #Display Outputs
        print(f'''Please review your inputs:
        Transaction ID: {TRANSACTION_ID}
        Transaction Date: {transactionDatedsp}
        Transaction Description: {transactionDesc}
        Driver ID: {driverIDdsp}
        Transaction Amount: {transactionAmtdsp}
        Transaction HST: {transactionHSTdsp}
        Transaction Total: {transactionTotaldsp}''')

        f = open('CompanyRevs.dat', 'a')
        f.write(entry)
        f.close()

        TRANSACTION_ID += 1

        print()
        TotalIterations = 10
        Message = "Saving Data ..."
        for i in range(TotalIterations + 1):
            time.sleep(0.1)  # Simulate some work
            ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=30)
        print() #For spacing
        print()
    
    #Housekeeping
    f = open('Defaults.dat', 'w')
    TRANSACTION_ID = f.write('{}\n'.format(TRANSACTION_ID))
    DRIVER_ID = f.write('{}\n'.format(DRIVER_ID))
    MONTHLY_STAND_FEE = f.write('{}\n'.format(MONTHLY_STAND_FEE))
    DAILY_RENTAL_FEE = f.write('{}\n'.format(DAILY_RENTAL_FEE))
    WEEKLY_RENTAL_FEE = f.write('{}\n'.format(WEEKLY_RENTAL_FEE))
    HST_RATE = f.write('{}\n'.format(HST_RATE))
    f.close()

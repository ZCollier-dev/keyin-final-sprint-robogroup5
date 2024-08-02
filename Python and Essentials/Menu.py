#DESCRIPTION: Menu for HAB Taxi Services to track employees, revenues, and expenses, as well as provice reports.
#AUTHOR:      Robot Group 5 (Zachary Collier)
#DATE:        July 30th 2024

#Import libraries
import NotifLib

#Import options

#Gather user input
while True:

    print('''
           HAB Taxi Services
        Company Services System
    
    1. Enter a New Employee (driver).
    2. Enter Company Revenues.
    3. Enter Company Expenses.
    4. Track Car Rentals.
    5. Record Employee Payment.
    6. Print Company Profit Listing.
    7. Print Driver Financial Listing.
    8. Corporate SUmmary Report.
    9. Quit Program.
    ''')
    while True:
        try:
            choice = input("Enter Choice (1-9): ")
            choice = int(choice)
        except:
            NotifLib.ErrorMessage('Please enter a number between 1 and 9.')
        else:
            if choice < 1 or choice > 9:
                NotifLib.ErrorMessage('Please enter a number between 1 and 9.')
            else:
                break
    
    #Perform calculations
    if choice == 1:
        print("run 1")
    elif choice == 2:
        print("run 2")
    elif choice == 3:
        print("run 3")
    elif choice == 4:
        print("run 4")
    elif choice == 5:
        print("run 5")
    elif choice == 6:
        print("run 6")
    elif choice == 7:
        print("run 7")
    elif choice == 8:
        print("run 8")
    else:
        print("Quitting Program... have a great day!")
        break
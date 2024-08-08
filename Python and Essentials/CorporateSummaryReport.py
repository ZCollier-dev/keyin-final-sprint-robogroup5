# Description: Company summary report
# Author: Michael Ward
# Date: August 5th 2024


def corporateSummaryReport():

    import ConvLib

    EmployeeDataFile = 'EmployeeRecs.dat'
    RevenueFile = 'CompanyRevs.dat'

    ActiveEmployees = 0

    with open('EmployeeRecs.dat', 'r') as file:
        for line in file:
            ActiveEmployees += 1
    ActiveEmployees = str(ActiveEmployees)

    TotalEmpBalance = 0    

    with open('EmployeeRecs.dat', 'r') as file:

        for line in file:
            EmployeeInfo = line.split()
            try:
                EmpBalanceDue = float(EmployeeInfo[-1])
                TotalEmpBalance += EmpBalanceDue
            except:
                continue
    TotalEmpBalanceDsp = ConvLib.DollarToStrConv(TotalEmpBalance)

    CarsRented = 0

    with open('EmployeeRecs.dat', 'r') as file:
        for line in file:
            EmployeeInfo = line.split()
            try:
                OwnCar = (EmployeeInfo[-2])
                if OwnCar == "Y,":
                    CarsRented += 1
            except:
                continue
    if OwnCar == "Y":
        CarsRented += 1

    TransactionQuantity = 0

    with open('CompanyRevs.dat', 'r') as file:
        for line in file:
            TransactionQuantity += 1


    TransactionAmounts = 0
    TransactionHSTs = 0
    TransactionTotals = 0

    with open('CompanyRevs.dat', 'r') as file:
        for line in file:
            RevenueInfo = line.split(',')
            try:
                TransactionAmountAdd = float(RevenueInfo[-3])
                TransactionAmounts += TransactionAmountAdd
            except:
                continue
    TransactionAmountsDsp = ConvLib.DollarToStrConv(TransactionAmounts)


    with open('CompanyRevs.dat', 'r') as file:
        for line in file:
            RevenueInfo = line.split(',')
            try:
                TransactionHSTAdd = float(RevenueInfo[-2])
                TransactionHSTs += TransactionHSTAdd
            except:
                continue
    TransactionHSTDsp = ConvLib.DollarToStrConv(TransactionHSTs)

    with open('CompanyRevs.dat', 'r') as file:
        for line in file:
            RevenueInfo = line.split(',')
            try:
                TransactionTotalAdd = float(RevenueInfo[-1])
                TransactionTotals += TransactionTotalAdd
            except:
                continue
    TransactionTotalsDsp = ConvLib.DollarToStrConv(TransactionTotals)

    ExpenseQuantity = 0

    with open('CompanyRevs.dat', 'r') as file:
        for line in file:
            ExpenseQuantity += 1
    ExpenseQuantity = str(ExpenseQuantity)


    SubTotalExpenses = 0

    with open('CompanyExpenses.dat', 'r') as file:
        for line in file:
            ExpensesInfo = line.split(',')
            try:
                ExpensesSubTotalAdd = float(ExpensesInfo[-3])
                SubTotalExpenses += ExpensesSubTotalAdd
            except:
                continue
    SubTotalExpensesDsp = ConvLib.DollarToStrConv(SubTotalExpenses)

    HSTExpenses = 0

    with open('CompanyExpenses.dat', 'r') as file:
        for line in file:
            ExpensesInfo = line.split(',')
            try:
                ExpensesHSTAdd = float(ExpensesInfo[-2])
                HSTExpenses += ExpensesHSTAdd
            except:
                continue
    HSTExpensesDsp = ConvLib.DollarToStrConv(HSTExpenses)

    TotalExpenses = 0

    with open('CompanyExpenses.dat', 'r') as file:
        for line in file:
            ExpensesInfo = line.split(',')
            try:
                ExpensesTotalAdd = float(ExpensesInfo[-1])
                TotalExpenses += ExpensesTotalAdd
            except:
                continue
    TotalExpensesDsp = ConvLib.DollarToStrConv(TotalExpenses)

    TotalRev = TransactionAmounts - TotalExpenses
    TotalRevDsp = ConvLib.DollarToStrConv(TotalRev)

    AverageRev = TransactionAmounts / TransactionQuantity
    AverageRevDsp = ConvLib.DollarToStrConv(AverageRev)



    NetHST = TransactionHSTs - HSTExpenses
    NetHSTDsp = ConvLib.DollarToStrConv(NetHST)

    TransactionQuantity = str(TransactionQuantity)

    print(f"                                                                                                 ")
    print(f"=================================================================================================")
    print(f"                                                                                                 ")
    print(f"                                        HAB TAXI SERVICES                                        ")
    print(f"                                   CORPORATE SUMMARY REPORTING                                   ")
    print(f"                                                                                                 ")
    print(f"=================================================================================================")
    print(f"-------------------------------------------------------------------------------------------------")
    print(f"=================================================================================================")
    print(f"                                                                                                 ")
    print(f"TRANSACTION INFORMATION:                                                                         ")
    print(f"                                                                                                 ")
    print(f"   Total Drivers Employed:                                                               {ActiveEmployees:>8s}")
    print(f"   Total Employee Balance due:                                                          {TotalEmpBalanceDsp:>9s}")
    print(f"   Total Cars on Rent:                                                                   {CarsRented:>8d}")
    print(f"   Total Transactions:                                                                   {TransactionQuantity:>8s}")
    print(f"   Average Transaction:                                                                 {AverageRevDsp:>9s}")
    print(f"                                                                                                 ")
    print(f"=================================================================================================")
    print(f"-------------------------------------------------------------------------------------------------")
    print(f"=================================================================================================")
    print(f"                                                                                                 ")
    print(f"REVENUE INFORMATION:                                                                             ")
    print(f"                                                                                                 ")
    print(f"   Revenue Subtotal:                                                                    {TransactionAmountsDsp:>9s}")
    print(f"   Revenue HST:                                                                         {TransactionHSTDsp:>9s}")
    print(f"   Revenue Total:                                                                       {TransactionTotalsDsp:>9s}")
    print(f"   Revenue HST:                                                                         {TransactionHSTDsp:>9s}")
    print(f"   Net HST:                                                                             {NetHSTDsp:>9s}")
    print(f"                                                                                                 ")
    print(f"=================================================================================================")
    print(f"-------------------------------------------------------------------------------------------------")
    print(f"=================================================================================================")
    print(f"                                                                                                 ")
    print(f"EXPENSE INFORMATION:                                                                             ")
    print(f"                                                                                                 ")
    print(f"   Expense Claims:                                                                       {ExpenseQuantity:>8s}")
    print(f"   Expense Subtotal:                                                                    {SubTotalExpensesDsp:>9s}")
    print(f"   Expense HST:                                                                         {HSTExpensesDsp:>9s}")
    print(f"   Expense Total:                                                                       {TotalExpensesDsp:>9s}")
    print(f"                                                                                                 ")
    print(f"=================================================================================================")
    print(f"-------------------------------------------------------------------------------------------------")
    print(f"=================================================================================================")
    print(f"                                                                                                 ")
    print(f"TOTAL PROFIT:                                                                           {TotalRevDsp:>9s}")
    print(f"                                                                                                 ")
    print(f"=================================================================================================") 
    print(f"                                                                                                 ")
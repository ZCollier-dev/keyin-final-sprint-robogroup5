#DESCRIPTION: Library with multiple functions:
# - quickly convert dates to and from strings using the yyyy-mm-dd format.
# - quickly convert floating point dollar values to and from strings in the format $#,###.##
#AUTHOR:      Zachary Collier
#DATE:        July 16th, 2024

import datetime

def StrToDateConv(dateToConv): #Parse String into a datetime
    try:
        dateReturn = datetime.datetime.strptime(dateToConv, '%Y-%m-%d')
    except:
        print("---!!!---")
        print("ERR: Invalid Date Format - please use 'YYYY-MM-DD'.")
        print("---!!!---")
    else:
        return dateReturn

def DateToStrConv(dateToConv): #Format datetime into a String
    dateReturn = datetime.datetime.strftime(dateToConv, '%Y-%m-%d')
    return dateReturn

def DollarToStrConv(dollarValue): #Format float into a String w/ dollar value
    try:
        dollarValue = float(dollarValue)
    except:
        print("---!!!---")
        print("ERR: Please enter a valid number.")
        print("---!!!---")
    else:
        dollarValueStr = "${:,.2f}".format(dollarValue)
        return dollarValueStr

def DollarToFloatConv(dollarValue): #Format String w/ dollar value into Float
    try:
        dollarValue = dollarValue.replace('$', '')
        dollarValue = dollarValue.replace(',', '')
        dollarValueFloat = float(dollarValue)
    except:
        print("---!!!---")
        print("ERR: Please enter a valid string.")
        print("---!!!---")
    else:
        return dollarValueFloat
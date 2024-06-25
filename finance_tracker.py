import pandas as pd
from datetime import date

dates = []
description = []
category = []
income = []
debit = []
balance = []
    
finance_report = pd.DataFrame()

def add_entries(dates, description, category, income, debit, balance):
    finance_report['Date'] = dates
    finance_report['Description'] = description
    finance_report['Category'] = category
    finance_report['Income'] = income
    finance_report['Debit'] = debit
    finance_report['Balance'] = balance
    
def dif(inc, deb):
    inc_total = 0
    deb_total = 0
    for value in inc:
        inc_total += value
    for value in deb:
        deb_total += value
    return inc_total - deb_total

option = -1
while(option != 0):
        
    print('Welcome to the simple finance tracker:')
    print('1. Make new entry')
    print('2. Save and Show finance report')
    print('0. Exit')
    option = int(input('Choose an option:\n'))

      #Print a new line
    print()
      #Check for the user choice or option or input
    if option == 0:
        print('Exiting the program')
        break

    elif option == 1:
        print('Making new entry')
        dates.append(date.today())
        des = input('Enter description:\n')
        description.append(des)
        cat = input('Enter category: Income/Mortgage/Utilities/Groceries/Fuel/Food/Hangout\n')
        category.append(cat)
        inc = int(input('Enter Income: 0 for Nil\n'))
        income.append(inc)
        deb = float(input('Enter Debit: 0 for Nil\n'))
        debit.append(deb)
        bal = dif(income,debit)
        balance.append(bal)
        
        
    elif option == 2:
        add_entries(dates, description, category, income, debit, balance)
        #Save the expense report
        finance_report.to_csv('fintrack.csv')
        #Show the expense report
        print(finance_report)
        if bal < 5000:
            print('Overspending: Yes')
        else:
            print('Overspending: No')
        break

    else:
        print('You chose and incorrect option. Please choose 0, 1, or 2')
     
 
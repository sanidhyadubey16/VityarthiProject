#main.py

from  storage  import Addexpense, getexpenses, clearexpenses
from  logic  import calculatetotal, categorytotals, searchexpenses, averageExpense
from  view  import showmenu, showExp, showcategoryTotal, average_show

def getcurrentdate():
    date = input("Enter date (dd): ")
    return date

def addnewexpense():
    print("Add New Expense")
    date = getcurrentdate()
    category = input("Category  : ")
    amount = input("Amount : ")
    note = input("Note: ")

    try:
        float(amount)
    except:
        print("Invalid amount! Please enter a number.")
        return

    Addexpense(date, category, amount,note)
    print("Expense added!")

def main():
    while True:
        showmenu()
        x = input("Choose the option : ")

        if x == "1":
            addnewexpense()

        elif x == "2":
            expenses = getexpenses()
            showExp(expenses)
            print("Total Spent:",calculatetotal(expenses))

        elif x == "3":
            expenses = getexpenses()
            totals = categorytotals(expenses)
            showcategoryTotal(totals)

        elif x== "4":
            Keyword = input("Enter search keyword : ")
            results = searchexpenses(getexpenses(), Keyword)
            showExp(results)

        elif x == "5":
            expenses = getexpenses()
            avg = averageExpense(expenses)
            average_show(avg)

        elif x ==  "6":
            Input = input(" Are you sure you want to clear off all the expenses ? (yes or no): ")
            if Input.lower()  ==  "yes":
                clearexpenses()
                print("All expenses cleared.")
            else:
                print("Clear cancelled.")

        elif x == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
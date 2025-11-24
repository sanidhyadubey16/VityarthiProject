#view.py

def showmenu():
    print("Personal Expense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Category Totals")
    print("4. Search Expenses")
    print("5. Show Average Expense")
    print("6. Clear All Expenses")
    print("7. Exit")

def showExp(Expense):
    if len(Expense) == 0:
        print("No expenses found.")
        return
    print("Date       | Category    | Amount   | Note")
    print("----------------------------------------------")
    for e in Expense:
        print(f"{e['date']} | {e['category']:<10} | ${e['amount']:<6} | {e['note']}")

def showcategoryTotal(Total):
    if len(Total) == 0:
        print("No category Total to show.")
        return
    print("Category Total:")
    for category, amount in Total.items():
        print(category , ":"," ","$",round(amount,2))

def average_show(avg):
    p = round(avg,2)
    print("Average Expense Amount: " , p)
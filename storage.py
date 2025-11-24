#storage.py

expenses = []

def Addexpense(date, category, amount, note):
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }
    expenses.append(expense)

def getexpenses():
    return expenses

def clearexpenses():
    expenses.clear()
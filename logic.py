#logic.py

def calculatetotal(expenses):
    total = 0
    for e in expenses:
        total += float(e["amount"])
    return total

def categorytotals(expenses):
    totals = {}
    for e in expenses:
        category = e["category"]
        amount = float(e["amount"])
        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount
    return totals

def searchexpenses(expenses, keyword):
    keyword = keyword.lower()
    result = []
    for e in expenses:
        if keyword in e["category"].lower() or keyword in e["note"].lower():
            result.append(e)
    return result

def averageExpense (expenses):
    if len(expenses) == 0:
        return 0
    return calculatetotal(expenses) / len(expenses)
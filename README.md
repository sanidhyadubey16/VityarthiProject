# 🟢 Project Title
**Personal Expense Tracker**

---

# 🟣 Overview of the Project

This is the project to managing personal expenses where expenses has become very important in daily life. A Personal Expense Tracker is a tool that helps the users record their expenses, categorize them, and understand their spending habits. The main goal of this project is to create a easy-to-use expense tracker that allows users to add, view,categorize and manage their personal finances.

---

#  Features
| Category | Description |
|---------|-------------|
|Add Expense | Simple form interface to record new transactions. |
| Transaction History | view of all past transactions. |
| Profile Management | It allows users to update their profile details. |
|Clear data|Option that clear all stored expenses.|
|Search Function | Ability to find transactions.|

---

#  Technologies / Tools Used
| Type | Tool |
|------|------|
| Programming Language | Python |
| Libraries | None (no external dependencies) |
| Storage | In-memory dictionary |
| Execution | Command Line / Terminal |

---

# Steps to Install & Run the Project
1️. Install Python 3.9 or newer.
2. Download the following four files into the same directory:

    *storage.py
    *logic.py
    *view.py
    *main.py  
4. Open terminal / command prompt inside that folder .
5.  Run the program using:
python main.py

---

 # Instructions for testing
To test the program start by running it and follow these steps to test it :

1.Add Expenses :  Add few expenses with different categories and amounts and make sure you enter a valid number.

2.View All Expenses: Verify that all the expenses you added in first step are displayed in correct format(Date,Category,Amount,Note) and that the "Total Spent" value is calculated correctly.

3. Show Category Totals: Verify that a total is calculated and displayed for each unique category and that categories with multiple entries are summed up to a single total.

4. Search Expenses : Enter a keyword (e.g., a specific note or category name). Check that only matching expenses are displayed .

5. Show Average Expense:  Verify that the displayed average expense is the Total Spent divided by the number of expenses.

6. Clear All Expenses : 
*Test Cancellation: Type no and verify that the clear operation is cancelled. 
*Test Confirmation: Type yes to confirm. Then, re-check step 2 (View All Expenses) to confirm the list is empty.

"""
Kevin Amaya
IS 303 - A03

Expense Tracker
This program will allow users to input their expenses, categorize them, and then provide insights.

Inputs:
- Ask the user to input expenses
- Ask them for their categories and amounts

Processes:
- Save inputs into a dictionary
- Track the biggest expense using min/max pattern
- Accumulate total per category with accumulator pattern
- Filter expenses above a certain limit using filter pattern

Outputs:
- Print biggest expense
- Print total per category
- Print filtered expenses
"""
#define list and validate
valid_categories = ["dining", "groceries", "entertainment", "rent", "gas"]
expenses = []
print()
print(f"Welcome to the Expense Tracker!")
print(f"Please enter your expenses (choose one of the following: {', '.join(valid_categories)}) followed by their amounts. Type 'done' when finished.\n")
input_category = input("Enter category (or type 'done'): ")

#While loop
while input_category.lower() != "done":
    if input_category not in valid_categories:
        print(f"Invalid category. Please enter a choice from {', '.join(valid_categories)}.")
        input_category = input("Enter category (or 'done'): ")
        continue
    input_amount = input(f"Enter the amount for {input_category}: ")
    if input_amount.replace('.', '', 1).isdigit():
        amount = float(input_amount)
        print(f"Expense added!")
    else:
        print(f"Please enter a valid amount")
    #Dictionary
    expenses.append({"category": input_category, "amount": amount})
    input_category = input("Enter category (or 'done'): \n")

print (f"====EXPENSES REPORT====")
#Find the biggest expense
top_expense = expenses[0]
for exp in expenses:
    if exp["amount"] > top_expense["amount"]:
        top_expense = exp
print(f"Biggest expense: {top_expense['category'].upper()} - ${top_expense['amount']:.2f}\n")
#Find total per category
expense_categories = {}
for exp in expenses:
    cat = exp["category"]
    amt = exp["amount"]
    if cat in expense_categories:
        expense_categories[cat] += amt  
    else:
        expense_categories [cat] = amt
for cat, total in expense_categories.items():
    print(f"Total for {cat}: ${total:.2f}\n")
#Filter expenses above a certain limit
print(f"Expenses over $100:")
for exp in expenses:
    if exp["amount"] >= 100:
        print(f"{exp['category'].upper()} - ${exp['amount']:.2f}")
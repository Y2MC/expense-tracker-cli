expenses = []

while True:

  print("\nExpense Tracker")
  print("1. Add Expense")
  print("2. View Expenses")
  print("3. Show Total")
  print("4. Delete Expense")
  print("5. Quit")

  option = input("Select an option from 1-5:")

  if option == "1":
    description = input("Enter expense description: ")
    amount_text = input("Enter amount: $")
    try:
      amount = float(amount_text)
      expense ={
        "description": description,
        "amount": amount
      }
      expenses.append(expense)
      print("Expense added.")
    except ValueError:
      print("Invalid amount. Please enter a number.")

  elif option =="2":
    if len(expenses) == 0:
      print("No expenses recorded yet.")
    else:
      print("\nYour Expenses: ")
      for i, expense in enumerate(expenses):
        print(f"{i + 1}. {expense['description']} - ${expense['amount']:.2f}")

  elif option == "3":
    if len(expenses) == 0:
      print("No expenses recorded yet.")
    else:
      print("\nYour Expenses:")
      for i, expense in enumerate(expenses):
        print(f"{i+ 1}. {expense['description']} - ${expense['amount']:.2f}")
        
      total = 0
      for expense in expenses:
        total += expense["amount"]
      print(f"\nTotal spent: ${total:.2f}")

  elif option == "4":
    if len(expenses) == 0:
      print("No expenses to delete.")
    else:
      print("\nYour Expenses:")
      for i, expense in enumerate(expenses):
        print(f"{i + 1}. {expense['description']} - ${expense['amount']:.2f}")
      try:
        num = int(input("Enter the number of the expense to delete:"))
        if 1 <= num <= len(expenses):
          removed = expenses.pop(num - 1)
          print(f"Deleted: {removed['description']} - ${removed['amount']:.2f}")
        else:
          print("Invalid number.")
      except ValueError:
        print("Please enter a valid number.")

  elif option == "5":
    print("See ya later.")
    break

  else:
    print("Invalid number. Please enter a number from 1-5.")
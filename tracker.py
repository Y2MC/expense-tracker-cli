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
    amount_text = input("Enter amount: ")
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
    print("View Expenses Selected.")

  elif option == "3":
    print("Show Total Selected.")

  elif option == "4":
    print("Delete Expense Selected.")

  elif option == "5":
    print("Quit selected.")
    break

  else:
    print("Invalid number. Please enter a number from 1-5.")

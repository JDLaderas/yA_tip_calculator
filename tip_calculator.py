print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? "))
percent = int(input("What percentage tip you like to give? 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))

bill_tip = round(bill * (percent / 100), 2)

total_bill = round(bill_tip + bill, 2)

bill_split = round(total_bill / people, 2)

print(f"The total tip: {bill_tip}")
print(f"The total bill: {total_bill}")
print(f"Each person should pay: {bill_split}")

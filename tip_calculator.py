print("Welcome to the Tip Calculator\n")

bill = float(input("What was the bill: $"))
tip = float(input("How much tip would you like to give? 10%, 12%, or 15%? "))

person = float(input("How many people to split the bill? "))

tipCalc = tip / 100

withTip = tipCalc * bill

totalBill = withTip + bill

eachPerson = round(totalBill / person,2)

print(f"\nThe total bill with tip is: ${totalBill}")
print(f"Each person should pay: ${eachPerson}")

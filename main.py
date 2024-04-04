#Welcoming to our calculator
print("Welcome to the Tip Calculator")
#Asking for the total bill
bill = float(input("What was the total bill? $"))
#Asking for the tip
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
#Asking for the number of people
people = int(input("How many people to split the bill?"))
#Calculating the tip
tAmount =( bill *  tip/100) + bill
#Calculating the amount per person
tbill = round ((tAmount/ people), 2)
#Printing the amont per person
print(f"Each person should pays: $ {tbill}")

print("Welcome to the tip calculator")
total_bill = float(input('What was the total bill: $'))
tip_per = int(input("What percentage of tip would you like to give? 10, 12 or 15? "))
members = int(input("How many people to split the bill? "))
total_bill = (total_bill/members)*(1+tip_per/100)
bill = "{:.2f}".format(total_bill)
print(f"Each person should pay ${bill}")

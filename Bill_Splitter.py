print("Welcome to the Bill Splitter!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage % Tip would you like to give? 10% 12% 15% ?"))
people = int(input("How many people to split the bill? "))

pay = round(((bill + (bill * tip / 100)) / people),2)
print(f"The Bill for each person is : {pay}")
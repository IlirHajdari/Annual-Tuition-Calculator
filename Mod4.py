tuition = int(input("Enter the current annual tuition: "))
print()
rateIncrease = 0.03

#Print current amount
print("The current annual tuition amount = ${}" .format(tuition))
print()

#Loop
for i in range(1,11):
    yearlyIncrease = tuition + (tuition * rateIncrease)
    print("Year {}" .format(i))
    print ("Projected annual tuition = ${:,.2f}" .format(yearlyIncrease))
    print()
    tuition += tuition * rateIncrease
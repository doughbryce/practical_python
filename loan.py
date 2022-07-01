# get the loan details

money_owed = float(input("how much money do you owe, in dollars?\n"))
apr = float(input("what is the apr?\n"))
payment = float(input("what will your monthly payment be in dollars?\n"))
months = int(input("how many monthly payments will you make?\n"))


monthly_rate = apr/100/12

for i in range(months):

    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment <= 0):
        print("the last mayment is %s" % money_owed)
        print("you paid off the loan in ", i + 1, " months")
        break

    money_owed = money_owed - payment

    print ("paid", payment, "of which", interest_paid, "was interest", end = " ")
    print ("now I owe", money_owed)
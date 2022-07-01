expenses = [10.5, 3, 45, 7.6, 6, 18]
sum = 0

for i in range(5):
    expenses.append(float(input("enter an expense from this week:\n")))

for x in expenses:
    sum += x

print ("you spent %s this week." % sum)

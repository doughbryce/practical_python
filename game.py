import random
from typing import Counter


def ask_for_number():
    guess = int(input("guess the number: "))
    return guess

def main():
    name = input("what is your name:\n")

    print("hello %s, ive got a challenge for you" % name)
    print ("im thinking of a number between 1 and 100")

    random_num = random.randint(1, 100)
    print(random_num)

    keep_going = True
    counter = 0

    while (keep_going):
        guess = ask_for_number()
        if (guess == random_num):
            print("you got it correct in %s tries, the number was %s" % (counter, random_num))

            keep_going = False
        elif (guess < random_num):
            print("too low, try again")
            counter += 1
        elif (guess > random_num):
            print("too high, try again")
            counter += 1

main()
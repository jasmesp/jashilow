from random import randint

easyrandomnumber = randint(1, 10)
mediumrandomnumber = randint(1, 100)
hardrandomnumber = randint(1, 1000)

easyrandomchance = 0
mediumrandomchance = 0
hardrandomchance = 0

print("1. Easy")
print("2. Medium")
print("3. Hard")
print()

x = input("Pick Menu Number: ")
print()

while True:

    if x == "1":
        usernum = int(input("Guess a number (1-10): "))
        print()

        if usernum == easyrandomnumber:
            print("You got it right!", "The number is", easyrandomnumber)
            print()
            break

        elif usernum > easyrandomnumber:
            print("Go Lower!")
            print()

            easyrandomchance += 1

            print("You Have", 5 - easyrandomchance, "More Chances")
            print()

            if easyrandomchance == 5:
                print("You Lose! Try Again")
                break

        elif usernum < easyrandomnumber:
            print("Go Higher!")
            print()

            easyrandomchance += 1

            print("You have", 5 - easyrandomchance, "More Chances")
            print()

            if easyrandomchance == 5:
                print("You Lose! Try Again")
                break

    elif x == "2":
        usernum = int(input("Guess a Number (1 - 100): "))
        print()

        if usernum == mediumrandomnumber:
            print("you Got it Right!", "The Number is", mediumrandomnumber)
            print()
            break

        elif usernum > mediumrandomnumber:
            print("Go Lower!")
            print()

            mediumrandomchance += 1

            print("You Have", 10 - mediumrandomchance, "More Chances")
            print()

            if mediumrandomchance == 10:
                print("You Lose! Try Again")

        elif usernum < mediumrandomnumber:
            print("Go Higher!")
            print()

            mediumrandomchance += 1

            print("You Have", 10 - mediumrandomchance, "More Chances")
            print()

            if mediumrandomchance == 10:
                print("You Lose! Try Again")
                break

    elif x == "3":
        usernum = int(input("Guess a Number (1-1000): "))
        print()

        if usernum == hardrandomnumber:
            print("You Got it Right!")
            print()
            break

        elif usernum > hardrandomnumber:
            print("Go Lower!")
            print()

            hardrandomchance += 1

            print("You Have", 25 - hardrandomchance, "More Chances")
            print()

            if hardrandomchance == 25:
                print("You Lose! Try Again")

        elif usernum < hardrandomnumber:
            print("Go Higher!")
            print()

            hardrandomchance += 1

            print("You Have", 25 - hardrandomchance, "More Chances")
            print()

            if hardrandomchance == 25:
                print("You Lose! Try Again")
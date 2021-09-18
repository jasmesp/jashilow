from random import randint
def random_int(difficulty):
    if difficulty == 1:
        return randint(1, 10)
    if difficulty == 2:
        return randint(1, 100)
    if difficulty == 3:
        return randint(1, 1000)
def start_screen():
    print("Welcome to jasHi-Low!\n")
    print("Please choose a difficulty:\n")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Quit")
    diff = int(input("\n"))
    if (diff) > 4 or (diff) < 1:
        print("Please choose a valid difficulty.")
        start_screen()
    return diff
difficulty = start_screen()
def game(seed, chances):
    while chances > 0:
        guess = int(input("Guess a number from fix this later\n"))
        print(seed)
        secretnum = random_int(seed)
        print(secretnum)
        if guess > secretnum:
            print("Too high")
            chances -= 1
            print(str(chances) + " guesses left")
        elif guess < secretnum:
            print("Too low")
            chances -= 1
            print(str(chances) + " guesses left")
        elif guess == secretnum:
            print("Correct, the number was" + str(random_int(difficulty)))
            start_screen()
if difficulty == 1:
    game(1, 5)
elif difficulty == 2:
    game(2, 10)
elif difficulty == 3:
    game(3, 25)
elif difficulty == 4:
    print("Peace out")
    quit()

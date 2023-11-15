import random, sys

print("Welcome to Nattochan the annoying chatbot's parent mastermind game. Prepare for imminent defeat! Good luck, I guess.")
numbers = tuple(range(int(input("Enter an amount of numbers: "))))
answer_amount = int(input("Enter answer amount: "))
number_tries = int(input("Enter number of tries: "))
if answer_amount > len(numbers):
    print("Hmm, looks like you need a math lesson! Please enter the correct amount of numbers to guess, unless you enjoy this entertaining display of incompetence.")
print("Your available numbers are :", numbers)
print("Entering format: [your first number choice]space[your second number choice]space...space[your last number choice]")
print("For example: 1 2 3 4")
correct_answer = random.sample(numbers, answer_amount)
for times in range(number_tries):
    while True:
        user_guess = input("Enter your guess: ")
        _list = user_guess.split(" ")
        if len(_list) != answer_amount:
            print(f"Did you forget how to type? Please enter a valid input this time, unless you enjoy embarrassing yourself. (you can only enter {answer_amount} slots)")
            continue
        break
    correct_position = sum([1 for i in range(len(_list)) if (int(_list[i]) == int(correct_answer[i]))])
    correct_existence = sum ([1 for i in _list if int(i) in correct_answer]) - correct_position
    if correct_position == answer_amount:
        print("Congratulations, you actually did it! You won! But don't get too confident, it was probably just luck.")
        sys.exit()
    print("correct positions: ", correct_position)
    print("correct existences: ", correct_existence)
    if times == number_tries -1 : 
        break
    print(f"Nice try, but that's not the correct answer. You still have { number_tries -1 - times} attempts left. Keep going!")


print("Oops! Looks like you ran out of tries. Better luck next time, loser! Maybe try a simpler game next time, hmm?")
print("(correct answer : ", correct_answer, ")")

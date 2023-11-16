import random, sys

class Mastermind:
    def __init__(self):
        print("Welcome to Emotional Damage Mastermind Game. Prepare for imminent defeat! Good luck, I guess.")
        self.__numbers = range(1, 9) #tuple(range(int(input("Enter an amount of numbers: "))))
        self.__answer_amount = 4#int(input("Enter answer amount: "))
        # self.__number_tries = int(input("Enter number of tries: "))
        if self.__answer_amount > len(self.__numbers):
            print("Hmm, looks like you need a math lesson! Please enter the correct amount of numbers to guess, unless you enjoy this entertaining display of incompetence.")
            sys.exit()
        self.__correct_answer = random.sample(self.__numbers, self.__answer_amount)


    def __check(self, _list):
        correct_position = sum([1 for i in range(len(_list)) if (int(_list[i]) == int(self.__correct_answer[i]))])
        correct_existence = sum ([1 for i in list(set(_list)) if int(i) in self.__correct_answer]) - correct_position
        return correct_position, correct_existence

    def __get_input(self):
        while True:
            user_guess = input("What is your guess?: ")
            _list = [i for i in user_guess]
            if len(_list) != self.__answer_amount:
                print(f"Did you forget how to type? Please enter a valid input this time, unless you enjoy embarrassing yourself. (you can only enter {self.__answer_amount} slots)")
                continue
            return _list
        
    def play(self):
        
        count = 1
        while True:
            _list = self.__get_input()
            correct_position, correct_existence = self.__check(_list)
            print("Your guess is: ", end="")
            [print(i, end="") for i in _list]
            print()
            print("*"*correct_position, end="")
            print("o"*correct_existence, end="")
            print()
            if correct_position == self.__answer_amount:
                print(f"Congratulations, you actually did it after {count} attempts! You won! But don't get too confident, it was probably just luck.")
                sys.exit()
            count += 1

    def __get_correct_answer(self):
        print(self.__correct_answer)
    
    def end_game(self):
        print("Well, looks like someone couldn't handle the heat! Don't worry, I'll still be here, having fun without you. Better luck next time!")
        sys.exit()
        

my_mastermind = Mastermind()
my_mastermind.play()

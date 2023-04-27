import random

number1 = 0
number2 = 0
add_answer = 0
sub_answer = 0
user_answer = 0
user_guesses = 0

print('Welcome to Math Quiz\n\n\nMAIN MENU\n--------------------\n1. Adding Random Numbers\n2. Subtracting Random Numbers\n3. Exit\n')
menu_input = int(input('Please choose one of the menu options: '))

while menu_input != 3:
    while menu_input == 1:
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        add_answer = number1 + number2
        print(' ', number1, '\n+', number2, '\n')
        user_answer = int(input('Enter answer.\n'))
        while user_answer != add_answer:
            if user_answer < add_answer:
                user_guesses = user_guesses + 1
                print('Sorry, guess is too low.\n')
                user_answer = int(input('Try again: '))
            if user_answer > add_answer:
                user_guesses = user_guesses + 1
                print('Sorry, guess is too high.\n')
                user_answer = int(input('Try again: '))
        user_guesses = user_guesses + 1
        print('Congratulations!!!! Your answer is correct.\nNumber of guesses:', user_guesses, '\n\nMAIN MENU\n--------------------\n1. Adding Random Numbers\n2. Subtracting Random Numbers\n3. Exit\n')
        user_guesses = 0
        menu_input = int(input('Please choose one of the menu options: '))
    while menu_input == 2:
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        while number1 < number2:
            number1 = random.randint(1, 10)
            number2 = random.randint(1, 10)
        sub_answer = number1 - number2
        print(' ', number1, '\n-', number2, '\n')
        user_answer = int(input('Enter answer.\n'))
        while user_answer != sub_answer:
            if user_answer < sub_answer:
                user_guesses = user_guesses + 1
                print('Sorry, guess is too low.\n')
                user_answer = int(input('Try again: '))
            if user_answer > sub_answer:
                user_guesses = user_guesses + 1
                print('Sorry, guess is too high.\n')
                user_answer = int(input('Try again: '))
        user_guesses = user_guesses + 1
        print('Congratulations!!!! Your answer is correct.\nNumber of guesses:', user_guesses, '\n\nMAIN MENU\n--------------------\n1. Adding Random Numbers\n2. Subtracting Random Numbers\n3. Exit\n')
        user_guesses = 0
        menu_input = int(input('Please choose one of the menu options: '))
    while menu_input != 1 and menu_input != 2 and menu_input != 3:
        print('\nERROR: Please enter the number 1, 2 or 3!')
        menu_input = int(input('\nTry again: '))

print('Thank you for playing...\nBye!!')

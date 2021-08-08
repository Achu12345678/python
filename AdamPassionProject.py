# Python Program - written by Adam Tomydas

import random
import string
import turtle as t

def password_picker():
    password_picker_repeat = True
    while(password_picker_repeat == True):
        print('\nWelcome to the Password Picker')
        colors = ['red', 'blue', 'yellow', 'green', 'black']
        animals = ['dog', 'cat', 'goat', 'duck', 'panda']
        color = random.choice(colors)
        animal = random.choice(animals)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)
        password = color + animal + str(number) + special_char
        print('Your new password is: %s' %password)
        chose_correct = True
        while(chose_correct):
            repeat = input('Would you like a new password? (y/n) ')
            if repeat == 'n':
                print('Thank you for using the Password Picker!')
                password_picker_repeat = False
                break

            elif repeat == 'y':
                chose_correct = False
                password_picker_repeat = True

            else:
                print('Please choose y or n, and try again.')
                chose_correct = True
            
    

def drawing():
    print('\nWelcome to Drawing!')
    repeat_drawing = True
    while(repeat_drawing):
        move = input('Type F to go forward, B to go backward, L to go left, R to go right, and type E to exit Drawing.')
        if move.upper() == 'F':
            t.fd(50)

        elif move.upper() == 'L':
            t.lt(90)
            t.fd(50)

        elif move.upper() == 'B':
            t.bk(50)
            

        elif move.upper() == 'R':
            t.rt(90)
            t.fd(50)

        elif move.upper() == 'E':
            repeat_drawing = False
            print('Thanks for Drawing!')
            break
    

def the_animal_quiz():
    print('\nWelcome to the Animal Quiz!')
    quiz_type = input('Type A to start!')
    if quiz_type.upper() == 'A':
        #print('You chose the Animal Quiz')
        animal_quiz()

def animal_quiz():
    print('Welcome to the Animal Quiz')
    score = 0
    animal_quiz_repeat = True
    while(animal_quiz_repeat == True):
        print('Guess The Animal!')
        animals = ['LION', 'TIGER', 'CAT', 'DOG', 'COW', 'HORSE', 'MOOSE', 'ZEBRA']
        animal = random.choice(animals)
        #print('The animal that has been chosen is a', animal)
        answer = input('Clue 1: My animal has four legs, Type your answer.')

        if answer.upper() == animal:
            print('Correct! You got 10 points!')
            score += 10
            print('Thank you playing the Animal Quiz! Your score is ',score)

        else:
            print('Incorrect, try again.')
            print('Your score is ',score)

            if (animal == 'LION') or (animal == 'TIGER') or (animal == 'CAT') or (animal == 'DOG'):
                answer = input('Clue 2: My animal is a meat eater, Type your answer.')
                

                if answer.upper() == animal:
                    print('Correct! You got 8 points!')
                    score += 8
                    print('Thank you playing the Animal Quiz! Your score is ',score)

                else:
                    print('Incorrect, try again.')
                    print('Your score is ',score)
                    if (animal == 'LION') or (animal == 'TIGER'):
                        answer = input('Clue 3: My animal is a wild animal, Type your answer.')
                        if answer.upper() == animal:
                            print('Correct! You got 6 points!')
                            score += 6
                            print('Thank you playing the Animal Quiz! Your score is ',score)

                        else:
                            print('Incorrect, try again.')
                            print('Your score is ',score)

                            if (animal == 'LION'):
                                answer = input('Clue 4: My animal has a mane, Type your answer.')
                                if answer.upper() == animal:
                                    print('Correct! You got 4 points!')
                                    score += 4
                                    print('Thank you playing the Animal Quiz! Your score is ',score)

                                else:
                                    print('You have failed the Animal Quiz, try again next time.')
                                    print('Your score is ',score)

                            elif (animal == 'TIGER'):
                                answer = input('Clue 4: My animal has stripes, Type your answer.')
                                if answer.upper() == animal:
                                    print('Correct! You got 4 points!')
                                    score += 4
                                    print('Thank you playing the Animal Quiz! Your score is ',score)

                                else:
                                    print('You have failed the Animal Quiz, try again next time.')
                                    print('Your score is ',score)

                       
                    elif (animal == 'CAT') or (animal == 'DOG'):
                        answer = input('Clue 3: My animal is a pet, Type your answer.')
                        if answer.upper() == animal:
                            print('Correct! You got 6 points!')
                            score += 6
                            print('Thank you playing the Animal Quiz! Your score is ',score)

                        else:
                            print('Incorrect, try again.')
                            print('Your score is ',score)

                            if (animal == 'CAT'):
                                answer = input('Clue 4: My animal can meow, Type your answer.')
                                if answer.upper() == animal:
                                    print('Correct! You got 4 points!')
                                    score += 4
                                    print('Thank you playing the Animal Quiz! Your score is ',score)

                                else:
                                    print('You have failed the Animal Quiz, try again next time.')
                                    print('Your score is ',score)

                            elif (animal == 'DOG'):
                                answer = input('Clue 4: My animal can bark, Type your answer.')
                                if answer.upper() == animal:
                                    print('Correct! You got 4 points!')
                                    score += 4
                                    print('Thank you playing the Animal Quiz! Your score is ',score)
                                    
                                    

                                else:
                                    print('You have failed the Animal Quiz, try again next time.')
                                    print('Your score is ',score)

                    else:
                        print('Incorrect, try again.')
                        print('Your score is ',score)
                            
                

            elif (animal == 'COW') or (animal == 'HORSE') or (animal == 'MOOSE') or (animal == 'ZEBRA'):
                answer = input('Clue 2: My animal is a plant eater, Type your answer.')
                

                if answer.upper() == animal:
                    print('Correct! You got 8 points!')
                    score += 8
                    print('Your score is ',score)

                else:
                    print('Incorrect, try again.')
                    print('Your score is ',score)

                    if (animal == 'MOOSE') or (animal == 'ZEBRA'):
                        answer = input('Clue 3: My animal is a wild animal, Type your answer.')
                        if answer.upper() == animal:
                            print('Correct! You got 6 points!')
                            score += 6
                            print('Thank you playing the Animal Quiz! Your score is ',score)

                        else:
                            print('Incorrect, try again.')
                            print('Your score is ',score)

                            if (animal == 'MOOSE'):
                                answer = input('Clue 4: My animal has antlers, Type your answer.')
                                if answer.upper() == animal:
                                    print('Correct! You got 4 points!')
                                    score += 4
                                    print('Thank you playing the Animal Quiz! Your score is ',score)

                                else:
                                    print('You have failed the Animal Quiz, try again next time.')
                                    print('Your score is ',score)

                            elif (animal == 'ZEBRA'):
                                answer = input('Clue 4: My animal has stripes, Type your answer.')
                                if answer.upper() == animal:
                                    print('Correct! You got 4 points!')
                                    score += 4
                                    print('Thank you playing the Animal Quiz! Your score is ',score)

                                else:
                                    print('You have failed the Animal Quiz, try again next time.')
                                    print('Your score is ',score)

                       
                    elif (animal == 'COW') or (animal == 'HORSE'):
                        answer = input('Clue 3: My animal is a farm animal, Type your answer.')
                        if answer.upper() == animal:
                            print('Correct! You got 6 points!')
                            score += 6
                            print('Thank you playing the Animal Quiz! Your score is ',score)

                        else:
                            print('Incorrect, try again.')
                            print('Your score is ',score)

                            if (animal == 'COW'):
                                answer = input('Clue 4: My animal can give milk, Type your answer.')
                                if answer.upper() == animal:
                                    print('Correct! You got 4 points!')
                                    score += 4
                                    print('Thank you playing the Animal Quiz! Your score is ',score)

                                else:
                                    print('You have failed the Animal Quiz, try again next time.')
                                    print('Your score is ',score)

                            elif (animal == 'HORSE'):
                                answer = input('Clue 4: You can ride on my animal, Type your answer.')
                                if answer.upper() == animal:
                                    print('Correct! You got 4 points!')
                                    score += 4
                                    print('Thank you playing the Animal Quiz! Your score is ',score)
                                    
                                    

                                else:
                                    print('You have failed the Animal Quiz, try again next time.')
                                    print('Your score is ',score)

                    else:
                        print('Incorrect, try again.')
                        print('Your score is ',score)

        repeat = input('Do you want to play the Animal quiz again? (y/n) ')
        if repeat == 'n':
                animal_quiz_repeat = False
                print('Thank you for playing the Animal Quiz, your final score is', score)
                break


print('Passion Project - Game developed in Python by Achu')
print('----------------------------------------------------------')
print('\n')

name = input('What is your name?')
print('Hello, ' + name)

while True:
    print('Choose one of the following, ' + name)

    chose_wrong = False
    while(chose_wrong == False):
    
        choice = input('Type 1 for Password Picker, 2 for Drawing, and 3 for the Animal Quiz!')

        if choice == '1':
            #print('You chose the Password Picker')
            chose_wrong = True
            password_picker()
            

        elif choice == '2':
            #print('You chose Drawing')
            chose_wrong = True
            drawing()

        elif choice == '3':
            #print('You chose the Quiz')
            chose_wrong = True
            the_animal_quiz()

        else:
            print('Choose one of the numbers listed, try again.')
            chose_wrong = False

    answer = input('Would you like to try something else? (y/n) ')

    if answer == 'n':
        print("Goodbye " + name)
        break


from this import d
from tkinter import N
import pandas as pd
dictionary = pd.read_csv("C:\\Users\\User\\vscode\\valid_guesses.csv", )
# dictionary.set_index("word", inplace=True)
import csv









nog = 0
#ONLY LETTER KNOWN
while nog != 10:
    q1 = input('How many letters in green: ')
    l1 = input('How many letters in yellow: ')
    #0 GREEN 1 YELLOW
    if q1 == "0" and l1 == "1":
        l_guess = input('Enter letter in yellow: ')
        no1 = input('Enter letter 1 not present in word: ')
        no2 = input('Enter letter 2 not present in word: ')
        no3 = input('Enter letter 3 not present in word: ')
        no4 = input('Enter letter 4 not present in word: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if l_guess in guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
                    else:
                        if l_guess in guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
    nog += 1
    #0 GREEN 2 YELLOW
    if q1 == "0" and l1 == "2":
        l_guess = input('Enter letter 1 in yellow: ')
        no1 = input('Enter letter 2 in yellow: ')
        no2 = input('Enter letter 1 not present in word: ')
        no3 = input('Enter letter 2 not present in word: ')
        no4 = input('Enter letter 3 not present in word: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if l_guess in guess and no1 in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
                    else:
                        if l_guess in guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
                    
    nog += 1
    #0 GREEN 3 YELLOW
    if q1 == "0" and l1 == "3":
        l_guess = input('Enter 1st letter in yellow: ')
        no1 = input('Enter 2nd letter in yellow: ')
        no2 = input('Enter 3rd letter in yellow: ')
        no3 = input('Enter 1st letter  not present in word: ')
        no4 = input('Enter 2nd letter not present in word: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if l_guess in guess and no1 in guess and no2 in guess and no3 not in guess and no4 not in guess:
                            print (guess)
                    else:
                        if l_guess in guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
    nog += 1
    #0 GREEN 4 YELLOW
    if q1 == "0" and l1 == "4":
        l_guess = input('Enter 1st letter in yellow: ')
        no1 = input('Enter 2nd letter in yellow: ')
        no2 = input('Enter 3rd letter in yellow: ')
        no3 = input('Enter 4th letter in yellow: ')
        no4 = input('Enter letter not present in word: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if l_guess in guess and no1 in guess and no2 in guess and no3 in guess and no4 not in guess:
                            print (guess)
                    else:
                        if l_guess in guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
    nog += 1
    #0 GREEN 5 YELLOW
    if q1 == "0" and l1 == "5":
        l_guess = input('Enter 1st letter in yellow: ')
        no1 = input('Enter 2nd letter in yellow: ')
        no2 = input('Enter 3rd letter in yellow: ')
        no3 = input('Enter 4th letter in yellow: ')
        no4 = input('Enter 5th letter in yellow: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if l_guess in guess and no1 in guess and no2 in guess and no3 in guess and no4 in guess:
                            print (guess)
                    else:
                        if l_guess in guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
    nog += 1
    #1 GREEN 0 YELLOW
    if q1 == "1" and l1 == "0":
        l_guess = input('Enter letter in green: ')
        qp = int(input('Enter position of green letter?: '))
        no1 = input('Enter 1st letter not present in word: ')
        no2 = input('Enter 2nd letter not present in word: ')
        no3 = input('Enter 3rd tter not present in word: ')
        no4 = input('Enter 4th letter not present in word: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if 0 <= qp <=5:
                        if l_guess in guess and guess[qp] == l_guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
                    else:
                        if l_guess in guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
    nog += 1
    #1 GREEN 1 YELLOW
    if q1 == "1" and l1 == "1":
        l_guess = input('Enter letter in green: ')
        qp = int(input('Enter position of green letter: '))
        no1 = input('Enter letter in yellow: ')
        no2 = input('Enter 1st letter not present in word: ')
        no3 = input('Enter 2nd letter not present in word: ')
        no4 = input('Enter 3rd letter not present in word: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if 0 <= qp <=5:
                        if l_guess in guess and guess[qp] == l_guess and no1 in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
                    else:
                        if l_guess in guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
    nog += 1
    #1 GREEN 2 YELLOW
    if q1 == "1" and l1 == "2":
        l_guess = input('Enter letter in green: ')
        qp = int(input('Enter position of green letter: '))
        no1 = input('Enter 1st letter in yellow: ')
        no2 = input('Enter 2nd letter in yellow: ')
        no3 = input('Enter 1st letter not present in word: ')
        no4 = input('Enter 2nd letter not present in word: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if 0 <= qp <=5:
                        if l_guess in guess and guess[qp] == l_guess and no1 in guess and no2 in guess and no3 not in guess and no4 not in guess:
                            print (guess)
                    else:
                        if l_guess in guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
    nog += 1
    #1 GREEN 3 YELLOW
    if q1 == "1" and l1 == "3":
        l_guess = input('Enter letter in green: ')
        qp = int(input('Enter position of green letter: '))
        no1 = input('Enter 1st letter in yellow: ')
        no2 = input('Enter 2nd letter in yellow: ')
        no3 = input('Enter 3rd letter in yellow: ')
        no4 = input('Enter letter not present in word: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if 0 <= qp <=5:
                        if l_guess in guess and guess[qp] == l_guess and no1 in guess and no2 in guess and no3 in guess and no4 not in guess:
                            print (guess)
                    else:
                        if l_guess in guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
    nog += 1
    #1 GREEN 4 YELLOW
    if q1 == "1" and l1 == '4':
        l_guess = input('Enter letter in green: ')
        qp = int(input('Enter position of green letter: '))
        no1 = input('Enter 1st letter in yellow: ')
        no2 = input('Enter 2nd letter in yellow: ')
        no3 = input('Enter 3rd letter in yellow: ')
        no4 = input('Enter 4th letter in yellow: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if 0 <= qp <=5:
                        if l_guess in guess and guess[qp] == l_guess and no1 in guess and no2 in guess and no3 in guess and no4 in guess:
                            print (guess)
                    else:
                        if l_guess in guess and no1 not in guess and no2 not in guess and no3 not in guess and no4 not in guess:
                            print (guess)
    nog += 1
    #2 GREEN 0 YELLOW
    if q1 == "2" and l_guess == '0':
         l_guess = input('Enter green letter 1: ')
         qp = int(input('Enter position of green letter?: '))
         l_guess2 = input('Enter green letter 2: ')
         qp2 = int(input('Enter position of green letter: '))
         no1 = input('Enter 1st letter not present in word: ')
         no2 = input('Enter 2nd letter not present in word: ')
         no3 = input('Enter 3rd letter not present in word: ')
         with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
             reader = csv.reader(f, delimiter=',') # good point by @paco
             for row in reader:
                 for guess in row:
                     guess.index
                     if 0 <= qp <=5 and 0 <= qp2 <=5:
                         if l_guess in guess and guess[qp] == l_guess and l_guess2 in guess and guess[qp2] == l_guess2 and no1 not in guess and no2 not in guess and no3 not in guess:
                             print (guess)
                     else:
                         if l_guess in guess and l_guess2 in guess and no1 not in guess and no2 not in guess and no3 not in guess:
                             print (guess)
    nog += 1
    #2 GREEN 1 YELLOW
    if q1 == "2" and l1 == '1':
        l_guess = input('Enter green letter 1: ')
        qp = int(input('Enter position of green letter: '))
        l_guess2 = input('Enter letter green 2: ')
        qp2 = int(input('Enter position of letter: '))
        no1 = input('Enter letter in yellow: ')
        no2 = input('Enter 1st letter not present in word: ')
        no3 = input('Enter 2nd letter not present in word: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if 0 <= qp <=5 and 0 <= qp2 <=5:
                        if l_guess in guess and guess[qp] == l_guess and l_guess2 in guess and guess[qp2] == l_guess2 and no1 in guess and no2 not in guess and no3 not in guess:
                            print (guess)
                    else:
                        if l_guess in guess and l_guess2 in guess and no1 not in guess and no2 not in guess and no3 not in guess:
                            print (guess)
    nog += 1
    #2 GREEN 2 YELLOW
    if q1 == "2" and l1 == '2':
        l_guess = input('Enter green letter 1: ')
        qp = int(input('Enter position of green letter: '))
        l_guess2 = input('Enter green letter 2: ')
        qp2 = int(input('Enter position of green letter:: '))
        no1 = input('Enter 1st letter in yellow: ')
        no2 = input('Enter 2nd letter in yellow: ')
        no3 = input('Enter letter not present in word: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if 0 <= qp <=5 and 0 <= qp2 <=5:
                        if l_guess in guess and guess[qp] == l_guess and l_guess2 in guess and guess[qp2] == l_guess2 and no1 in guess and no2 in guess and no3 not in guess:
                            print (guess)
                    else:
                        if l_guess in guess and l_guess2 in guess and no1 not in guess and no2 not in guess and no3 not in guess:
                            print (guess)
    nog += 1
    #2 GREEN 3 YELLOW
    if q1 == "2" and l1 == '3':
        l_guess = input('Enter green letter 1: ')
        qp = int(input('Enter position of green letter:: '))
        l_guess2 = input('Enter green letter 2: ')
        qp2 = int(input('Enter position of green letter:: '))
        no1 = input('Enter 1st letter in yellow: ')
        no2 = input('Enter 2nd letter in yellow: ')
        no3 = input('Enter 3rd letter in yellow: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if 0 <= qp <=5 and 0 <= qp2 <=5:
                        if l_guess in guess and guess[qp] == l_guess and l_guess2 in guess and guess[qp2] == l_guess2 and no1 in guess and no2 in guess and no3 in guess:
                            print (guess)
                    else:
                        if l_guess in guess and l_guess2 in guess and no1 not in guess and no2 not in guess and no3 not in guess:
                            print (guess)
    nog += 1
    #3 GREEN 0 YELLOW
    if q1 == "3":
         l_guess = input('Enter letter 1: ')
         qp = int(input('Do you know position of letter?: '))
         l_guess2 = input('Enter letter 2: ')
         qp2 = int(input('Do you know position of letter?: '))
         l_guess3 = input('Enter green letter 3: ')
         qp3 = int(input('Enter position of green letter:: '))
         no1 = input('Enter 1st letter not present in word: ')
         no2 = input('Enter 2nd letter not present in word: ')
         with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
             reader = csv.reader(f, delimiter=',') # good point by @paco
             for row in reader:
                 for guess in row:
                     guess.index
                     if 0 <= qp <=5 and 0 <= qp2 <=5 and 0 <= qp3 <=5:
                         if l_guess in guess and guess[qp] == l_guess and l_guess2 in guess and guess[qp2] == l_guess2 and l_guess3 in guess and guess[qp3] == l_guess3 and no1 not in guess and no2 not in guess:
                             print (guess)
                     else:
                         if l_guess in guess and l_guess2 in guess and l_guess3 in guess and no1 not in guess and no2 not in guess:
                             print (guess)
    nog += 1
    #3 GREEN 1 YELLOW
    if q1 == "3" and l1 == '1':
        l_guess = input('Enter letter 1: ')
        qp = int(input('Do you know position of letter?: '))
        l_guess2 = input('Enter letter 2: ')
        qp2 = int(input('Do you know position of letter?: '))
        l_guess3 = input('Enter letter 3: ')
        qp3 = int(input('Do you know position of letter?: '))
        no1 = input('Enter letter in yellow: ')
        no2 = input('Enter letter not present in word: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if 0 <= qp <=5 and 0 <= qp2 <=5 and 0 <= qp3 <=5:
                        if l_guess in guess and guess[qp] == l_guess and l_guess2 in guess and guess[qp2] == l_guess2 and l_guess3 in guess and guess[qp3] == l_guess3 and no1 in guess and no2 not in guess:
                            print (guess)
                    else:
                        if l_guess in guess and l_guess2 in guess and l_guess3 in guess and no1 not in guess and no2 not in guess:
                            print (guess)
    nog += 1
    
    #3 GREEN 2 YELLOW
    if q1 == "3" and l1 == '2':
        l_guess = input('Enter green letter 1: ')
        qp = int(input('Enter position of green letter:: '))
        l_guess2 = input('Enter green letter 2: ')
        qp2 = int(input('Enter position of green letter:: '))
        l_guess3 = input('Enter green letter 3: ')
        qp3 = int(input('Enter position of green letter:: '))
        no1 = input('Enter 1st letter in yellow: ')
        no2 = input('Enter 2nd letter in yellow: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if 0 <= qp <=5 and 0 <= qp2 <=5 and 0 <= qp3 <=5:
                        if l_guess in guess and guess[qp] == l_guess and l_guess2 in guess and guess[qp2] == l_guess2 and l_guess3 in guess and guess[qp3] == l_guess3 and no1 in guess and no2 in guess:
                            print (guess)
                    else:
                        if l_guess in guess and l_guess2 in guess and l_guess3 in guess and no1 not in guess and no2 not in guess:
                            print (guess)
    nog += 1
    #4 GREEN 0 YELLOW
    if q1 == "4":
         l_guess = input('Enter green letter 1: ')
         qp = int(input('Enter position of green letter:: '))
         l_guess2 = input('Enter green letter 2: ')
         qp2 = int(input('Enter position of green letter:: '))
         l_guess3 = input('Enter green letter 3: ')
         qp3 = int(input('Enter position of green letter:: '))
         l_guess4 = input('Enter green letter 4: ')
         qp4 = int(input('Enter position of green letter:: '))
         no1 = input('Enter letter not present in word: ')
         with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
             reader = csv.reader(f, delimiter=',') # good point by @paco
             for row in reader:
                 for guess in row:
                     guess.index
                     if 0 <= qp <=5 and 0 <= qp2 <=5 and 0 <= qp3 <=5 and 0 <= qp4 <= 5:
                         if l_guess in guess and guess[qp] == l_guess and l_guess2 in guess and guess[qp2] == l_guess2 and l_guess3 in guess and guess[qp3] == l_guess3 and l_guess4 in guess and guess[qp4] == l_guess4 and no1 not in guess:
                                 print (guess)
                     else:
                         if l_guess in guess and l_guess2 in guess and l_guess3 in guess and l_guess4 in guess and no1 not in guess:
                             print (guess)
    nog += 1
    #4 GREEN 1 YELLOW
    if q1 == "4" and l1 == '1':
        l_guess = input('Enter green letter 1: ')
        qp = int(input('Enter position of green letter:: '))
        l_guess2 = input('Enter green letter 2: ')
        qp2 = int(input('Enter position of green letter:: '))
        l_guess3 = input('Enter green letter 3: ')
        qp3 = int(input('Enter position of green letter:: '))
        l_guess4 = input('Enter green letter 4: ')
        qp4 = int(input('Enter position of green letter:: '))
        no1 = input('Enter letter in yellow: ')
        with open('C:\\Users\\User\\vscode\\valid_guesses.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for guess in row:
                    guess.index
                    if 0 <= qp <=5 and 0 <= qp2 <=5 and 0 <= qp3 <=5 and 0 <= qp4 <= 5:
                        if l_guess in guess and guess[qp] == l_guess and l_guess2 in guess and guess[qp2] == l_guess2 and l_guess3 in guess and guess[qp3] == l_guess3 and l_guess4 in guess and guess[qp4] == l_guess4 and no1 in guess:
                                print (guess)
                    else:
                        if l_guess in guess and l_guess2 in guess and l_guess3 in guess and l_guess4 in guess and no1 not in guess:
                            print (guess)
    nog += 1
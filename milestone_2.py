#Choosing a random word from a list of given fruits
import random
word_list = ['pineapple', 'strawberry', 'mango', 'apple', 'kiwi']
#print(word_list)
word = random.choice(word_list)
#print(word)

#Asking the user to enter input, guessing a letter.
#guess = input('Please enter a single letter: ')

#Validating user input 
guess = input('Please enter a single letter: ')

if len(guess) == 1 and type(guess) == str: 
    print('Good guess!')
else:
    print('Oops, that is not a valid input')
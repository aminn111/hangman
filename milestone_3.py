#Create a while loop to constantly validate the user input. 
import random
word_list = ['pineapple', 'strawberry', 'mango', 'apple', 'kiwi']
#print(word_list)
word = random.choice(word_list)
       
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess. {guess} is in the word')
    else:
        print('Please try again')

def ask_for_input():
    while True:
        guess = input('Please enter a letter: ')
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character")
    check_guess(guess)

ask_for_input()
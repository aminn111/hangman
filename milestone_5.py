import random

word_list = ['pineapple', 'strawberry', 'mango', 'apple', 'kiwi']
word = random.choice(word_list)

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

        self.word = word
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess. {guess} is in the word')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
                    print(self.word_guessed)
            self.num_letters -=1
        else:
            self.num_lives -= 1
            print(f'Sorry,{guess} is not in the word')
            print(f'You have {self.num_lives} lives left') 
            print('Please try again')
    
    def ask_for_input(self):
        while True:
            guess = input('Please enter a letter: ')
            print(self.word_guessed)
            if len(guess) != 1 and not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print('You already tried that letter')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if num_lives == 0:
            print(f'You have lost the game!')
        elif num_lives > 0:
            game.ask_for_input()
        elif num_lives != 0 and game.num_letters == 0:
            print(f'Congratulations, you have guessed the word: {game.word}')
            break
        else:
            game.ask_for_input()

play_game(word_list)

        
'''
    Project 2: Hangman
'''

# Import Dependencies
import sys

def prep_game(word):
    if word.isalpha() == True:
        guess_word = word.lower()
        guess_string = ''
        
        for letter in guess_word:
            guess_string += "_"

        return guess_word, guess_string

    else:
        print("Error: The word to guess cannot contain any numbers or special characters.")
        sys.exit()

def run_startup():
    print("Welcome to Hangman!")
    print('-----------------------------------------------------------------------------------------')
    print("This is a two player game where you try and guess a word, a letter at a time.")
    print("Each letter you guess correctly will earn you points, if you guess incorrectly,")
    print("a body part will be added to the gallows. After all 6 parts, have been added you lose.")
    print("Each player takes turns guessing letters until the word is solved, or someone loses.")
    print('-----------------------------------------------------------------------------------------')
    print("If you are ready to start, player 1 please enter a word for player 2 to guess.")
    temp = input("The word: ")
    return temp

def draw_gallows(num_guesses, guess_string, guesses):
    print("------------------ Hangman -----------------")
    print("|----------|")
    print("|          |")

    guesses_so_far = ''
    if len(guesses) > 0:
        for guess in guesses:
            guesses_so_far += guess + ' '


    # Draw the head
    if num_guesses == 1:
        print("|          O")
        print("|")
        print("|")
        print("|")
        print("|")

    elif num_guesses == 2:
        print("|          O")
        print("|          -")
        print("|")
        print("|")
        print("|")

    elif num_guesses  == 3:
        print("|          O")
        print("|          ---")
        print("|")
        print("|")
        print("|")
    
    elif num_guesses == 4:
        print("|          O")
        print("|        -----")
        print("|")
        print("|")
        print("|")

    elif num_guesses == 5:
        print("|          O")
        print("|        -----")
        print("|          |")
        print("|          |")
        print("|")

    elif num_guesses == 6:
        print("|          O")
        print("|        -----")
        print("|          |")
        print("|          |")
        print("|         /")

    elif num_guesses == 7:
        print("|          O")
        print("|        -----")
        print("|          |")
        print("|          |")
        print("|         / \\")

    else:
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")


    print("|")
    print("|")
    print("|")
    print("|")
    print("--------------------------")
    print("Number of failed guesses:", num_guesses)
    print("The guesses so far: ", guesses_so_far)
    print("The word has {} letters".format(len(guess_string)))
    print(" ")
    print("The word to guess: " + guess_string)

def prompt_player(guesses):
    valid_guess = False
    current_guess = None

    print("Please enter the letter you would like to guess.")
    current_guess = input("Your Guess:")

    if len(current_guess) != 1:
        print("Please enter a single letter.")

    if current_guess.isalpha() == False:
        print("Please enter a letter.")

    if len(guesses) > 0:
        for guess in guesses:
            if guess == current_guess:
                print("Please enter a letter you have not guessed before.")

    print("-------------------------------------------------")
    print(" ")
    return current_guess
        
def main():
    guesses = set()
    input_word = run_startup()
    guess_word, guess_string = prep_game(input_word)
    num_guesses = 0

    while num_guesses < 7:
        draw_gallows(num_guesses, guess_string, guesses)
        current_guess = prompt_player(guesses)
        valid_guess = False

        guesses.add(current_guess)

        for i in range(len(guess_word)):
            if guess_word[i] == current_guess:
                guess_string = guess_string[0:i] + current_guess + guess_string[i+1:]
                valid_guess = True

        if valid_guess == False:
            num_guesses += 1

        # Check if the game has been won
        if guess_string.find('_') == -1:
            print("Congratulations! You won!")
            sys.exit()

    draw_gallows(num_guesses, guess_string, guesses)
    print("Sorry, you lost. The word was " + guess_word)


if __name__ == '__main__':
    main()
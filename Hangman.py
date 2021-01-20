from random import randint

word_list = ["REPTILE", "DUCK"]

# Prints out the guessed letters in a word
def print_the_guess(word, guessed_letters):
    list_of_letters = ", ".join(guessed_letters)
    print(f"Guessed letters: {list_of_letters}")
    global output_word
    output_word = ""
    for i in word:
        if i in guessed_letters:
            output_word += i
        else:
            output_word += "-"
    print(output_word)

# A function to draw the hangman bassed on mistakes made
def draw_hangman(mistakes):
    print(" +----+ \n"
          "\n"
          " |  | ")
    if mistakes >= 1:
        print(" O  |")
    else:
        print("    |")

    if mistakes == 2:
        print(" |  |")
    elif mistakes == 3:
        print("/|  |")
    elif mistakes >= 4:
        print("/|\ |")
    else:
        print("    |")

    if mistakes == 5:
        print("/   |")
    elif mistakes >= 6:
        print("/ \ |")
    else:
        print("    |")

    print("    |\n"
          "\n"
          " ====== ")

while True:

    #Game cycle starting point with players input
    print("Enter 1 to play hangman, 2 to add a new word, 3 to quit program")
    while True:
        try:
            choice = input("Your chice: ")
            choice = int(choice)
        except ValueError:
            print("Please enter number from 1 to 3.")
            continue
        if 1 <= choice <= 3:
            break
        else:
            print("Plese enter value from 1 to 3.")

    #Quits the game
    if choice == 3:
        break

    #Adds a word to the list
    elif choice == 2:
        while True:
            try:
                add_word = (input("add a word: ")).upper()
                assert add_word.isalpha()
                break
            except:
                print("Please enter valid input.")
        word_list.append(add_word)

    elif choice == 1 and len(word_list) == 0:
        print("There are no word in word list. Please add some words to the list.")
        continue

    # Enters Else if choice 3 was made and the actual game bigins
    else:
        mistakes_made = 0
        word = word_list[randint(0, len(word_list)-1)]
        guessed_letters = []
        output_word = ""

        while mistakes_made < 6:

            #Input of the guess letter and validation of the input
            while True:
                try:
                    guess_letter = (input("Make your guess: ")).upper()
                    assert guess_letter.isalpha()
                except:
                    print("Please enter a letter.")
                    continue
                if guess_letter in guessed_letters:
                    print(f"The letter {guess_letter} was allready previosly guest. Please make another guess.")
                elif len(guess_letter) ==1:
                    break
                else:
                    print("Please enter just one letter")

            guessed_letters.append(guess_letter)

            #Checking and drawing of the hangman
            if guess_letter in word:
                draw_hangman(mistakes_made)
                print_the_guess(word, guessed_letters)

            else:
                mistakes_made += 1
                draw_hangman(mistakes_made)
                print_the_guess(word, guessed_letters)

            # Checks the conditions for game to end
            if output_word == word:
                print("You won!\n")
                break
            elif mistakes_made == 6:
                print("You loose!\n"
                      f"The word was: {word} \n")
                break
        #Removes the word from the list
        word_list.remove(word)

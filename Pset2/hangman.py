# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    for char in secret_word:
        if char in letters_guessed:
            continue
        else:
            return False
        
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ''
    
    for char in secret_word:
       if char in letters_guessed:
           guessed_word += char + ' '
       else:
           guessed_word += '_ '
    
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available_letters = ''
    
    for char in alphabet:
        if char in letters_guessed:
            continue
        else:
            available_letters += char
            
    return available_letters

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    alphabet = string.ascii_lowercase
    letters_guessed = ''
    breaker = "-------------------"
    
    print("\nSecret word contains " + str(len(secret_word)) + " letters.")
    print("You have been given " + str(warnings) + " warnings. Play by the rules!")

    while guesses > 0:
        print("You have " + str(guesses) + " guesses remaining.")
        print("Available letters: " + get_available_letters(letters_guessed) + "")
        
        guess = input("Enter a letter: ").lower()
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        # check that guess is a single character
        if len(guess) != 1:
            print("Guess must be a single character!: " + guessed_word)
            print(breaker)
            continue
        
        # check that guess is a letter of the alphabet
        if guess not in alphabet:
            if warnings != 0:
                warnings -= 1
            else:
                guesses -=1
            print("Invalid guess. " + str(warnings) + " warnings remaining: " + guessed_word)
            print(breaker)
            continue
        
        # check if the valid guess has already been guessed
        if guess in letters_guessed:
            if warnings != 0:
                warnings -= 1
            else:
                guesses -= 1
            print("Already guessed that letter! " + str(warnings) + " warnings remaining: " + guessed_word)
            print(breaker)
            continue
        
        # add new, valid guess to letters guessed and show word in progress
        letters_guessed += guess
        # update value of guessed_word with new value in letters_guessed
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        # remove a guess if it isn't in secret word
        if guess not in secret_word and guesses != 0:
            print("Not in secret word!: " + guessed_word)
            
            if guess in 'aeiou':
                guesses -= 2
            else:
                guesses -= 1
            
            print(breaker)
            continue
        elif guess in secret_word and guesses != 0:
            print("Good guess!: " + guessed_word)

        # break out of the game if user has guessed the word
        if is_word_guessed(secret_word, letters_guessed):
            print("You won!!")
            
            score = guesses * len(letters_guessed)
            print("Score: " + str(score))
            print(breaker)
            break
        
        print(breaker)
        
    # if the user didn't guess the word, let them know the game has ended
    if guesses <= 0:
        print("Secret word was " + secret_word + ", better luck next time!")
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # my_word should always be structured as a character + whitespace, so the length of my_word should always be equal to double the length of other_word
    # returns False when other_word is of an improper length because it therefore cannot be the same as my_word
    if len(my_word) != len(other_word)*2:
        return False
    
    # strip whitespace out of my_word, save as my_word_stripped
    # save unique alphabetic chars of my_word to my_word_chars
    my_word_stripped = ''
    my_word_chars = ''
    for char in my_word:
        if char not in string.whitespace:
            my_word_stripped += char
            if char not in my_word_chars and char in string.ascii_lowercase:
                my_word_chars += char
    
    # iterate over my_word_stripped looking for invalid chars
    for i in range(len(my_word_stripped)):
        # return False if a guessed letter in my_word_stripped does not match the corresponding letter of other_word
        if my_word_stripped[i] != '_' and my_word_stripped[i] != other_word[i]:
            return False
        
        # hidden letters cannot be one of the letters that has already been revealed - returns False in this case
        if my_word_stripped[i] == '_' and other_word[i] in my_word_chars:
            return False
    
    # no invalid chars found - return True
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    show_possible_matches = ''
    
    # if match_with_gaps returns True while comparing a word from wordlist with my_word, append word to show_possible_matches
    for word in wordlist:
        if match_with_gaps(my_word, word):
            show_possible_matches += word + ' '
    
    # check if show_possible_matches has found any matches to choose what to return
    if show_possible_matches == '':
        return "No matches found"
    else:
        return show_possible_matches

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    alphabet = string.ascii_lowercase
    letters_guessed = ''
    breaker = "-------------------"
    
    print("\nSecret word contains " + str(len(secret_word)) + " letters.")
    print("You have been given " + str(warnings) + " warnings. Play by the rules!")

    while guesses > 0:
        print("You have " + str(guesses) + " guesses remaining.")
        print("Available letters: " + get_available_letters(letters_guessed) + "")
        
        guess = input("Enter a letter: ").lower()
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        # check that guess is a single character
        if len(guess) != 1:
            print("Guess must be a single character!: " + guessed_word)
            print(breaker)
            continue
        
        # check if the user wants a hint
        if guess == '*':
            print("Possible word matches are: \n" + show_possible_matches(guessed_word))
            print(breaker)
            continue
        
        # check that guess is a letter of the alphabet
        if guess not in alphabet:
            if warnings != 0:
                warnings -= 1
            else:
                guesses -=1
            print("Invalid guess. " + str(warnings) + " warnings remaining: " + guessed_word)
            print(breaker)
            continue
        
        # check if the valid guess has already been guessed
        if guess in letters_guessed:
            if warnings != 0:
                warnings -= 1
            else:
                guesses -= 1
            print("Already guessed that letter! " + str(warnings) + " warnings remaining: " + guessed_word)
            print(breaker)
            continue
        
        # add new, valid guess to letters guessed and show word in progress
        letters_guessed += guess
        # update value of guessed_word with new value in letters_guessed
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        # remove a guess if it isn't in secret word
        if guess not in secret_word and guesses != 0:
            print("Not in secret word!: " + guessed_word)
            
            if guess in 'aeiou':
                guesses -= 2
            else:
                guesses -= 1
            
            print(breaker)
            continue
        elif guess in secret_word and guesses != 0:
            print("Good guess!: " + guessed_word)

        # break out of the game if user has guessed the word
        if is_word_guessed(secret_word, letters_guessed):
            print("You won!!")
            
            score = guesses * len(letters_guessed)
            print("Score: " + str(score))
            print(breaker)
            break
        
        print(breaker)
        
    # if the user didn't guess the word, let them know the game has ended
    if guesses <= 0:
        print("Secret word was " + secret_word + ", better luck next time!")

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

    # test cases for match_with_gaps
    # print(match_with_gaps("t e _ t ", "tact")) # should return False
    # print(match_with_gaps("a _ _ l e ", "banana")) # should return False
    # print(match_with_gaps("a _ p l e ", "apple")) # should return False
    # print(match_with_gaps("a _ _ l e ", "apple")) # should return True

    # test cases for show_possible_matches
    # print(show_possible_matches("t _ _ t "))
    # print(show_possible_matches("a b b b b _ "))
    # print(show_possible_matches("a _ p l _ "))
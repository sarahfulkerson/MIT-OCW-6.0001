# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou*'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

# modified SCRABBLE_LETTER_VALUES to include wildcard with a value of '0'
SCRABBLE_LETTER_VALUES = {
    '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
# (end of helper code)
# -----------------------------------
#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    
    # First component: grab the value associated with key 'char' and add it to sum_letter_points
    first_component = 0
    for char in word:
        first_component += SCRABBLE_LETTER_VALUES[char]
    
    # Second component: assign the value of 7*wordlen - 3*(n-wordlen) to second_component, then reassign to 1 if value is less than 1
    wordlen = len(word)
    second_component = 7*wordlen - 3*(n-wordlen)

    if second_component < 1:
        second_component = 1

    return first_component * second_component
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line
#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    # modified to subtract 1 from the vowel count and replace it as a wildcard
    hand={'*':1}
    num_vowels = int(math.ceil(n / 3)) - 1

    # add vowels to hand
    for i in range(num_vowels):
        x = random.choice(VOWELS[:-1]) # modified to never select the wildcard at random
        hand[x] = hand.get(x, 0) + 1
    
    # add consonants to hand
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand
#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    for char in word.lower():
        if new_hand.get(char) == None:
            continue
        elif new_hand.get(char) > 0:
            new_hand[char] -= 1
        else:
            new_hand.pop(char)

    return new_hand
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_lower = word.lower()
    word_dict = get_frequency_dict(word_lower)

    # check if word is in word_list
    if '*' not in word_lower:
        # if word_lower doesn't have a wildcard and isn't in word_list, it isn't a valid word
        if word_lower not in word_list:
            return False
    else:
        # if word_lower does have a wildcard, replace the wildcard with every vowel and try against word_list
        wildcard_pos = word_lower.find('*')
        found_word = False
        for char in VOWELS[:-1]:
            try_word = word_lower[:wildcard_pos] + char + word_lower[wildcard_pos+1:]
            if try_word in word_list:
                # change found_word to True if a word is found in word_list and break out of the loop
                found_word = True
                break
        
        # if found_word is still False, no word was found in word_list and word is not valid
        if found_word == False:
            return False
    
    # check if word can be made from letters in the hand
    for letter in word_dict:
        # if a letter in word_dict is not present in hand, then it cannot be a valid word
        if hand.get(letter) == None:
            return False
        # if there are fewer letters in the hand than there are in the word_dict, it cannot be a valid word
        if hand.get(letter) < word_dict.get(letter):
            return False

    # no issues found, return True
    return True
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    number_of_letters = 0
    for value in hand.values():
        number_of_letters += value
    
    return number_of_letters

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.    
    * The user may input a word.
    * When any word is entered (valid or invalid), it uses up letters
      from the hand.
    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    total_score = 0
    current_hand = hand.copy()
    num_of_keys = len(current_hand.keys())

    while num_of_keys > 0:
        # build a string containing all the letters in the hand
        # calculate the length of the hand
        letters = ''
        hand_len = 0
        for key in current_hand:
            letters += (key + ' ') * current_hand[key]
            hand_len += current_hand[key]
        
        # display current hand and ask for user input
        print('Current Hand: ' + letters)
        response = input('Enter word, or "!!" to indicate that you are finished: ')

        # process user input
        if response == '!!':
            print('Total score: ' + str(total_score) + ' points\n')
            break
        elif not is_valid_word(response, current_hand, word_list):
            print("That is not a valid word. Please choose another word.\n")
        else:
            score = get_word_score(response, hand_len)
            total_score += score
            print('"' + response + '" earned ' + str(score) + ' points. Total: ' + str(total_score) + ' points\n')
        
        # remove played letters from current_hand
        for char in response:
            if current_hand[char]-1 == 0:
                current_hand.pop(char)
            else:
                current_hand[char] -= 1
        
        # recalculate number of keys remaining
        num_of_keys = len(current_hand.keys())

    # if user used all letters, print final score
    if num_of_keys == 0:
        print('Ran out of letters. Total score: ' + str(total_score) + ' points')

        #break # TODO: remove after implementation
#
# Problem #6: Playing a game
# 

#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    pass  # TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    print("play_game not implemented.\n") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    # hand = {'a':1, 'j':1, 'e':1, 'f':1, '*':1, 'r':1, 'x':1}
    # hand = {'a':1, 'c':1, 'f':1, 'i':1, '*':1, 't':1, 'x':1, }
    # play_hand(hand, word_list)
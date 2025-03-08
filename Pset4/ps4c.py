# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        transpose_dict = {}

        # for every consonant, make two dictionary entries with key-value pairs lowercase->lowercase and lowercase->lowercase
        # paramenter for range() set to 21 to correspond to 21 consonants in the English alphabet (includes 'y')
        for n in range(21):
            transpose_dict[CONSONANTS_LOWER[n]] = CONSONANTS_LOWER[n]
            transpose_dict[CONSONANTS_UPPER[n]] = CONSONANTS_UPPER[n]

        # for every vowel, make two dictionary entries: one that maps lowercase vowels directly to vowels_permutation, and one that maps uppercase vowels to vowels_permutation.upper()
        # parameter for range() set to 5 to correspond to 5 vowels in the English alphabet (does not include 'y')
        for n in range(5):
            transpose_dict[VOWELS_LOWER[n]] = vowels_permutation[n]
            transpose_dict[VOWELS_UPPER[n]] = vowels_permutation[n].upper()

        return transpose_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_message_text = ''
        
        # for every character in message_text, either:
        # (1) append directly to encrypted_message_text if it isn't an alphabetic char in our transpose_dict, or
        # (2) append the transposed character to encrypted_message_text
        for char in self.get_message_text():
            val = transpose_dict.get(char)

            if val == None:
                encrypted_message_text += char
            else:
                encrypted_message_text += val

        return encrypted_message_text
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        results = []
        valid_words_list = self.get_valid_words() 
        vowel_permutations = get_permutations('aeiou')

        # For every permutation in vowel_permutations: Build a transpose_dict, apply the transpose to self.message_text using the 
        # transpose_dict, then split words out from the transposed_message_text.
        for permutation in vowel_permutations:
            valid_word_count = 0
            transpose_dict = self.build_transpose_dict(permutation)
            transposed_message_text = self.apply_transpose(transpose_dict)
            transposed_message_text_split = transposed_message_text.split()

            # for every word of our transposed message, check if it is a valid English word and +1 to valid_word_count if True
            for word in transposed_message_text_split:
                if is_word(valid_words_list, word):
                    valid_word_count += 1
                
            results.append((valid_word_count, permutation, transposed_message_text))
        
        best_result = (0,)  # initialized as singleton tuple to catch case when no valid words were found in transposed_message_text_split
        for tup in results: # iterate over every result from the previous loop - should be a tuple with format (valid_word_count, permutation, transposed_message_text)
            if tup[0] > best_result[0]: # tup[0] should give the valid_word_count of the current item in results; if greater than current value of best_result[0]...
                best_result = (tup[0], tup[1], tup[2])  # ...then replace best_result with a new tuple containing the value of permutation and the transposed message

        if best_result == (0,):
            return self.get_message_text()
        else:
            return best_result[2]

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:   ", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:  ", message.apply_transpose(enc_dict))
    print()

    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:  ", enc_message.decrypt_message())
    print()
     
    #TODO: WRITE YOUR TEST CASES HERE

    # SubMessage Test 1:
    message = SubMessage('Sarah Was Here')
    permutation = 'eioua'
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:   ", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", 'Sereh Wes Hiri')
    print("Actual encryption:  ", message.apply_transpose(enc_dict))
    print()

    # SubMessage Test 2:
    message = SubMessage('which ONE jon?')
    permutation = 'eioua'
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:   ", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", 'whoch UNI jun?')
    print("Actual encryption:  ", message.apply_transpose(enc_dict))
    print()

    # EncryptedSubMessage Test 1:
    enc_message = EncryptedSubMessage('Sereh Wes Hiri')
    print("Original message:   ", enc_message.get_message_text(), "Permutation:", permutation)
    print("Expected decryption:", 'Sarah Was Here')
    print("Decrypted message:  ", enc_message.decrypt_message())
    print()

    # EncryptedSubMessage Test 2:
    enc_message = EncryptedSubMessage('whoch UNI jun?')
    print("Original message:   ", enc_message.get_message_text(), "Permutation:", permutation)
    print("Expected decryption:", 'which ONE jon?')
    print("Decrypted message:  ", enc_message.decrypt_message())
    print()

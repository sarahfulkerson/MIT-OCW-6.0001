# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
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
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        shift_dict = {}
        
        try:
            # iterate over all lowercase characters, providing both the index and char at that index
            # add the shift value to the current index to get the char to retrieve, using modulus operator to make sure we don't over index, then add to shift_dict
            for pos, char in enumerate(string.ascii_lowercase):
                shift_dict[char] = string.ascii_lowercase[(pos + shift) % 26]
            
            # do the same for all uppercase characters
            for pos, char in enumerate(string.ascii_uppercase):
                shift_dict[char] = string.ascii_uppercase[(pos + shift) % 26]
        except TypeError:
            raise TypeError("value for 'shift' must be an int.")

        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''        
        shifted_message_text = ''
        shift_dict = self.build_shift_dict(shift) # create a shifted dictionary based on int value 'shift'

        # For every character in self.message_text, check if it is in our shift_dict (i.e. a lowercase or uppercase letter of the alphabet).
        # If val == None then it is not, so append the character to shifted_message_text.
        # Otherwise, grab the value for key 'char' and append the character to shifted_message_text.
        for char in self.get_message_text():
            val = shift_dict.get(char)
            if val == None:
                shifted_message_text += char
            else:
                shifted_message_text += val
        
        return shifted_message_text

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: EITHER a tuple of the best shift value used to decrypt the 
        message and the decrypted message text using that shift value, OR a 
        string with value 'Not able to decrypt: no valid words found.'
        '''
        results = []    # a list of tuples with format (valid_word_count, shift, shifted_message_text)
        valid_words_list = self.get_valid_words()   # the list of valid words to check against when decrypting our message

        for shift in range(26): # iterate the loop a total of 26 times (0-25), once for each letter of the alphabet (and therefore once per possible shift value)
            valid_word_count = 0    # the number of valid words we found in our decrypted message
            shifted_message_text = self.apply_shift(shift)  # our shifted message using our current position in range(26) as the value for the 'shift' parameter of apply_shift()
            shifted_message_text_split = shifted_message_text.split()   # create a list of words from our shifted_message_text string to iterate over when checking word validity
            
            for word in shifted_message_text_split: # for every word in our shifted message, test if it is a valid word. if True, increment valid_word_count.
                if is_word(valid_words_list, word):
                    valid_word_count +=1

            results.append((valid_word_count, shift, shifted_message_text)) # at the end of each loop iteration, append a tuple to 'results' with the count of valid words, shift value, and the attempt at decrypting the message

        best_result = (0,)  # initialized as singleton tuple to catch case when no valid words were found in shifted_message_text_split
        for tup in results: # iterate over every result from the previous loop - should be a tuple with format (valid_word_count, shift, shifted_message_text)
            if tup[0] > best_result[0]: # tup[0] should give the valid_word_count of the current item in results; if greater than current value of best_result[0]...
                best_result = (tup[1], tup[2])  # ...then replace best_result with a new tuple containing the value of shift and the decrypted message

        if best_result == (0,):
            best_result = 'Not able to decrypt: no valid words found.'

        return best_result  # returns either the best result from list 'results' OR string 'Not able to decrypt: no valid words found.'

if __name__ == '__main__':

    # # Example test case (PlaintextMessage)
    # plaintext = PlaintextMessage('hello', 2)
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())
    # print()

    # # Example test case (CiphertextMessage)
    # ciphertext = CiphertextMessage('jgnnq')
    # print('Expected Output:', (24, 'hello'))
    # print('Actual Output:', ciphertext.decrypt_message())
    # print()

    # TODO: WRITE YOUR TEST CASES 
    plaintext = PlaintextMessage('sarah. WAS. here', -2)
    print('Expected Output: qypyf. UYQ. fcpc')
    print('Actual Output:  ', plaintext.get_message_text_encrypted())
    print()

    plaintext = PlaintextMessage('Port Aransas', 26)
    print('Expected Output: Port Aransas')
    print('Actual Output:  ', plaintext.get_message_text_encrypted())
    print()

    ciphertext = CiphertextMessage('qypyf. UYQ. fcpc')
    print('Expected Output:', (2, 'sarah. WAS. here'))
    print('Actual Output:  ', ciphertext.decrypt_message())
    print()

    ciphertext = CiphertextMessage('Port Aransas')
    print('Expected Output:', (0, 'Port Aransas'))
    print('Actual Output:  ', ciphertext.decrypt_message())
    print()

    ciphertext = CiphertextMessage('awegf aaweg')
    print('Expected Output: Not able to decrypt: no valid words found.')
    print('Actual Output:  ', ciphertext.decrypt_message())
    print()

    # TODO: best shift value and unencrypted story 

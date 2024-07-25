'''
Encryption is the process of obscuring information to make it unreadable 
without special knowledge. For centuries, people have devised schemes to 
encrypt messages - some better than others - but the advent of the computer 
and the Internet revolutionized the field. These days, it's hard not to 
encounter some sort of encryption, whether you are buying something online or 
logging into a shared computer system. Encryption lets you share information 
with other trusted people, without fear of disclosure.

A cipher is an algorithm for performing encryption (and the reverse, 
decryption). The original information is called plaintext. After it is 
encrypted, it is called ciphertext. The ciphertext message contains all the 
information of the plaintext message, but it is not in a format readable by a 
human or computer without the proper mechanism to decrypt it; it should 
resemble random gibberish to those for whom it is not intended.

A cipher usually depends on a piece of auxiliary information, called a key. 
The key is incorporated into the encryption process; the same plaintext 
encrypted with two different keys should have two different ciphertexts. 
Without the key, it should be difficult to decrypt the resulting ciphertext 
into readable plaintext.

This assignment will deal with a well-known (though not very secure) 
encryption method called the Caesar cipher. Some vocabulary to get you started 
on this problem:
- Encryption - the process of obscuring or encoding messages to make them 
unreadable until they are decrypted
- Decryption - making encrypted messages readable again by decoding them
- Cipher - algorithm for performing encryption and decryption
- Plaintext - the original message
- Ciphertext - the encrypted message. Note: a ciphertext still contains all of 
the original message information, even if it looks like gibberish.

The Caesar Cipher

The idea of the Caesar Cipher is to pick an integer and shift every letter of 
your message by that integer. In other words, suppose the shift is k . Then, 
all instances of the i-th letter of the alphabet that appear in the plaintext 
should become the (i+k)-th letter of the alphabet in the ciphertext. You will 
need to be careful with the case in which i + k > 26 (the length of the 
alphabet). Here is what the whole alphabet looks like shifted three spots to 
the right:

Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
 3-shift:  d e f g h i j k l m n o p q r s t u v w x y z a b c
Using the above key, we can quickly translate the message "happy" to "kdssb" 
(note how the 3-shifted alphabet wraps around at the end, so x -> a, y -> b, 
and z -> c).
'''

import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
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
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
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
        #pass #delete this line and replace with your code here
        lc = string.ascii_lowercase
        uc = string.ascii_uppercase
        lc_dict = {}
        uc_dict = {}
        lc_num = 1
        uc_num = 1
        for letter in lc:
            lc_dict[letter] = lc_num
            lc_num += 1
        for letter in uc:
            uc_dict[letter] = uc_num
            uc_num += 1
        lc_dict_new = lc_dict.copy()
        uc_dict_new = uc_dict.copy()
        for key1, val1 in lc_dict_new.items():
            if val1 + shift <= 26:
                for key2, val2 in lc_dict.items():
                    if val2 == val1 + shift:
                        lc_dict_new.update({key1: key2})
                        break
            else:
                for key2, val2 in lc_dict.items():
                    if val2 == (val1 + shift) % 26:
                        lc_dict_new.update({key1: key2})
                        break
        for key1, val1 in uc_dict_new.items():
            if val1 + shift <= 26:
                for key2, val2 in uc_dict.items():
                    if val2 == val1 + shift:
                        uc_dict_new.update({key1: key2})
                        break
            else:
                for key2, val2 in uc_dict.items():
                    if val2 == (val1 + shift) % 26:
                        uc_dict_new.update({key1: key2})
                        break
        new_dict = uc_dict_new.copy()
        new_dict.update(lc_dict_new)
        return new_dict

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
        #pass #delete this line and replace with your code here
        message_text = self.get_message_text()
        shift_dict = self.build_shift_dict(shift)
        new_message_text = ""
        for letter in message_text:
            if letter in shift_dict.keys():
                new_message_text += shift_dict[letter]
            else:
                new_message_text += letter
        return new_message_text

# test
msg = Message("TESTING.... so many words we are testing out your code: last one")
print(msg.build_shift_dict(25))
print(msg.apply_shift(25))

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
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        #pass #delete this line and replace with your code here
        Message.__init__(self, text)
        self.message_text = Message.get_message_text(self)
        self.valid_words = Message.get_valid_words(self)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        #pass #delete this line and replace with your code here
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        #pass #delete this line and replace with your code here
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        #pass #delete this line and replace with your code here
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        #pass #delete this line and replace with your code here
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #pass #delete this line and replace with your code here
        Message.__init__(self, text)
        self.message_text = Message.get_message_text(self)
        self.valid_words = Message.get_valid_words(self)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #pass #delete this line and replace with your code here
        num_real_words_1 = 0
        num_real_words_2 = 0
        message = Message(self.message_text)
        for s in range(26):
            for word in message.apply_shift(s).split(" "):
                if word in self.valid_words:
                    num_real_words_1 += 1
            if num_real_words_2 < num_real_words_1:
                num_real_words_2 = num_real_words_1
                decrypted_message = message.apply_shift(s)
                best_shift = s
            num_real_words_1 = 0
        return (best_shift, decrypted_message)
    

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())


"""
Now that you have all the pieces to the puzzle, please use them to decode the 
file story.txt.
"""

def decrypt_story():
    ciphertext = CiphertextMessage(get_story_string())
    return ciphertext.decrypt_message()

print(decrypt_story())

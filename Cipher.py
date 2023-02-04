import string


# TODO: Finish the naming system and improve efficiency: LRU cache

class Cipher:
    """ For a normal cipher that maps alphabet -> a new one eg. a -> u"""

    def __init__(self, cipher_text: str):

        self.cipher_text = cipher_text

        ALPHA_LEN = 25

        l_alphabet = list(string.ascii_lowercase)
        u_alphabet = list(string.ascii_uppercase)

        self.key = {}
        self.decipher_key = {}

        for letter in range(0, ALPHA_LEN):
            self.key[l_alphabet[letter]] = cipher_text[letter].lower()
            self.key[u_alphabet[letter]] = cipher_text[letter].upper()
        self.decipher_key = {i: j for j, i in self.key.items()}

    def cipher(self, text: str, cipher: bool = True) -> str:
        """maps text given key, or reverses mapping based on cipher[bool]"""
        key = None
        # decides key to use
        match cipher:
            case True:
                key = self.key
            case False:
                key = self.decipher_key

        translated_text = ""
        for letter in text:
            # make no changes to the text if isn't in key
            if letter in key:
                translated_text += key[letter]
            else:
                translated_text += key[letter]
        return translated_text

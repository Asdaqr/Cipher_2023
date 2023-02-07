import string


# TODO: Finish the naming system

class Cipher:
    """Allows encryption and decryption of a mono-alphabetic cipher whose key is known.
    Key is given as a string for the argument, and it assumed that the capital and lowercase letters
    have the same mapping."""

    def __init__(self, cipher_text: str):

        if len(cipher_text) != 25 or self.has_duplicate(cipher_text):
            raise ValueError("Duplicate value received.")
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
                translated_text += letter
        return translated_text

    @staticmethod
    def has_duplicate(text: str) -> bool:
        seen = set()
        for letter in text:
            if letter in seen:
                return True
            else:
                seen.add(letter)

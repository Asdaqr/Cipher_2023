import string
from typing import Optional
from functools import cache


# TODO: finish auto-cipher & cipher
class CaesarCipher:
    """Encrypts and decrypts caesar ciphers. Allows for auto-decrypting.
    For more information see https://www.sciencedirect.com/topics/computer-science/caesar-cipher"""
    def __init__(self, shift: Optional[int] = None):
        self.key = None
        if shift is not None:
            self.key = shift
        else:
            self.auto_decipher(self.get_text())

    @staticmethod
    def get_text() -> str:
        text = input("Enter text to decipher")
        return text

    def auto_decipher(self, text: str) -> bool:
        key = None
        guess = None
        for i in range(1, 26):
            # self.cipher(text, i, False)
            pass

        while True:
            # while loop asks user if the guess is correct
            is_correct = input(f"Deciphered Text: \n {guess} \n Does this look correct?(y/n): ")
            match is_correct:
                case 'y':
                    self.key = key
                    return True
                case 'n':
                    print("Sorry, we couldn't decipher it.")
                    return False
                case _:
                    print("Unrecognized value. Please enter y/n")

    @cache
    def common_words(self) -> set:
        common_words = set()
        with open('common-words.txt', 'r') as f:
            for line in f:
                common_words.add(line.strip())
        return common_words

    def cipher(self, key: int = None, cipher: bool = True):
        if key is None:
            key = self.key

        match cipher:
            case True:
                pass
            case False:
                pass

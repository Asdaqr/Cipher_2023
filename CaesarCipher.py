import string
from typing import Optional
from functools import cache


# TODO
class CaesarCipher:
    def __init__(self, shift: Optional[int] = None):
        self.key = None
        if shift is not None:
            self.key = shift
        else:
            self.autodecipher(self.get_text())

    @staticmethod
    def get_text() -> str:
        text = input("Enter text to decipher")
        return text

    def autodecipher(self, text: str) -> bool:
        key = None
        for i in range(1, 26):
            # self.cipher(text, i, False)
            pass

        while True:
            isCorrect = input(f"Deciphered Text: \n {text} \n Does this look correct?(y/n): ")
            match isCorrect:
                case 'y':
                    self.key = key
                    return True
                case 'n':
                    print("Sorry, we couldn't decipher it.")
                    return False
                case _:
                    print("Unrecognized value")

    @cache
    def common_words(self) -> set:
        #TODO: code common words func
        common_words = {}
        with open('common-words.txt', 'r') as f:
            pass

        return common_words

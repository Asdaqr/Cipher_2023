from typing import Optional
from functools import cache
from os import path


class CaesarCipher:
    """Encrypts and decrypts caesar ciphers. Allows for auto-decrypting.
    For more information see https://www.sciencedirect.com/topics/computer-science/caesar-cipher"""

    def __init__(self, shift: Optional[int] = None):
        self.text = None
        self.key = None
        self.words_list = self.common_words()
        if shift is not None:
            self.key = shift
        else:
            self.auto_decipher(self.get_text())

    @staticmethod
    def get_text() -> str:
        text = input("Enter text to decipher: ")
        return text

    @staticmethod
    def map_char(char: str, shift: int):
        if char.isalpha():
            if char.isupper():
                offset = 65
            else:
                offset = 97
            ascii_val = ord(char) + shift
            if ascii_val < offset:
                ascii_val += 26
            elif ascii_val > offset + 25:
                ascii_val -= 26
            translated_char = chr(ascii_val)
            return translated_char

        else:
            return char

    @cache
    def common_words(self) -> set:
        common_words = set()
        location = path.dirname(__file__) + "\\common-words.txt"
        with open(location, 'r') as f:
            for line in f:
                common_words.add(line.strip())
        return common_words

    def auto_decipher(self, text: str) -> bool:
        self.text = text
        max_words = 0
        key = 0
        for i in range(1, 26):
            word_count = 0
            possible_solution = self.cipher(i, False)
            solution_list = possible_solution.strip(".").split()
            for word in solution_list:
                if word in self.words_list:
                    word_count += 1
            if word_count > max_words:
                key = i
                max_words = word_count
        guess = self.cipher(key, False)

        while True:
            # while loop asks user if the guess is correct
            is_correct = input(f"Deciphered Text: \n {guess} \n Does this look correct?(y/n): ")[0]
            match is_correct.lower():
                case 'y':
                    self.key = key

                    return True
                case 'n':
                    print("Sorry, we couldn't decipher it.")
                    return False
                case _:
                    print("Unrecognized value. Please enter y/n")

    def cipher(self, key: int = None, cipher: bool = True) -> str:
        shift = None
        if key is None:
            key = self.key

        match cipher:
            case True:
                shift = key
            case False:
                shift = -1 * key

        translated_text = ''
        for letter in self.text:
            translated_text += self.map_char(letter, shift)

        return translated_text

    def get_curr_text(self):
        return self.text

    def get_key(self):
        return self.key

from Cipherlib import CaesarCipher


def get_mode():
    while True:
        input_mode = input("Are you ciphering or deciphering text: (cipher/decipher): ").strip().lower()

        match input_mode:
            case "cipher":
                return "cipher"
            case "decipher":
                return "decipher"
            case _:
                print("Please enter either cipher or decipher")


def get_key() -> int:
    key = None
    while True:
        try:
            key = int(input("Please enter the key"))
        except ValueError:
            print("please enter a integer value:")
            continue
        break
    return key


if __name__ == "__main__":
    print("Welcome!")
    mode = get_mode()
    NewCipher = None
    shift = None
    match mode:
        case "cipher":
            shift = get_key()
            NewCipher = CaesarCipher.CaesarCipher(shift)
        case "decipher":
            has_key = input("Do you have the key?(y/n)").lower().strip()[0]
            match has_key:
                case "y":
                    shift = get_key()
                    NewCipher = CaesarCipher.CaesarCipher(shift)
                case "n":
                    NewCipher = CaesarCipher.CaesarCipher()
        case _:
            raise Exception("Unreachable code has occurred.")

    print(f"New text is \n{NewCipher.get_curr_text()}")

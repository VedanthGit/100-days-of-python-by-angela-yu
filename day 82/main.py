MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "/",
}


def text_to_morse(text):
    text = text.upper()
    morse_output = []

    for char in text:
        if char in MORSE_CODE_DICT:
            morse_output.append(MORSE_CODE_DICT[char])
        else:
            morse_output.append("?")

    return " ".join(morse_output)


def main():

    while True:

        text = input("Enter text: ")
        print("Morse Code:", text_to_morse(text))
        break


if __name__ == "__main__":
    main()

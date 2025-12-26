# Ceaser Cipher Text
def caesor(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabets:
            output_text += letter
        else:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
    print(f"here is the {encode_or_decode}d text: {output_text}")
    
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n").lower()
    message = input("Write the message you want to send: \n")
    shift = int(input("Type the shift number: \n"))

    caesor(message, shift, direction)
    
    restart = input("Type 'Yes' if you want to continue else  type 'No': ").lower()
    if restart == "no":
        should_continue = False
        print("GOODBYE")
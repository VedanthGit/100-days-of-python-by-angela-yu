import os
PLACEHOLDER = "[name]"

BASE_DIR = os.path.dirname(__file__)
names_path = os.path.join(BASE_DIR, "Input", "Names", "invited_names.txt")
letter_path = os.path.join(BASE_DIR, "Input", "Letters", "starting_letter.txt")
output_path = os.path.join(BASE_DIR, "Output", "ReadyToSend")

with open(names_path) as names_files:
    names = names_files.readlines()
    
    
with open(letter_path) as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"{output_path}/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
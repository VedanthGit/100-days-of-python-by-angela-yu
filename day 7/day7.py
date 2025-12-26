# HANGMAN PROJECT

# STEP 1 - Picking random word and guessing a letter in the word
# STEP 2 - Replaceing Blanks with Guesses
# STEP 3 - Checking if the player has won
import random

stages = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

lives = 6

word_list = ["aardvark","baboon","camel","hypnosis","baguette","pterodactyl","fjord","chandelier","pharaoh","kaleidoscope",
"apothecary","eccentric","chimera","photosynthesis","hologram","atmosphere","nephilim","millennium","centrifugal","phonograph","semaphore","bioluminescence","circumference","electromagnetism","archaeology","fibonacci"
]

choosen_word = random.choice(word_list)
print(choosen_word)

placeholder = ""
for position in range(len(choosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letters = []
guessed_letters = []
while not game_over:

    print(f"***********{lives}/6***********")
    
    guess = input("Select a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    print(f"Letters tried: {guessed_letters}")
        
    if guess in choosen_word:
        correct_letters.append(guess)
    else:
        lives -= 1
        print("Wrong letter! You lose a life.")
        if lives == 0:
            print("Hangman Just Got Vanished!!! You Lose!!")
            game_over = True
    
    display = ""

    for letter in choosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
            
    print(display)

    if "_" not in display:
        print("You Win!!! 🏆")
        game_over = True
    
    print(stages[lives])
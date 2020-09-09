import random

lives=9
words =['write','big','help','axe','pumpkin']
secret_word=random.choice(words)
clue = []
index =0
heart =u'\u2764'
guessed_word_correctly=False
while index < len(secret_word):
    clue.append('?')
    index= index+1

def update_clue(guessed_letter,secret_word,clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter

        index = index + 1

while lives > 0:
    print(clue)
    if clue == list(secret_word):
        guessed_word_correctly = True
        break
    print("your lives: "+heart * lives)
    guess = input("Enter a letter or whole word: ")

    if guess in secret_word:
        print("letter found..")
        update_clue(guess,secret_word,clue)
    else:
        print("incorrect guess. you lose a life")
        lives = lives -1

if guessed_word_correctly:
    print("you win.The secret word is [%s]"%secret_word)
else:
    print("you lose.The secret word is [%s]"%secret_word)


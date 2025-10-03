##################################################################################
#
# Project 3
#
#
#
#
#
#
#
#################################################################################


# Use these strings in your code. Remove these strings when done
"\n:~Enter a word or phrase ~:"
from operator import truediv

"Error: only letters are allowed as input."
"phrase: {}"
"current: {}"
"♥"
"lives left: {}"
"guesses: {}"
"\n:~Guess a letter or whole word/phrase ~:"
"Only letters and spaces are allowed as input.\n"
"Wrong guess of whole word or phrase."
"Already guessed {}"
"Letter not in phrase.\n"
"\n♥ Congratulations! You saved all your hearts ♥"
"\nGAME OVER. No hearts left!\n The word/phrase was: {}"



# Constants that holds the banner and the rules
banner = """
===================================
    ♥  WORD GUESS GAME ♥       
        HANGMAN EDITION          
===================================
"""

rules = """Hangman: guess letters until you can guess the whole word or phrase."
\tRULES:
\t\t1. You have 6 hearts ♥.
\t\t2. Guess one LETTER at a time, or try the full answer.
\t\t3. Correct letters will be revealed in the word.
\t\t4. Wrong guesses cost you a heart.
\t\t5. Spaces are shown automatically.
\t\t6. Win by guessing all letters before hearts run out!
"""
lives="♥♥♥♥♥♥"
print(banner)
print(rules)

while True:
    answ = input("\n:~Enter a word or phrase ~:")
    for char in answ:
        if char.isalpha() or char.isspace():
            valid_str=True
            continue

        else:
            print("Error: only letters are allowed as input.")
            valid_str=False
            break

    if valid_str==False:
        continue
    else:
        print("phrase:", answ)
        break
answ2=""
while True:
    for char in answ:
        if char.isalpha():
            answ2=answ2+"-"
            continue
        else:
            answ2=answ2+" "
            continue
    break
answ_origin=answ
answ=answ.lower()
position=0
hearts = 6
guesses=""
dummy = answ2
print("current:", answ2)
while True:

    if hearts == 0:
        print("\nGAME OVER. No hearts left!\n The word/phrase was:", answ_origin)
        break
    print("lives left:", lives)
    print("guesses:", guesses)
    guess=input("\n:~Guess a letter or whole word/phrase ~:").lower()
    if hearts == 6 and answ2 == dummy and guess.isdigit():
        dummy = 0
        print("Only letters and spaces are allowed as input.\n")
        continue
    if guess.isdigit():
        print("Only letters and spaces are allowed as input.\n")
        print("current:", answ2)
        continue
    if guess in guesses:
        print("Already guessed", guess)
        continue
    guesses=guesses+guess
    valid_str2=False
    if len(guess)==1:
        for char in answ:
            if char != guess:
                position+=1
            elif char == guess:
                answ2 = answ2[0:position] + answ_origin[position] + answ2[position + 1:]
                position += 1
                valid_str2=True

        position=0
        if valid_str2!=True:
            hearts=hearts-1
            lives = lives[0:hearts]
            print("Letter not in phrase.\n")
        if answ2==answ:
            print("current:", answ_origin)
            print("\n♥ Congratulations! You saved all your hearts ♥")
            break

    else:
        if guess == answ:
            print("\n♥ Congratulations! You saved all your hearts ♥")
            break
    print("current:", answ2)




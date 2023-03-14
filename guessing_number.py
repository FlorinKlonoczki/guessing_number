#  Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!
import random

numar_secret = random.randint(1, 30)
while True:
    numar_ghicit = int(input('Guess the secret number (hint: between 1 and 30): '))
    if numar_ghicit < numar_secret:
        print('The secret number is higher!')
    elif numar_ghicit > numar_secret:
        print('The secret number is lower!')
    else:
        print('Congratulation! You guessed it!')
        break

user_word = input("Ingresa tu palabra: ")
user_word = user_word.upper()

#continue avanza al siguiente codigo de bloque
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)

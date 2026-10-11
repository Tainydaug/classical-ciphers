import random

word = input("Enter the plaintext: ")
word = word.upper()

keygen = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = ""
for i in range(len(word)):
    key = key + keygen[random.randint(0,25)]
print("the key is: ", key)

cipher = ""
for i in range(len(word)):
    ci = ((ord(word[i]) - 65) + (ord(key[i]) - 65)) % 26
    cipher = cipher + chr(ci + 65)
print("the ciphertext is: ", cipher)

plain = ""
for i in range(len(word)):
    pl = ((ord(cipher[i]) - 65) - (ord(key[i]) - 65)) % 26
    plain = plain + chr(pl + 65)
print("the plaintext was: ", plain.lower())                                                                                                               

arrp = []
arrk = []
arri = []
arrd = []
count = []
plain = input("Enter the plain text: ")
key = input("Enter the key: ")
plain = plain.upper()
key = key.upper()
for i in range(len(plain)):
    if plain[i] == " ":
        count.append(i) 
plain = plain.replace(" ", "")        
for i in range(len(plain)):
    arrp.append(ord(plain[i]) - 65)

for i in range(len(key)):
    arrk.append(ord(key[i]) - 65)
j = 0
k = 0
while True:
    if j == len(plain):
        break
    if k == len(key):
        k = 0    
    arri.append((arrp[j] + arrk[k]) % 26)
    j += 1
    k += 1
cipher = ""
for i in range(len(arri)):
    cipher += chr(arri[i] + 65)
print("Cipher text is: ", cipher)
j = 0
k = 0
while True:
    if j == len(cipher):
        break
    if k == len(key):
        k = 0
    arrd.append(arri[j] - arrk[k] % 26)
    j += 1
    k += 1    
plain = ""
c = 0
for i in range(len(arrd)):
    if c < len(count) and count[c] == len(plain):
        plain += " "
        c += 1
    if arrd[i] < 0:
        arrd[i] += 26
    plain += chr(arrd[i] + 65)
print("Plain text is: ", plain.lower())    
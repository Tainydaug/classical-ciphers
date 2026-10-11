arr = []
oth = []
j = 0
alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
count = 0
key = input("Enter the key: ")
key = key.upper()
for i in range(len(key)):
    if key[i] not in arr:
        arr.append(key[i])
for i in range(len(alpha)):
    if alpha[i] not in arr:
        oth.append(alpha[i])
for i in range(25):
    if count % 5 == 0 and count != 0:
        print()
    if count < len(arr):
        print(arr[i], end = " ")
    else:
        print(oth[j], end = " ")
        j += 1
    count += 1
print()    
word = input("Enter the word: ")
word = word.upper()
pair = []
i = 0
while i < len(word):
    if i + 1 < len(word):
        if word[i] == word[i + 1]:
            if word[i] == "X":
                pair.append(word[i] + "Q")
            else:
                pair.append(word[i] + "X")
            i += 1         
        else:
            pair.append(word[i] + word[i + 1])
            i += 2        
    else:
        if "X" in word:
            pair.append(word[i] + "Q")
        else:
            pair.append(word[i] + "X")
        i += 1        
print(pair)
al = []
all = [0,]
al.append(arr+oth)
for i in al:
    for j in i: 
        all.append(j)      
lett = []
for i in pair:
    for j in i:
        lett.append(j)
print(lett)  
print(all) 
mat = 0 
cipher = ""      
for i in range(0, len(lett),2):
    for j in range(len(all)):
        if i + 1 < len(lett):
            if lett[i] in all:
                mat = all.index(lett[i])   
                if lett[i+1] in all:
                    if (mat - 1) // 5 == (all.index(lett[i+1]) - 1) // 5:
                        if (mat - 1) % 5 == 4:
                            cipher = cipher + all[mat - 4]
                        else:
                            cipher = cipher + all[mat + 1]
                        mat = all.index(lett[i+1])
                        if (mat - 1) % 5 == 4:
                            cipher = cipher + all[mat - 4]
                        else:
                            cipher = cipher + all[mat + 1]
                        break
                    elif (mat - 1) % 5 == (all.index(lett[i+1]) - 1) % 5:
                        if (mat - 1) // 5 == 4:
                            cipher = cipher + all[mat - 20]
                        else:
                            cipher = cipher + all[mat + 5]
                        mat = all.index(lett[i+1])
                        if (mat - 1) // 5 == 4:
                            cipher = cipher + all[mat - 20]
                        else:
                            cipher = cipher + all[mat + 5]
                        break   
                    else:
                        mat2 = int(all.index(lett[i+1]))
                        cipher = cipher + all[((mat-1)//5)*5 + ((mat2-1)%5) + 1]  
                        cipher = cipher + all[((mat2-1)//5)*5 + ((mat-1)%5) + 1]
                        break                                      
print("the cipher text is:", cipher)
mat = 0 
plain = ""
for i in range(0, len(cipher), 2):
    for j in range(len(all)):
        if i + 1 < len(cipher):
            if cipher[i] in all:
                mat = all.index(cipher[i])   
                if cipher[i+1] in all:
                    if (mat - 1) // 5 == (all.index(cipher[i+1]) - 1) // 5:
                        if (mat - 1) % 5 == 0:
                            plain = plain + all[mat + 4]
                        else:
                            plain = plain + all[mat - 1]
                        mat = all.index(cipher[i+1])
                        if (mat - 1) % 5 == 0:
                            plain = plain + all[mat + 4]
                        else:
                            plain = plain + all[mat - 1]
                        break
                    elif (mat - 1) % 5 == (all.index(cipher[i+1]) - 1) % 5:
                        if (mat - 1) // 5 == 0:
                            plain = plain + all[mat + 20]
                        else:
                            plain = plain + all[mat - 5]
                        mat = all.index(cipher[i+1])
                        if (mat - 1) // 5 == 0:
                            plain = plain + all[mat + 20]
                        else:
                            plain = plain + all[mat - 5]
                        break   
                    else:
                        mat2 = int(all.index(cipher[i+1]))
                        plain = plain + all[((mat-1)//5)*5 + ((mat2-1)%5) + 1]  
                        plain = plain + all[((mat2-1)//5)*5 + ((mat-1)%5) + 1]
                        break                                      
print("the plain text is:", plain)                  
clean = ""
i = 0
while i < len(plain):
    if i + 2 < len(plain):
        if plain[i] == plain[i+2] and (plain[i+1] == "X" or plain[i+1] == "Q"):
            clean = clean + plain[i]
            i += 2
        else:
            clean = clean + plain[i]
            i += 1
    else:
        clean = clean + plain[i]
        i += 1
print("cleaned plaintext:", clean)   
                 
                                          

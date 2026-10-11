p = input("Enter a character: ")
p = p.upper()
c = ord(p)
x = (c - 65 + 1) % 26
x = x + 65      
print("The converted character is:", chr(x),"its ASCII value is:",x) 
z = (x - 65 - 1) % 26
z = z + 65
z = chr(z)
z = z.lower()
print("The original character is:",z)      
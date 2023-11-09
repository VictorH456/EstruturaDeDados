from collections import deque

frase1 = deque()
texto1 = "Arara".lower()
frase2 = deque()

for i in texto1:
    frase1.append(i)

#cria uma copia da frase1
frase_temporaria = frase1.copy() 

while frase_temporaria:
    frase2.append(frase_temporaria.pop())

for i in range(len(frase2)):
    if frase1[i] != frase2[i]:
        print(f"{texto1} não é um palindromo")
        exit()

print(f"{texto1} é um palindromo")
#Numeros Primos

listaPrimos = []
listaNaoPrimos = []

j = 0
k = 0

tamanhoLista = int(input("Until which number must I search for the primes? "))

for j in range (1, tamanhoLista+1):
    
    contador = 0
    
    for k in range (1, tamanhoLista):
        
        if j == k or j < k or k == 1 or j == 1:
            continue
        
        resto = j%k
        
        #print("remainder of %d divided by %d = %d" % (j, k, resto))

        if resto == 0:
            contador += 1
                
    if contador == 0 and j != 1:
        listaPrimos.append(j)
                   
    elif contador >= 1:
        listaNaoPrimos.append(j)

        


print("List of prime numbers until %d = " % (tamanhoLista), listaPrimos)
print("List of non-prime numbers until %d = " % (tamanhoLista), listaNaoPrimos)

#Prime numbers until 100:

#2 3 5 7 11 13 17 19 23 29
#31 37 41 43 47 53 59 61 67 71
#73 79 83 89 97 

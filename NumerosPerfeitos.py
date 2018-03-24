#Numeros Perfeitos

listaPerfeitos = []
listaNaoPerfeitos = []
listaDivisoresN = []

tamanhoLista = int(input("Ate que numero devo procurar os perfeitos? "))

for a in range (1, tamanhoLista+1):

    contador = 0
    listaDivisoresN[:] = []

    for b in range (1, tamanhoLista+1):

        if a < b or a == b or b > (a/2):
            continue

        resto = a%b
        
        #print("resto de %d por %d = %d" % (a, b, resto))

        if resto == 0:
            
            contador += 1
            listaDivisoresN.append(b)

        if contador > 0 and b == (a/2):

            temporario = sum(listaDivisoresN)
            
            if temporario == a:
                
                listaPerfeitos.append(a)
                
            else:

                listaNaoPerfeitos.append(a)
                
print("Lista dos numeros perfeitos ate %d =" % (tamanhoLista), listaPerfeitos)
print("Lista dos numeros nao perfeitos ate %d =" % (tamanhoLista), listaNaoPerfeitos)
        
'''
Dez menores
6
28
496 
8.128 
33.550.336
8.589.869.056
137.438.691.328
2.305.843.008.139.952.128
2.658.455.991.569.831.744.645.692.615.953.842.176
191.561.942.608.236.107.294.793.378.084.303.638.130.997.321.548.169.216
'''

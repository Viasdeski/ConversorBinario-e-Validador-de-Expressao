from classes import Binario

bin = Binario()

binario = []

numero = int(input("Qual número deseja converter para binário: "))

bin.dec2bin(numero)

while len(bin) > 0:
    binario.append(bin.pop())

binario = ''.join(map(str, binario))
       
print(f'O número {numero} em binário equivale a: {binario}')










            

            
            
        
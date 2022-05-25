
''' crie um programa onde o usuário possa digitar cinco valores numéricos 
e cadastre-os em uma lista, ja na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela. '''

lista = []
for v in range(0, 5):   
    n = int(input("Digite um número: "))
    if v == 0  or n > lista[-1]:
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.append(posicao, n)
                break
            posicao += 1
   
            
                
print("=" *30)
print(f'Os números digitados em ordem foram: {lista}')
    



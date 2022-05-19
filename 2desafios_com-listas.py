

''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista,
 caso  o número ja exista la dentro, ele não será adicionado. No final serão exibidos todos os valores únicos 
 digitados, em uma ordem crescente. '''


valor = list()
while True:
    v = int(input("Digite um número: "))
    if v not in valor:
        valor.append(v)
        print('Valor adicionado com sucesso.')
    else:
        print('Esse número não pode ser adicionado, por favor digite um valor diferente')
        
    r = str(input("Deseja digitar um outro valor? [S/N]: "))
    if r in 'Nn':
        break
    
valor.sort()

print(f"Você digitou os valores: {valor}")

    



''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final mostre qual foi o maior e o menor  valor digitado e suas respectivas posições na lista.'''





listvalor = []
men = 0
mai = 0
for c in range(0, 5):
    listvalor.append(int(input(f'Digite cinco valores {c}º : ')))
    if c == 0:
        mai = men = listvalor[c]
    else:
        if listvalor[c]>mai:
            mai = listvalor[c]
        if listvalor[c]<men:
            men = listvalor[c]


print('=-' *30)
print(listvalor)

print(f'O maior valor da lista é: {max(listvalor)} na posição ', end="")
for i, v in enumerate(listvalor):
    if v == mai:
        print(f'{i}...', end="")
print()
print(f'O menor valor da lista é: {min(listvalor)} na posição ', end="")
for i, v in enumerate(listvalor):
    if v == men:
        print(f'{i}...', end="")
print()
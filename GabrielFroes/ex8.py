
notas = []

for i in range(4):
    nota = float(input(f"Digite as 4 notas do aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

if (media >= 7) :
    print("Aprovado!!")
elif(media < 7) :
    nota = float(input(f"Digite a nota da prova final do aluno: "))
    notas.append(nota)
    media = sum(notas) / len(notas)
    if(media >= 5):
        print("Aprovado!!")
    else:
        print("Reprovado!!")










    
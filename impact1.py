lista = input("Digite as notas separadas por espaço: ").split()
notas = [float(x) for x in lista] 

qtd = len(notas)
media = sum(notas) / qtd

notas_ordenadas = sorted(notas)
mediana = 0 
if qtd // 2 == 1:
    mediana = notas_ordenadas[qtd // 2]

else:
    mediana = (notas_ordenadas[(qtd // 2) - 1] + notas_ordenadas[qtd // 2])/2

soma_quadrados = 0
for nota in notas:
    soma_quadrados += (nota - media) ** 2

variancia = soma_quadrados / qtd
desvp = variancia ** 0.5

print(f"\nMédia: {media:.2f} | Mediana: {mediana:.2f} | Desvio padrão: {desvp:.2f}\n")

for nota in notas:
    if nota >= 6: 
        status = "Aprovado"
    elif nota >= 5:
        status = "Recuperação"
    else:
        status = "Reprovado"
    print(f"Nota {nota}: {status}")
"""
Exercicio 1

1. Faça um programa que exiba seu nome na tela.
"""

print("Meu nome é Juliana Sandes")


"""
Exercicio 2

2. Escreva um programa que exiba o resultado de 2a x
3b, em que a vale 3 e b vale 5.
"""
a = 3
b = 5
print(2*a * 3*b)



"""
Exercicio 3

3. Escreva um programa que calcule a soma de três
variáveis e imprima o resultado na tela.
"""

a = 25
b = 60
c = 2000

resultado = a + b + c
print("O resultado é:", resultado)


"""
Exercicio 4

4. Faça um programa que peça dois números inteiros.
Imprima a soma desses dois números na tela.

"""

valorA= int(input("Informe um número:"))
valorB = int(input("Informe um segundo número:"))


resultado = valorA + valorB

print("A soma é", resultado)


"""
Exercicio 5

5. Escreva um programa que leia um valor em metros e
o exiba convertido em milímetros.


"""

valorA= int(input("Informe um valor em metros, para transformar em milímetros:"))

resultado = valorA * 1000

print("O resultado é", resultado, "mm")


"""
Exercicio 6

6. Escreva um programa que leia a quantidade de dias,
horas, minutos e segundos do usuário. Calcule o total
em segundos.
"""

dias = int(input("Coloque sua quantidade de dias:"))
horas = int(input("Coloque sua quantidade de horas:"))
minutos = int(input("Coloque sua quantidade de minutos:"))
segundos = int(input("Coloque sua quantidade de segundos:"))

resultado = dias * 86400 + horas * 3600 + minutos * 60 + segundos

print("O resultado em segundos é", resultado, "segundos")

"""
Exercicio 7

7. Faça um programa que calcule o aumento de um
salário. Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e
do novo salário. 
"""

salarioAtual = float(input("Coloque o valor atual do seu salário:"))
porcentagemAumento = int(input("Coloque sua porcentagem de aumento:"))

valorAumento = salarioAtual * (porcentagemAumento/100)
novoSalario = salarioAtual + valorAumento 

print("O valor de aumento é de R$%.2f." %valorAumento)
print("O valor de aumento do salário é de R$%.2f." %novoSalario)

"""
Exercicio 8

8. Faça um programa que solicite o preço de uma
mercadoria e o percentual de desconto. Exiba o valor do
desconto e o preço a pagar. 
"""

precoMercadoria = float(input("Coloque o preço atual da mercadoria:"))
desconto = int(input("Coloque o valor da porcentagem de desconto:"))

desconto = precoMercadoria * (desconto/100)
novoPreco = precoMercadoria - desconto

print("O valor do desconto é de R$%.2f." %desconto)
print("O valor da mercadoria é de R$%.2f." %novoPreco)

"""
Exercicio 9

9. Escreva um programa que calcule o tempo de uma
viagem de carro. Pergunte a distância a percorrer e a
velocidade média esperada para a viagem.

"""

distancia = int(input("Coloque a distancia percorrida:"))
velocidade = int(input("Coloque o valor da velocidade média:"))

tempo = distancia / velocidade

print("O valor do tempo médio é de %.2f horas." %tempo)

"""
Exercicio 10

10. Escreva um programa que converta uma
temperatura digitada em ºC para ºF. A fórmula para essa
conversão é F = ((9 x C) / 5) + 32
"""

celsius = int(input("Entre com a temperatura em °C: "))

fahrenheit = ((9 * celsius) / 5 ) + 32

print(f"{celsius} °C = {fahrenheit} °F")


"""
Exercicio 11

11. Escreva um programa que pergunte a quantidade de
km percorridos por um carro alugado pelo usuário, assim
como a quantidade de dias pelos quais o carro foi
alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por km rodado.
"""

km = int(input("Coloque a quantidade de km percorrido:"))
dias = int(input("Coloque a quantidade de dias:"))

resultado = (km * 0.15) + (dias * 60)

print("O preço a pagar é de R$%.2f." %resultado)

"""
Exercicio 12

12. Escreva um programa que receba 2 valores do tipo
inteiro x e y, e calcule o valor de z:
z = (x2 + y2) / (x – y)2

"""
x = int(input("x = "))
y = int(input("y = "))

z = (x**2 + y**2) / (x - y)**2

print("z =",z)

"""
Exercicio 13

13. Escreva um programa que receba o salário de um
funcionário (float) e retorne o resultado do novo salário
com reajuste de 35%.
"""

salario = float(input("Digite o valor do salário: R$"))
print("O valor do novo salário é de R$%.2f"%(salario * 1.35)+".")















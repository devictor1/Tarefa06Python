# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor.

valor1 = int(input("Insira aqui o primeiro valor inteiro"))
valor2 = int(input("Agora, insira o segundo valor inteiro."))
print("A diferença do maior pelo menor é", valor1 - valor2) if valor1>valor2 else print("A diferença do maior pelo menor é",valor2 - valor1)
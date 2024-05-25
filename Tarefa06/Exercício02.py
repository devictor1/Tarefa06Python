# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar o número
# lido como sendo um valor positivo, ou seja, o programa deverá apresentar o módulo
# de um número fornecido. Lembre-se de verificar se o número fornecido é menor que zero;
# sendo, multiplique-o por -1.

valor1 = int(input("Insira aqui um valor inteiro"))
print("O valor em módulo é", valor1 * -1) if valor1<0 else print("O valor é", valor1)
# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Efetuar a leitura de três valores (variáveis A, B e C) e apresentá-los dispostos em ordem crescente.

a = float(input("Insira o primeiro valor ao lado"))
b = float(input("Agora, insira o terceiro"))
c = float(input("Por último, insira o terceiro valor"))

if a > b or a > c:
    if a > b and b > c:
        print("Os valores em ordem crescente são:", a, b, c)
    elif a > c and c > b:
        print("Os valores em ordem crescente são:", a, c, b)
elif b > a or b > c:
    if b > a and a > c:
        print("Os valores em ordem crescente são:", b, a, c)
    elif b > c and c > a:
        print("Os valores em ordem crescente são:", b, c, a)
elif c > a:
    if c > a and a > b:
        print("Os valores em ordem crescente são:", c, a, b)
    elif c > b and b > a:
        print("Os valores em ordem crescente são:", c, b, a)
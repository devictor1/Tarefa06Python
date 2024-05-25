# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma
# mensagem dizendo que o aluno foi aprovado, se o valor da média escolar for maior
# ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem informando esta
# condição. Apresentar junto das mensagens o valor da média do aluno para qualquer condição.

nota1 = float(input("Qual foi sua primeira nota?"))
nota2 = float(input("E qual a sua da segunda nota?"))
nota3 = float(input("E como você foi na terceira avalização?"))
nota4 = float(input("Por último, qual sua quarta nota?"))
media = (nota1+nota2+nota3+nota4)/4
print("Parabéns! Você passou com uma média de",media) if media >= 5 else print("Infelizmente você não passou com a média de",media)
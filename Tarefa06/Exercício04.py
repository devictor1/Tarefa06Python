# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem dizendo que
# o aluno foi aprovado, se o valor da média escolar for maior ou igual a 7. Se o valor da média for menor
# que 7, solicitar a nota de exame, somar com o valor da média e obter nova média. Se a nova média for maior
# ou igual a 5, apresentar uma mensagem dizendo que o aluno foi aprovado em exame. Se o aluno não foi aprovado,
# indicar uma mensagem informando esta condição. Apresentar com as mensagens o valor da média do aluno, para
# qualquer condição.

nota1 = float(input("Qual foi sua primeira nota?"))
nota2 = float(input("E qual a sua da segunda nota?"))
nota3 = float(input("E como você foi na terceira avalização?"))
nota4 = float(input("Por último, qual sua quarta nota?"))
media = (nota1+nota2+nota3+nota4)/4
if media >= 7:
    print("Parabéns! Você passou com a média de",media)
else:
    notaExame = float(input("E qual a sua nota de exame?"))
    novaMedia = (media+notaExame)/2
    if novaMedia >5:
        print("Parabéns! Você passou com a média de", novaMedia)
    else:
        print("Infelizmente você não passou com a média de",novaMedia)
        
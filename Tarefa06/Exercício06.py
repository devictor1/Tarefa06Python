# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Elaborar um programa que efetue a leitura do nome e do sexo de uma pessoa, apresentando com saída
# uma das seguintes mensagens: "Ilmo Sr.", se o sexo informado como masculino, ou a mensagem "Ilma Sra.",
# para o sexo informado como feminino. Apresente também junto da mensagem de saudação o nome
# previamente informado.

nome = input("Escreva o seu primeiro nome!")
sexo = int(input("E qual o seu sexo? Use 1 para masculino e 2 para feminino"))
print("Ilmo Sr.", nome, ", seja bem-vindo às nossas instalações") if sexo == 1 else print("Ilma Sra,", nome, ", seja bem-vinda às nossas instalações")

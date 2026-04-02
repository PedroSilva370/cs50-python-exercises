while True:
    try:
        # ENTRADA
        # peça um numero inteiro e positivo de 1 a 8
        quantidade = int(input('Digite um número de 1 a 8: '))

        # PROCESSAMENTO
        # se não for um numero inteiro não superior a 8, peça novamente
        if 1 <= quantidade <= 8:
            break
    except ValueError:
        pass

# gerar a piramide
for i in range(1, quantidade + 1):
    spaces = quantidade - i
    hashes = i

# SAÍDA
# mostrar a piramede gerada
    print(" " * spaces + "#" * hashes)
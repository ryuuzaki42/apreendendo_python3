
def fatorial(n):
    # Funcao que calcula o fatorial de um número inteiro
    # Exemplo: x = fatorial(5)
    """
    Docstring exemplo, acessado pelo .__doc__ ou help()
    Funcao que calcula o fatorial de um numero inteiro
    Exemplo: x = fatorial(5)
    """
    if (n <= 1) :
        return 1
    else :
        return n * fatorial(n -1)

print(fatorial.__doc__)

help(fatorial)

x = int(input("Digite um valor: "))
result = fatorial(x)
print("O fatorial de", x, "é:", result)

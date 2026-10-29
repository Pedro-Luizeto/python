#Crie uma função chamada quadrado(numero) que recebe um número como argumento e retorna o quadrado dele.
#Depois, use a função com um valor recebido via input() e exiba o resultado com print().

def quadrado(numero):
    return numero ** 2

quadrado_input = float(input("Digite um número para calcular o quadrado: "))
resultado = quadrado(quadrado_input)
print(f"O quadrado de {quadrado_input} é: {resultado}")

quadrado(quadrado_input)
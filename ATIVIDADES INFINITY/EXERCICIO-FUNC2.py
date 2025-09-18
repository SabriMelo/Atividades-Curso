def maior_numero(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

NUMEROS = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))
MAIOR = maior_numero(NUMEROS[0], NUMEROS[1], NUMEROS[2]) # Fiz dessa forma para facilitar o entendimento, mas descobri que colocar um * antes do NUMEROS também funciona.
# MAIOR = maior_numero(*NUMEROS)

print(f"O maior número é: {MAIOR}")
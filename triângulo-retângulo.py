import math

def teorema_pitagoras(cateto1, cateto2):
    return math.sqrt(cateto1*2 + cateto2*2)

def seno(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    return math.sin(angulo_radianos)

def cosseno(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    return math.cos(angulo_radianos)

def tangente(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    return math.tan(angulo_radianos)

def menu():
    print("Calculadora de Triângulo Retângulo:")
    print("1. Teorema de Pitágoras")
    print("2. Calcular seno")
    print("3. Calcular cosseno")
    print("4. Calcular tangente")
    print("5. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção (1/2/3/4/5): ")
    
    if escolha == '1':
        cateto1 = float(input("Insira o valor do primeiro cateto: "))
        cateto2 = float(input("Insira o valor do segundo cateto: "))
        resultado = teorema_pitagoras(cateto1, cateto2)
        print(f"A hipotenusa é {resultado}.\n")
        
    elif escolha == '2':
        angulo = float(input("Insira o valor do ângulo em graus: "))
        resultado = seno(angulo)
        print(f"O seno de {angulo} graus é {resultado}.\n")
    
    elif escolha == '3':
        angulo = float(input("Insira o valor do ângulo em graus: "))
        resultado = cosseno(angulo)
        print(f"O cosseno de {angulo} graus é {resultado}.\n")
        
    elif escolha == '4':
        angulo = float(input("Insira o valor do ângulo em graus: "))
        resultado = tangente(angulo)
        print(f"A tangente de {angulo} graus é {resultado}.\n")
    
    elif escolha == '5':
        print("Saindo...")
        break
    
    else:
        print("Opção inválida! Tente novamente.\n")
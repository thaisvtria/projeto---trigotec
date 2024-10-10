import math

def graus_para_radianos(angulo_graus):
    return angulo_graus * (math.pi / 180)

def radianos_para_graus(angulo_radianos):
    return angulo_radianos * (180 / math.pi)

def menu():
    print("Calculadora de Conversão:")
    print("1. Converter graus para radianos")
    print("2. Converter radianos para graus")
    print("3. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção (1/2/3): ")
    
    if escolha == '1':
        angulo_graus = float(input("Insira o ângulo em graus: "))
        resultado = graus_para_radianos(angulo_graus)
        print(f"{angulo_graus} graus é igual a {resultado} radianos.\n")
        
    elif escolha == '2':
        angulo_radianos = float(input("Insira o ângulo em radianos: "))
        resultado = radianos_para_graus(angulo_radianos)
        print(f"{angulo_radianos} radianos é igual a {resultado} graus.\n")
    
    elif escolha == '3':
        print("Saindo...")
        break
    
    else:
        print("Opção inválida! Tente novamente.\n")
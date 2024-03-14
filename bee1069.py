caso_teste = int(input("Digite o número de casos de teste: "))

for _ in range(caso_teste):
    diamante = input("Digite a sequência de diamantes: ")
    
    pares_diamantes = 0
    diamantes_abertos = 0
    
    for aspas in diamante:
        if aspas == "<":
            diamantes_abertos += 1
        elif aspas == ">" and diamantes_abertos > 0:
            pares_diamantes += 1
            diamantes_abertos -= 1
    
    print(f"O número total de pares de diamantes é: {pares_diamantes}")



            
   
            


    
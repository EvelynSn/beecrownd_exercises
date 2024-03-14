caso_teste = int(input())

for _ in range(caso_teste):
    diamante = input()
    
    pares_diamantes = 0
    diamantes_abertos = 0
    
    for aspas in diamante:
        if aspas == "<":
            diamantes_abertos += 1
        elif aspas == ">" and diamantes_abertos > 0:
            pares_diamantes += 1
            diamantes_abertos -= 1
    
    print(pares_diamantes)



            
   
            


    

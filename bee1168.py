leds_por_digito = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

lista = []
caso_teste = int(input("Quantos casos de teste deseja realizar? "))

for _ in range(caso_teste):
    valor = input("Digite o número: ")
    digitos = [int(digito) for digito in valor]
    leds_total = 0
    
    for digito in digitos:
        leds_total += leds_por_digito[digito]
        
    lista.append(leds_total)

for leds in lista:
    print(leds, "leds")

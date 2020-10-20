from math import *

print("Informe tudas as medidas em metros")
H = float(input("Tamanho do Cilíndro: "))
h = float(input("Altura do combustível em relação a base: "))
r = float(input("Raio do bojo semiesférico: "))

if (H > 0 and h > 0 and r > 0):
    '''print("ok")'''
    if (H > h and H > 2 * r):
        '''print("ok")'''
        if h == r:
            Vcomb = (2 * pi * (r ** 3)) / 3  # metros cubicos
            Vcomb = Vcomb * 1000
            print(round(Vcomb, 3), 'Litros')
        elif h < r:
            Vcomb = (pi / 3) * ((H - h) ** (2) * 3 * r - (H - h))  # metros cubicos
            Vcomb = Vcomb * 1000
            print(round(Vcomb, 3), 'Litros')
        else:
            Vcomb = (pi * r ** 2 * (h - r)) + (2 * pi * r ** 3) / 3  # metros cubicos
            Vcomb = Vcomb * 1000
            print(round(Vcomb, 3), 'Litros')
    else:
        '''print("erro")'''
        print('Dados de Entrada: ', H, h, r)
        print('Dados inválidos.')
else:
    '''print("erro")'''
    print('Dados de Entrada: ', H, h, r)
    print('Dados inválidos.')
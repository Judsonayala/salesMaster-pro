

import os
def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def calcular_comision(ventas, tasa):
    return ventas * tasa
"""calcula la comision basica basada en las ventas"""
def verificar_bono(ventas, meta=100000):
    if ventas >= meta:
        return 30000
    return 0
"""verifica si el vendedor califica para el bono"""


def ejecutar_sistema():
    continuar = "s"
    
    

    while continuar.lower() == "s":
        
        limpiar_pantalla()
        print("----BIENVENIDO AL SISTEMA----")
        print("=" * 30)
        nombre = input("ingrese nombre del vendedor: ")
        try:
            ventas_input = input(f"ingrese las ventas totales de {nombre}:")
            ventas = float(ventas_input)
        

            tasa_comision = 0.1

            comision = calcular_comision(ventas, tasa_comision)
            bono = verificar_bono(ventas)
            total = comision + bono
        

            print("\n" + "=" * 30)
            print(f"RESUMEN DE PAGOS")
            print("=" * 30)
            
            print(f"vendedor: {nombre}")
            print(f"comision calculada {comision}")
        
            if bono > 0:
                print(f"BONO POR META: {bono}")
            print(f"PAGO TOTAL: {total}")
            print("=" * 30)
        except ValueError:
            print("ERROR por favor ingrese un numero valido") 
        
        continuar = input("\n desea ingresar otro vendedor? (s/n): ")
     
if __name__ == "__main__":
    ejecutar_sistema()


      







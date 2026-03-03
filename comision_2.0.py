import os
#el molde clase
class vendedor:
    def __init__(self, nombre, ventas):
        self.nombre = nombre
        self.ventas = ventas
        self.tasa_comision = 0.10
        self.meta = 100000
        self.monto_bono = 30000
    
    def calcular_comision(self):
        return self.ventas * self.tasa_comision
    def calcular_bono(self):
        if self.ventas >= self.meta:
            return self.monto_bono
        return 0
    def obtener_total(self):
        return self.calcular_comision + self.calcular_bono
def limpiar_pantalla():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")


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
            sujeto = vendedor(nombre,ventas)
            comision = sujeto.calcular_comision()
            bono = sujeto.calcular_bono()
            total = sujeto.obtener_total()
                
            

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
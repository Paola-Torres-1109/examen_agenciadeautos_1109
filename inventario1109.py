print("Examen tabla iventario")
print("Paola Torres Valle Mat: 22308051281109")

#Zona de clases
class Inventario1109: 

    #Zona de atributos
    id_inventario = 0
    vehiculo = ""
    cantidad_d = 0
    ubicacion = ""
    estado_v = ""
    proveedor = ""
    marca = ""


    #Funciones creadas por el usuario
    def altas(self):
        print("Tenemos disponible 21 carros")
    def bajas(self):
        print("No lo tenemos disponible")


    #Zona de funciones
    def marcas_lista(self):
        lista_marcas = ["Chevrolet", "Audi", "BMW", "Infinity", "Mercedes"]
        for x in lista_marcas:
            print (x)
    def tupla_ubicaciones(self):
        ubi_tupla = ("Suc. Juarez", "Suc. Chihuahua", "Suc. Jimenez", "Suc. Delicias", "Suc. Camargo")
        for y in ubi_tupla:
            print (y)
    def dicc_vehiculo(self):
        inventario= {
            "marca: ": "Chevrolet",
            "Modelo: ": "Camaro ZL1",
            "Cantidad: ": "17"
        }
        for a, b in inventario.items():
            print( a, b )


inventario = Inventario1109()

#Valores a objetos
inventario.id_inventario = 1255
inventario.vehiculo = "Challenger"
inventario.cantidad_d = 17
inventario.ubicacion = "Suc. Juarez"
inventario.estado_v = "Nuevo"
inventario.proveedor = "MOPAR"
inventario.marca = "Dodge" 

#Llamando objetos
print("")
print("Datos del inventario: ")
print(f"Id de inventario: {inventario.id_inventario}")
print(f"Vehiculo: {inventario.vehiculo}")
print(f"Cantidad de vehiculos: {inventario.cantidad_d}")
print(f"Ubicacion: {inventario.ubicacion}")
print(f"Estado del vehiculo: {inventario.estado_v}")
print(f"Proveedor: {inventario.proveedor}")
print(f"Marca del vehiculo: {inventario.marca}")
print("")



#Llamadas a funciones
print("------Lista------\n**Marcas de carros:**")
inventario.marcas_lista()
print("")
print("------Tupla------\n**Ubicaciones:**")
inventario.tupla_ubicaciones()
print("")
print("------Diccionario------\n**Vehiculo:**")
inventario.dicc_vehiculo()


print("")
print("Mis dos funciones")
inventario.altas()
inventario.bajas()








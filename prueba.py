import random
import math
import os
import globales
import json

PRODUCTOS = [
"Café Americano",
"Té Chai",
"Croissant",
"Jugo Naranja",
"Panini de Pavo y Queso",
"Pastel de Zanahoria",
"Espresso Doble",
"Ba;do de Frutas",
"Muffin",
"Ensalada",
"Chocolate Caliente",
"Tarta de Frambuesa",
"Sándwich de Huevo",
"Galletas de Avena",
"Frappé de Caramelo"
]

DIR='archivo.json'

MONTO_MIN=20
MONTO_MAX=100

def generar_montos():
    montos=[]
    for _ in range(len(PRODUCTOS)):
        monto=random.randint(MONTO_MIN,MONTO_MAX)
        monto*=100
        montos.append(monto)
    return montos

def crea_producto():
    lista_productos=[]
    montos=generar_montos()
    for i,prod in enumerate(PRODUCTOS):
        producto={
            'nombre':prod,
            'valor':montos[i],
            'Iva':round(montos[i]*0.19)
         }
        lista_productos.append(producto)
    globales.guardar_archivo_json(DIR,lista_productos)
    print("Lista de productos creada exitosamente! :D")
    return

def estadisticas():
    data=globales.leer_archivo_json(DIR)
    if not data:
        print("Primero se debe generar la lista de los productos! [ENTER PARA VOLVER AL MENU]")
        input()
        return
    max_val=0
    min_iva=100000000
    val=0
    valores=[]
    for producto in data:
        if max_val<producto['valor']:
            mayor=producto['nombre']
        if min_iva>producto['Iva']:
            menor=producto['nombre']
        val+=producto['valor']
        valores.append(producto['valor'])
    

    promedio=val/len(data)
    media_g=media_geometrica(valores)
    print("ESTADISTICAS:")
    print("--------------------------------------------------------------")
    print(f"Producto con mayor valor: {mayor}")
    print(f"Producto con menor IVA: {menor}")
    print(f"Promedio del valor de todos los productos: {promedio}")
    print(f"Media Geometrica del valor de los productos: {media_g}")
    print("--------------------------------------------------------------")
    
    input("[ENTER PARA VOLVER AL MENU]")

def media_geometrica(valores):
    num=1
    for i in valores:
        num*=i
    media_g=math.pow(num,1/len(valores))
    return media_g


def main():
    menu=True
    while menu:
        print("MENU")
        print("1.Asignar montos aleatorios.")
        print("2.Ver estadisticas.")
        print("3.Salir del programa.")
        opc=globales.seleccionar_opcion(3)

        if opc == 1:
            crea_producto()
        elif opc == 2:
            estadisticas()
        else:
            print("Chao :D")
            input()
            return
            



if __name__ == '__main__':
    main()
    
   


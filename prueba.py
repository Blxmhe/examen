productos = {
    '8475HD':['HP',15.6,'8GB','DD','1T','Intel Core i5','Nvidia GTX1050'],
    '2175HD':['LENOVO',14,'4GB','SSD','512GB','Intel Core i5', 'Nvidia GTX1050']
}

stock = {
    '8475HD':[387990,10],
    '2175HD':[327990,4]
}



def stock_marca():

    marca = input('Ingresa la marca de la cual deseas buscar stock: ').upper()
    suma = 0

    for producto,i in productos.items():
        if i[0] == marca:
            suma += stock[producto][1]
    print (f'Tienes {suma} unidades de la marca que deseas')



def busqueda_precio(p_min,p_max):

    for producto, i in stock.items():
        if p_min <= i[0] <= p_max and i[1]>0:
            print(productos[producto][0],'--',producto)

        else:
            print('No hay Notebooks en ese rango de precios o no hay stock')

def actualizar_precio(modelo,p):
    while True:
        if modelo not in stock:
            return False
        else:
            return True


while True:
    print('===MENÚ PRINCIPAL===')
    print('1.-Stock marca\n2.-Búsqueda por precio\n3.-Actualizar precio\n4.-Salir')

    opcion = input('Ingrese opción deseada: ')

    if opcion == '1':
        stock_marca()
    elif opcion == '2':
        while True:
            try:
                precio_minimo = int(input('Ingresa el precio mínimo que puedes pagar por el producto: '))
                precio_maximo = int(input('Ingresa el precio máximo que puedes pagar por el producto: '))
                    
            except Exception as error:
                print(f'ERROR {error}. Ingresa solamente números enteros!!')
            else:
                break
        busqueda_precio(precio_minimo,precio_maximo)

    elif opcion == '3':

        while True:
            modelo = input('Ingresa el modelo que deseas actualizar: ')
            while True:
                try:
                    precio = int(input('Ingresa el precio que al que deseas actualizar este modelo: '))
                        
                except Exception as error:
                    print(f'ERROR {error}. Ingresa solamente números enteros!!')
                else:
                    break
            
            if actualizar_precio(modelo,precio) == True:
                stock[modelo][1] = precio
                print('Precio actualizado!!')
            else:
                print('El modelo no existe!!')
            
            salir = input('Deseas actualizar otro precio? Presiona "s" para si y cualquier otra tecla para no: ').lower
            if salir != 's':
                break
    
    elif opcion == '4':
        print('Programa finalizado')
        break
    else:
        print('Selecciona una opción válida!!')
    
    
    
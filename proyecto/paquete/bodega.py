import json
class Producto():
    def __init__(self, codigo:str, articulo:str, costo:float):
        self.codigo=codigo
        self.articulo=articulo
        self.costo=costo

    def actualizar_datos_producto(self, nuevo_codigo:str, nuevo_articulo:str, nuevo_costo:float):
        self.codigo=nuevo_codigo
        self.articulo=nuevo_articulo
        self.costo=nuevo_costo
    
    def imprimir_datos_producto(self):
        producto = {"CODIGO":self.codigo, "ARTICULO":self.articulo, "COSTO":self.costo }
        for k,v in producto.items():
            print(k,v)

class Bodega():
    def __init__(self, *args):#meter como atributos a los productos que estan en la bodega
        self.productos={}
        self.entradas={}
        self.salidas={}
        self.devolucion={}
        for x in range(len(args)):
            self.productos[args[x].codigo]={"ARTICULO":args[x].articulo, "COSTO":args[x].costo,"ENTRADAS": 0, "SALIDAS": 0, "DEVOLUCION":0, "STOCK":0}
    
    def agregar_producto_a_bodega(self, producto:Producto):
        self.productos[producto.codigo]={"ARTICULO":producto.articulo, "COSTO":producto.costo,"ENTRADAS": 0, "SALIDAS": 0, "DEVOLUCION":0, "STOCK":0}
    
    def retirar_producto_de_bodega(self, producto:Producto):
        del self.productos[producto.codigo]

    def imprimir_productos_bodega(self):
        for k,v in self.productos.items():
            print(k,v)
    
    def crear_archivo_productos_bodega(self):
        data=self.productos
        writeFile = open("data_productos_bodega.json","w")
        json.dump(data, writeFile)
        writeFile.close()
        print("Archivo creado exitosamente.")

    def imprimir_producto_especifico_bodega(self, producto:Producto):
        if producto.codigo in self.productos:
            print(producto.codigo, (self.productos[producto.codigo]))
        else:
            print("El producto no existe en bodega.")

    def registrar_entrada_producto(self, codigo_producto_entrada: str, fecha_entrada:str, cantidad_producto_entrada:int):
        self.codigo=codigo_producto_entrada
        self.fecha=fecha_entrada
        self.cantidad=cantidad_producto_entrada
        if self.codigo in self.productos:
            longitud_diccionario=len(self.entradas)
            self.entradas[int(longitud_diccionario+1)]={"CODIGO":self.codigo, "ARTICULO":self.productos.get(self.codigo).get("ARTICULO"), "FECHA":self.fecha, "CANTIDAD":self.cantidad}
            self.productos[codigo_producto_entrada]["ENTRADAS"]+=int(self.cantidad)
            self.productos[codigo_producto_entrada]["STOCK"]+=int(self.cantidad)
        else:
            print("Código inexistente, la entrada del producto no se puede registrar.")
    
    def eliminar_registro_entrada(self,numero_de_registro:int):
        self.productos[self.entradas[numero_de_registro]["CODIGO"]]["ENTRADAS"]-=int(self.entradas.get(numero_de_registro).get("CANTIDAD"))
        self.productos[self.entradas[numero_de_registro]["CODIGO"]]["STOCK"]-=int(self.entradas.get(numero_de_registro).get("CANTIDAD"))
        del self.entradas[numero_de_registro]

    def imprimir_entradas_bodega(self):
        for k,v in self.entradas.items():
            print(k,v)

    def crear_archivo_entradas_bodega(self):
            data=self.entradas
            writeFile = open("data_entradas_bodega.json","w")
            json.dump(data, writeFile)
            writeFile.close()
            print("Archivo creado exitosamente.")

    def registrar_salida_producto(self, codigo_producto_salida: str, fecha_salida:str, cantidad_producto_salida:int):
        self.codigo=codigo_producto_salida
        self.fecha=fecha_salida
        self.cantidad=cantidad_producto_salida
        if self.codigo in self.productos:
            longitud_diccionario=len(self.salidas)
            self.salidas[int(longitud_diccionario+1)]={"CODIGO":self.codigo, "ARTICULO":self.productos.get(self.codigo).get("ARTICULO"), "FECHA":self.fecha, "CANTIDAD":self.cantidad}
            self.productos[codigo_producto_salida]["SALIDAS"]+=int(self.cantidad)
            self.productos[codigo_producto_salida]["STOCK"]-=int(self.cantidad)
        else:
            print("Código inexistente, la salida del producto no se puede registrar.")

    def eliminar_registro_salida(self,numero_de_registro:int):
        self.productos[self.salidas[numero_de_registro]["CODIGO"]]["SALIDAS"]+=int(self.salidas.get(numero_de_registro).get("CANTIDAD"))
        self.productos[self.salidas[numero_de_registro]["CODIGO"]]["STOCK"]+=int(self.salidas.get(numero_de_registro).get("CANTIDAD"))
        del self.salidas[numero_de_registro]

    def imprimir_salidas_bodega(self):
        for k, v in self.salidas.items():
            print(k,v)

    def crear_archivo_salidas_bodega(self):
            data=self.salidas
            writeFile = open("data_salidas_bodega.json","w")
            json.dump(data, writeFile)
            writeFile.close()
            print("Archivo creado exitosamente.")

    def registrar_devolucion_producto(self, codigo_producto_devolucion: str, fecha_devolucion:str, cantidad_producto_devolucion:int):
        self.codigo=codigo_producto_devolucion
        self.fecha=fecha_devolucion
        self.cantidad=cantidad_producto_devolucion
        if self.codigo in self.productos:
            longitud_diccionario=len(self.devolucion)
            self.devolucion[int(longitud_diccionario+1)]={"CODIGO":self.codigo, "ARTICULO":self.productos.get(self.codigo).get("ARTICULO"), "FECHA":self.fecha, "CANTIDAD":self.cantidad}
            self.productos[self.codigo]["DEVOLUCION"]+=int(self.cantidad)
            self.productos[self.codigo]["STOCK"]+=int(self.cantidad)
        else:
            print("Código inexistente, la devolucion del producto no se puede registrar.")
    
    def eliminar_registro_devolucion(self,numero_de_registro:int):
        self.productos[self.entradas[numero_de_registro]["CODIGO"]]["DEVOLUCION"]-=int(self.entradas.get(numero_de_registro).get("CANTIDAD"))
        self.productos[self.devolucion[numero_de_registro]["CODIGO"]]["STOCK"]-=int(self.devolucion.get(numero_de_registro).get("CANTIDAD"))
        del self.devolucion[numero_de_registro]

    def imprimir_devolucion_bodega(self):
        for k,v in self.devolucion.items():
            print(k,v)

    def crear_archivo_devoluciones_bodega(self):
            data=self.devolucion
            writeFile = open("data_devoluciones_bodega.json","w")
            json.dump(data, writeFile)
            writeFile.close()
            print("Archivo creado exitosamente.")

    def control(self):#Método para hacer conteo del inventario y confirmar que los datos del sistema sean iguales a los del conteo
        control_correcto={}
        control_incorrecto={}
        tipo_control=int(input("Usted va a realizar el control extracontable. Si el control es del todo el inventario ingrese el número 1, si es de solo un producto ingrese el número 2: "))
        if tipo_control==1:
            for x in self.productos:
                cantidad=int(input("Digite la cantidad de "+ str(x)+ " : "+str(self.productos.get(x).get("ARTICULO"))+" que hay en la bodega: "))
                if cantidad==int(self.productos.get(x).get("STOCK")):
                    control_correcto[x]={"ARTICULO":self.productos.get(x).get("ARTICULO"),"CANTIDAD":self.productos.get(x).get("STOCK")}
                    print("Los datos ingresados SÍ coinciden con los datos del sistema.")
                else:
                    control_incorrecto[x]={"ARTICULO":self.productos.get(x).get("ARTICULO"),"CANTIDAD BODEGA":self.productos.get(x).get("STOCK"), "CANTIDAD DEL CONTEO":cantidad}
                    print("Los datos ingresados NO coinciden con los datos del sistema. ")
            if len(control_correcto)>0:
                print("Los productos en los que SÍ coincide la cantidad en el sistema y en el conteo son: ")
                for k, v in control_correcto.items():
                    print(k,v)
            if len(control_incorrecto)>0:
                print("Los productos en los que NO coincide la cantidad en el sistema y en el conteo son: ")
                for k,v in control_incorrecto.items():
                    print(k,v)
        elif tipo_control==2:
            producto_control=str(input("Ingrese el código del producto del cual desea hacer el control: "))
            if producto_control in self.productos:
                cantidad=int(input("Digite la cantidad de "+ producto_control + " : "+str(self.productos.get(producto_control).get("ARTICULO"))+" que hay en la bodega: "))
                if cantidad==int(self.productos.get(producto_control).get("STOCK")):
                    print("Los datos ingresados SÍ coinciden con los datos del sistema.")
                else:
                    print("Los datos ingresados NO coinciden con los datos del sistema. ")
                    control_incorrecto[producto_control]={"ARTICULO":self.productos.get(producto_control).get("ARTICULO"),"CANTIDAD BODEGA":self.productos.get(producto_control).get("STOCK"), "CANTIDAD DEL CONTEO":cantidad}
                    for k,v in control_incorrecto.items():
                        print(k,v)
            else:
                print("El código ingresado no existe.")
        else:
            print("El número ingresado no es válido.")

        print("El control ha finalizado.")


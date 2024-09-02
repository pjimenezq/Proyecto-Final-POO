import json
class Producto():
    def __init__(self, referencia:str, articulo:str, precio:float, color:str, talla: str, material:str):
        self.referencia=referencia
        self.articulo=articulo
        self.precio=precio
        self.color=color
        self.talla=talla
        self.material=material

    def actualizar_informacion_producto(self, nueva_referencia:str, nuevo_articulo:str, nuevo_precio:float, nuevo_color:str, nueva_talla:str, nuevo_material:str):
        self.referencia=nueva_referencia
        self.articulo=nuevo_articulo
        self.precio=nuevo_precio
        self.color=nuevo_color
        self.talla=nueva_talla
        self.material=nuevo_material
        print("La información del producto",self.articulo, "fue actualizada exitosamente.")

    def imprimir_informacion_producto(self):
        informacion_producto = {"REFERENCIA":self.referencia, "ARTÍCULO":self.articulo, "PRECIO":self.precio, "COLOR":self.color, "TALLA":self.talla, "MATERIAL": self.material}
        print("La información del producto", self.articulo, "es:")
        for k,v in informacion_producto.items():
            print(k,":", v)

class Bodega():
    def __init__(self, *args):#meter como atributos a los productos que estan en la bodega
        self.productos={}
        self.entradas={}
        self.salidas={}
        self.devolucion={}
        for x in range(len(args)):
            self.productos[args[x].referencia]={"ARTÍCULO":args[x].articulo, "PRECIO":args[x].precio,"ENTRADAS": 0, "SALIDAS": 0, "DEVOLUCIÓN":0, "STOCK":0}
    
    def agregar_producto_a_bodega(self, producto:Producto):
        if producto.referencia in self.productos:
            print("El producto",producto.articulo,"no se puede agregar a la bodega porque ya se encuentra registrado dentro del inventario de la bodega.")
        else:
            self.productos[producto.referencia]={"ARTÍCULO":producto.articulo, "PRECIO":producto.precio,"ENTRADAS": 0, "SALIDAS": 0, "DEVOLUCIÓN":0, "STOCK":0}
            print("El producto",producto.articulo,"fue agregado a bodega exitosamente.")

    def retirar_producto_de_bodega(self, producto:Producto):
        if producto.referencia in self.productos:
            del self.productos[producto.referencia]
            print("El producto",producto.articulo,"fue retirado de bodega exitosamente.")
        else:
            print("El producto",producto.articulo,"no se puede retirar de la bodega porque no se encuentra registrado dentro del inventario de la bodega.")

    def imprimir_productos_bodega(self):
        if len(self.productos)>0:
            print("La información de todos los productos que hay en el inventario de la bodega y el resumen de sus movimientos son: ")
            for k,v in self.productos.items():
                print(k,v)
        else:
            print("No hay ningún producto registrado en el inventario de la bodega.")
    
    def crear_archivo_productos_bodega(self):
        data=self.productos
        writeFile = open("data_productos_bodega.json","w")
        json.dump(data, writeFile)
        writeFile.close()
        print("El archivo de los productos en bodega fue creado exitosamente.")

    def imprimir_producto_especifico_bodega(self, producto:Producto):
        if producto.referencia in self.productos:
            print("La información del producto",producto.articulo,"y el resumen de sus movimientos son: ")
            print(producto.referencia, (self.productos[producto.referencia]))
        else:
            print("No se puede imprimir la información del producto",producto.articulo,"porque no se encuentra registrado dentro del inventario de la bodega.")

    def registrar_entrada_producto(self, referencia_producto_entrada: str, fecha_entrada:str, cantidad_producto_entrada:int):
        if referencia_producto_entrada in self.productos:
            longitud_diccionario=len(self.entradas)
            self.entradas[int(longitud_diccionario+1)]={"REFERENCIA":referencia_producto_entrada, "ARTÍCULO":self.productos.get(referencia_producto_entrada).get("ARTÍCULO"), "FECHA":fecha_entrada, "CANTIDAD":cantidad_producto_entrada}
            self.productos[referencia_producto_entrada]["ENTRADAS"]+=int(cantidad_producto_entrada)
            self.productos[referencia_producto_entrada]["STOCK"]+=int(cantidad_producto_entrada)
            print("La entrada del producto",self.productos.get(referencia_producto_entrada).get("ARTÍCULO"),"fue registrada exitosamente.")
        else:
            print("La entrada del producto no se puede registrar porque la referencia ingresada no existe en el inventario de la bodega.")
    
    def eliminar_registro_entrada(self,numero_de_registro_entrada:int):
        if numero_de_registro_entrada in self.entradas:
            self.productos[self.entradas[numero_de_registro_entrada]["REFERENCIA"]]["ENTRADAS"]-=int(self.entradas.get(numero_de_registro_entrada).get("CANTIDAD"))
            self.productos[self.entradas[numero_de_registro_entrada]["REFERENCIA"]]["STOCK"]-=int(self.entradas.get(numero_de_registro_entrada).get("CANTIDAD"))
            del self.entradas[numero_de_registro_entrada]
            print("La entrada con el número de registro ", numero_de_registro_entrada, "fue eliminada exitosamente.")
        else:
            print("No se puede eliminar la entrada con el número de registro", numero_de_registro_entrada, "porque no existe ese número de registro en el historial de entradas a la bodega.")

    def imprimir_entradas_bodega(self):
        if len(self.entradas)>0:
            print("El historial de todos los registros de las entradas a la bodega es: ")
            for k,v in self.entradas.items():
                print(k,v)
        else:
            print("Ninguna entrada a la bodega ha sido registrada.")

    def crear_archivo_entradas_bodega(self):
            data=self.entradas
            writeFile = open("data_entradas_bodega.json","w")
            json.dump(data, writeFile)
            writeFile.close()
            print("El archivo de las entradas a la bodega fue creado exitosamente.")

    def registrar_salida_producto(self, referencia_producto_salida: str, fecha_salida:str, cantidad_producto_salida:int):
        if referencia_producto_salida in self.productos:
            if cantidad_producto_salida<=self.productos.get(referencia_producto_salida).get("STOCK"):
                longitud_diccionario=len(self.salidas)
                self.salidas[int(longitud_diccionario+1)]={"REFERENCIA":referencia_producto_salida, "ARTÍCULO":self.productos.get(referencia_producto_salida).get("ARTÍCULO"), "FECHA":fecha_salida, "CANTIDAD":cantidad_producto_salida}
                self.productos[referencia_producto_salida]["SALIDAS"]+=int(cantidad_producto_salida)
                self.productos[referencia_producto_salida]["STOCK"]-=int(cantidad_producto_salida)
                print("La salida del producto",self.productos.get(referencia_producto_salida).get("ARTÍCULO"),"fue registrada exitosamente.")
            else:
                print("La salida del producto",self.productos.get(referencia_producto_salida).get("ARTÍCULO"),"no se puede registrar porque no hay suficientes unidades del producto en el stock.")
        else:
            print("La salida del producto no se puede registrar porque la referencia ingresada no existe en el inventario de la bodega.")

    def eliminar_registro_salida(self,numero_de_registro_salida:int):
        if numero_de_registro_salida in self.salidas:
            self.productos[self.salidas[numero_de_registro_salida]["REFERENCIA"]]["SALIDAS"]-=int(self.salidas.get(numero_de_registro_salida).get("CANTIDAD"))
            self.productos[self.salidas[numero_de_registro_salida]["REFERENCIA"]]["STOCK"]+=int(self.salidas.get(numero_de_registro_salida).get("CANTIDAD"))
            del self.salidas[numero_de_registro_salida]
            print("La salida con el número de registro ", numero_de_registro_salida, "fue eliminada exitosamente.")
        else:
            print("No se puede eliminar la salida con el número de registro", numero_de_registro_salida, "porque no existe ese número de registro en el historial de salidas de la bodega.")

    def imprimir_salidas_bodega(self):
        if len(self.salidas)>0:
            print("El historial de todos los registros de las salidas de la bodega es:")
            for k, v in self.salidas.items():
                print(k,v)
        else:
            print("Ninguna salida de la bodega ha sido registrada.")

    def crear_archivo_salidas_bodega(self):
            data=self.salidas
            writeFile = open("data_salidas_bodega.json","w")
            json.dump(data, writeFile)
            writeFile.close()
            print("El archivo de las salidas de la bodega fue creado exitosamente.")

    def registrar_devolucion_producto(self, referencia_producto_devolucion: str, fecha_devolucion:str, cantidad_producto_devolucion:int):
        if referencia_producto_devolucion in self.productos:
            if cantidad_producto_devolucion<=self.productos.get(referencia_producto_devolucion).get("SALIDAS"):
                longitud_diccionario=len(self.devolucion)
                self.devolucion[int(longitud_diccionario+1)]={"REFERENCIA":referencia_producto_devolucion, "ARTÍCULO":self.productos.get(referencia_producto_devolucion).get("ARTÍCULO"), "FECHA":fecha_devolucion, "CANTIDAD":cantidad_producto_devolucion}
                self.productos[referencia_producto_devolucion]["DEVOLUCIÓN"]+=int(cantidad_producto_devolucion)
                self.productos[referencia_producto_devolucion]["STOCK"]+=int(cantidad_producto_devolucion)
                print("La devolución del producto",self.productos.get(referencia_producto_devolucion).get("ARTÍCULO"),"fue registrada exitosamente.")
            else: 
                print("La salida del producto", self.productos.get(referencia_producto_devolucion).get("ARTÍCULO"), "no se puede registrar porque la cantidad de devolución no puede ser mayor a la cantidad de salidas del producto.")
        else:
            print("La devolución del producto no se puede registrar porque la referencia ingresada no existe en el inventario de la bodega.")
    
    def eliminar_registro_devolucion(self,numero_de_registro_devolucion:int):
        if numero_de_registro_devolucion in self.devolucion:
            self.productos[self.entradas[numero_de_registro_devolucion]["REFERENCIA"]]["DEVOLUCIÓN"]-=int(self.devolucion.get(numero_de_registro_devolucion).get("CANTIDAD"))
            self.productos[self.devolucion[numero_de_registro_devolucion]["REFERENCIA"]]["STOCK"]-=int(self.devolucion.get(numero_de_registro_devolucion).get("CANTIDAD"))
            del self.devolucion[numero_de_registro_devolucion]
            print("La devolución con el número de registro ", numero_de_registro_devolucion, "fue eliminada exitosamente.")
        else:
            print("No se puede eliminar la devolución con el número de registro", numero_de_registro_devolucion, "porque no existe ese número de registro en el historial de devoluciones de la bodega.")
    
    def imprimir_devoluciones_bodega(self):
        if len(self.devolucion)>0:
            print("El historial de todos los registros de las devoluciones de la bodega es:")
            for k,v in self.devolucion.items():
                print(k,v)
        else:
            print("Ninguna devolución ha sido registrada.")

    def crear_archivo_devoluciones_bodega(self):
            data=self.devolucion
            writeFile = open("data_devoluciones_bodega.json","w")
            json.dump(data, writeFile)
            writeFile.close()
            print("El archivo de las devoluciones de la bodega fue creado exitosamente.")

    def control(self):#Método para hacer conteo del inventario y confirmar que los datos del sistema sean iguales a los del conteo
        control_correcto={}
        control_incorrecto={}
        tipo_control=int(input("Usted va a realizar el control extracontable. Si el control es del todo el inventario ingrese el número 1, si es de solo un producto ingrese el número 2: "))
        if tipo_control==1:
            for x in self.productos:
                cantidad=int(input("Digite la cantidad de "+ str(x)+ " : "+str(self.productos.get(x).get("ARTÍCULO"))+" que hay en la bodega: "))
                if cantidad==int(self.productos.get(x).get("STOCK")):
                    control_correcto[x]={"ARTÍCULO":self.productos.get(x).get("ARTÍCULO"),"CANTIDAD":self.productos.get(x).get("STOCK")}
                    print("Los datos ingresados SÍ coinciden con los datos del sistema.")
                else:
                    control_incorrecto[x]={"ARTÍCULO":self.productos.get(x).get("ARTÍCULO"),"CANTIDAD EN EL PROGRAMA":self.productos.get(x).get("STOCK"), "CANTIDAD DEL CONTEO":cantidad}
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
            producto_control=str(input("Ingrese la referencia del producto del cual desea hacer el control: "))
            if producto_control in self.productos:
                cantidad=int(input("Digite la cantidad de "+ producto_control + " : "+str(self.productos.get(producto_control).get("ARTÍCULO"))+" que hay en la bodega: "))
                if cantidad==int(self.productos.get(producto_control).get("STOCK")):
                    print("Los datos ingresados SÍ coinciden con los datos del sistema.")
                else:
                    print("Los datos ingresados NO coinciden con los datos del sistema. ")
                    control_incorrecto[producto_control]={"ARTÍCULO":self.productos.get(producto_control).get("ARTÍCULO"),"CANTIDAD EN EL PROGRAMA":self.productos.get(producto_control).get("STOCK"), "CANTIDAD DEL CONTEO":cantidad}
                    for k,v in control_incorrecto.items():
                        print(k,v)
            else:
                print("La referencia ingresada no existe en el inventario de la bodega.")
        else:
            print("El número ingresado no es válido.")

        print("El control ha finalizado.")


import json
import os.path

class Producto():
    def __init__(self, referencia:str, articulo:str, precio:float, color:str, talla: str, material:str):
        self.referencia=referencia
        self.articulo=articulo
        self.precio=precio
        self.color=color
        self.talla=talla
        self.material=material

    def imprimir_informacion_producto(self):
        informacion_producto = {"REFERENCIA":self.referencia, "ARTÍCULO":self.articulo, "PRECIO":self.precio, "COLOR":self.color, "TALLA":self.talla, "MATERIAL": self.material}
        print(informacion_producto)

class Bodega():
    def __init__(self, *args):#meter como atributos a los productos que estan en la bodega
        self.productos=self.abrir_archivo_productos_bodega()
        self.entradas=self.abrir_archivo_entradas_bodega()
        self.salidas=self.abrir_archivo_salidas_bodega()
        self.devoluciones=self.abrir_archivo_devoluciones_bodega()
        self.productos_en_bodega=[]
        for producto in args:
            self.productos_en_bodega.append(producto)
        for x in range(len(args)):
            self.productos[args[x].referencia]={"ARTÍCULO":args[x].articulo, "PRECIO":args[x].precio,"ENTRADAS": 0, "SALIDAS": 0, "DEVOLUCIÓN":0, "STOCK":0}

    def guardar_informacion(self):
        self.guardar_informacion_devoluciones_bodega()
        self.guardar_informacion_entradas_bodega()
        self.guardar_informacion_productos_bodega()
        self.guardar_informacion_salidas_bodega()

    def imprimir_caracteristicas_productos_bodega(self):
        for producto in self.productos_en_bodega:
            producto.imprimir_informacion_producto()

    def imprimir_caracteristicas_producto_especifico(self):
        print("Estos son los productos que hay en bodega")
        for indice, producto in enumerate(self.productos_en_bodega):
            print(indice+1,":", producto.referencia,"-", producto.articulo)
        indice_seleccion_producto=int(input("Ingrese el número correspondiente al producto que desea conocer: "))
        if indice_seleccion_producto not in range (1,len(self.productos_en_bodega)+1):
            print("El número ingresado no corresponde a ningún producto.")
        else:
            producto=self.productos_en_bodega[indice_seleccion_producto-1]
            if producto.referencia in (self.productos):
                producto.imprimir_informacion_producto()
            else:
                print("No se puede imprimir la información del producto",producto.articulo,"porque no se encuentra registrado dentro del inventario de la bodega.")

    def imprimir_productos_bodega(self):
        if len(self.productos)>0:
            print("La información de todos los productos que hay en el inventario de la bodega y el resumen de sus movimientos son: ")
            for k,v in self.productos.items():
                print(k,v)
        else:
            print("No hay ningún producto registrado en el inventario de la bodega.")
    
    def imprimir_producto_especifico_bodega(self):
        print("Estos son los productos que hay en bodega")
        for indice, producto in enumerate(self.productos_en_bodega):
            print(indice+1,":", producto.referencia,"-", producto.articulo)
        indice_seleccion_producto=int(input("Ingrese el número correspondiente al producto que desea conocer: "))
        if indice_seleccion_producto not in range (1,len(self.productos_en_bodega)+1):
            print("El número ingresado no corresponde a ningún producto.")
        else:
            producto=self.productos_en_bodega[indice_seleccion_producto-1]
            if producto.referencia in self.productos:
                print("La información del producto",producto.articulo,"y el resumen de sus movimientos son: ")
                print(producto.referencia, (self.productos[producto.referencia]))
            else:
                print("No se puede imprimir la información del producto",producto.articulo,"porque no se encuentra registrado dentro del inventario de la bodega.")

    def crear_archivo_productos_bodega(self):
        data=self.productos
        writeFile = open("data_productos_bodega.json","w")
        json.dump(data, writeFile)
        writeFile.close()
        print("El archivo de los productos en bodega fue creado exitosamente.")
    
    def abrir_archivo_productos_bodega(self):
        if os.path.isfile("data_productos_bodega.json"):
            readFile = open("data_productos_bodega.json","r")
            self.data=json.load(readFile)
            readFile.close()
            return self.data
        else:
            return {}
    
    def eliminar_todos_los_registros_de_movimientos(self):
        confirmacion=int(input("Presione el número 1 si usted desea eliminar todos los registros del los movimientos realizados en bodega, si desea cancelar la solicitud presione enter: "))
        if confirmacion==1:
            self.eliminar_historial_devoluciones()
            self.eliminar_historial_entradas()
            self.eliminar_historial_salidas()
            print("Se han eliminado todos los registros de los movimientos con éxito.")
    
    def guardar_informacion_productos_bodega(self):
        data=self.productos
        writeFile = open("data_productos_bodega.json","w")
        json.dump(data, writeFile)
        writeFile.close()

    def registrar_entrada_producto(self):
        print("\nIngrese la información correspondiente a la entrada del producto:")
        referencia_producto_entrada=str(input("Ingrese la referencia del producto: "))
        fecha_entrada=str(input("Ingrese la fecha de entrada: "))
        cantidad_producto_entrada=int(input("Ingrese la cantidad: "))
        if referencia_producto_entrada in self.productos:
            if len(self.entradas)>0:
                numero_ultimo_registro=max(self.entradas)
            else:
                numero_ultimo_registro=0
            self.entradas[int(numero_ultimo_registro+1)]={"REFERENCIA":referencia_producto_entrada, "ARTÍCULO":self.productos.get(referencia_producto_entrada).get("ARTÍCULO"), "FECHA":fecha_entrada, "CANTIDAD":cantidad_producto_entrada}
            self.productos[referencia_producto_entrada]["ENTRADAS"]+=int(cantidad_producto_entrada)
            self.productos[referencia_producto_entrada]["STOCK"]+=int(cantidad_producto_entrada)
            print("La entrada del producto",self.productos.get(referencia_producto_entrada).get("ARTÍCULO"),"fue registrada exitosamente.")
        else:
            print("La entrada del producto no se puede registrar porque la referencia ingresada no existe en el inventario de la bodega.")
    
    def eliminar_registro_entrada(self):
        numero_de_registro_entrada=int(input("Ingrese el número de registro de la entrada que desea eliminar: "))
        confirmacion=int(input("Presione el número 1 si usted desea eliminar el registro de la entrada número "+str(numero_de_registro_entrada)+"\nSi desea cancelar la solicitud de eliminar el registro de entrada presione enter."))
        if confirmacion==1:
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
    
    def eliminar_historial_entradas(self):
        self.entradas={}

    def abrir_archivo_entradas_bodega(self):
        if os.path.isfile("data_entradas_bodega.json"):
            readFile = open("data_entradas_bodega.json","r")
            self.data=json.load(readFile)
            readFile.close()
            return self.data
        else:
            return {}
    
    def guardar_informacion_entradas_bodega(self):
        data=self.entradas
        writeFile = open("data_entradas_bodega.json","w")
        json.dump(data, writeFile)
        writeFile.close()

    def registrar_salida_producto(self):
        print("\nIngrese la información correspondiente a la salida del producto:")
        referencia_producto_salida=str(input("Ingrese la referencia del producto: "))
        fecha_salida=str(input("Ingrese la fecha de salida: "))
        cantidad_producto_salida=int(input("Ingrese la cantidad: "))
        if referencia_producto_salida in self.productos:
            if cantidad_producto_salida<=self.productos.get(referencia_producto_salida).get("STOCK"):
                if len(self.salidas)>0:
                    numero_ultimo_registro=max(self.salidas)
                else:
                    numero_ultimo_registro=0
                self.salidas[int(numero_ultimo_registro+1)]={"REFERENCIA":referencia_producto_salida, "ARTÍCULO":self.productos.get(referencia_producto_salida).get("ARTÍCULO"), "FECHA":fecha_salida, "CANTIDAD":cantidad_producto_salida}
                self.productos[referencia_producto_salida]["SALIDAS"]+=int(cantidad_producto_salida)
                self.productos[referencia_producto_salida]["STOCK"]-=int(cantidad_producto_salida)
                print("La salida del producto",self.productos.get(referencia_producto_salida).get("ARTÍCULO"),"fue registrada exitosamente.")
            else:
                print("La salida del producto",self.productos.get(referencia_producto_salida).get("ARTÍCULO"),"no se puede registrar porque no hay suficientes unidades del producto en el stock.")
        else:
            print("La salida del producto no se puede registrar porque la referencia ingresada no existe en el inventario de la bodega.")

    def eliminar_registro_salida(self):
        numero_de_registro_salida=int(input("Ingrese el número de registro de la salida que desea eliminar: "))
        confirmacion=(input("Presione el número 1 si usted desea eliminar el registro de la salida número "+str(numero_de_registro_salida)+"\nSi desea cancelar la solicitud de eliminar el registro de salida presione enter."))
        if confirmacion==1:
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

    def eliminar_historial_salidas(self):
        self.salidas={}

    def abrir_archivo_salidas_bodega(self):
        if os.path.isfile("data_salidas_bodega.json"):
            readFile = open("data_salidas_bodega.json","r")
            self.data=json.load(readFile)
            readFile.close()
            return self.data
        else:
            return {}
    
    def guardar_informacion_salidas_bodega(self):
        data=self.salidas
        writeFile = open("data_salidas_bodega.json","w")
        json.dump(data, writeFile)
        writeFile.close()

    def registrar_devolucion_producto(self):
        print("\nIngrese la información correspondiente a la devolución del producto:")
        referencia_producto_devolucion=str(input("Ingrese la referencia del producto: "))
        fecha_devolucion=str(input("Ingrese la fecha de la devolución: "))
        cantidad_producto_devolucion=int(input("Ingrese la cantidad: "))
        if referencia_producto_devolucion in self.productos:
            if cantidad_producto_devolucion<=self.productos.get(referencia_producto_devolucion).get("SALIDAS"):
                if len(self.devoluciones)>0:
                    numero_ultimo_registro=max(self.devoluciones)
                else:
                    numero_ultimo_registro=0
                self.devoluciones[int(numero_ultimo_registro+1)]={"REFERENCIA":referencia_producto_devolucion, "ARTÍCULO":self.productos.get(referencia_producto_devolucion).get("ARTÍCULO"), "FECHA":fecha_devolucion, "CANTIDAD":cantidad_producto_devolucion}
                self.productos[referencia_producto_devolucion]["DEVOLUCIÓN"]+=int(cantidad_producto_devolucion)
                self.productos[referencia_producto_devolucion]["STOCK"]+=int(cantidad_producto_devolucion)
                print("La devolución del producto",self.productos.get(referencia_producto_devolucion).get("ARTÍCULO"),"fue registrada exitosamente.")
            else: 
                print("La salida del producto", self.productos.get(referencia_producto_devolucion).get("ARTÍCULO"), "no se puede registrar porque la cantidad de devolución no puede ser mayor a la cantidad de salidas del producto.")
        else:
            print("La devolución del producto no se puede registrar porque la referencia ingresada no existe en el inventario de la bodega.")
    
    def eliminar_registro_devolucion(self):
        numero_de_registro_devolucion=int(input("Ingrese el número de registro de la devolución que desea eliminar:"))
        confirmacion=int(input("Presione el número 1 si usted desea eliminar el registro de la devolución número "+str(numero_de_registro_devolucion)+"\nSi desea cancelar la solicitud de eliminar el registro de devolución presione enter."))
        if confirmacion==1:
            if numero_de_registro_devolucion in self.devoluciones:
                self.productos[self.entradas[numero_de_registro_devolucion]["REFERENCIA"]]["DEVOLUCIÓN"]-=int(self.devoluciones.get(numero_de_registro_devolucion).get("CANTIDAD"))
                self.productos[self.devoluciones[numero_de_registro_devolucion]["REFERENCIA"]]["STOCK"]-=int(self.devoluciones.get(numero_de_registro_devolucion).get("CANTIDAD"))
                del self.devoluciones[numero_de_registro_devolucion]
                print("La devolución con el número de registro ", numero_de_registro_devolucion, "fue eliminada exitosamente.")
            else:
                print("No se puede eliminar la devolución con el número de registro", numero_de_registro_devolucion, "porque no existe ese número de registro en el historial de devoluciones de la bodega.")
        
    def imprimir_devoluciones_bodega(self):
        if len(self.devoluciones)>0:
            print("El historial de todos los registros de las devoluciones de la bodega es:")
            for k,v in self.devoluciones.items():
                print(k,v)
        else:
            print("Ninguna devolución ha sido registrada.")

    def crear_archivo_devoluciones_bodega(self):
            data=self.devoluciones
            writeFile = open("data_devoluciones_bodega.json","w")
            json.dump(data, writeFile)
            writeFile.close()
            print("El archivo de las devoluciones de la bodega fue creado exitosamente.")

    def eliminar_historial_devoluciones(self):
        self.devoluciones={}

    def abrir_archivo_devoluciones_bodega(self):
        if os.path.isfile("data_devoluciones_bodega.json"):
            readFile = open("data_devoluciones_bodega.json","r")
            self.data=json.load(readFile)
            readFile.close()
            return self.data
        else:
            return {}
        
    def guardar_informacion_devoluciones_bodega(self):
        data=self.devoluciones
        writeFile = open("data_salidas_bodega.json","w")
        json.dump(data, writeFile)
        writeFile.close()

    def control(self, tipo_control):#Método para hacer conteo del inventario y confirmar que los datos del sistema sean iguales a los del conteo
        control_correcto={}
        control_incorrecto={}
        if tipo_control==1:##############
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
    
    def mostrar_instructivo(self):
        print("\nInstructivo del sistema de gestión de inventario de la bodega de NOTCHOLTHES")
        print("\n Este sistema cuenta con seis categorías principales:\n1. Productos \n2. Bodega \n3. Entradas \n4. Salidas \n5. Devoluciones \n6. Control ")
        print("\nA continuación se presentan las acciones que se pueden llevar a cabo en cada una de las categorías: ")
        print("\nCategoria Productos \n1. Imprimir características de todos los productos \n2. Imprimir características de un solo producto")
        print("\nCategoria Bodega \n1. Imprimir información e historial de movimientos de todos los productos en bodega \n2. Imprimir información e historial de movimientos de un producto específico en bodega \n3. Crear archivo de la información e historial de movimientos de todos los productos en bodega \n4. Eliminar todo el historial de movimientos de todos los productos en bodega")
        print("\nCategoría Entradas \n1. Registrar entrada de un producto a bodega  \n2. Eliminar el registro de una entrada  \n3. Imprimir historial de entradas \n4. Crear archivo del historial de entradas ")
        print("\nCategoría Salidas \n1. Registrar salida de un producto  \n2. Eliminar el registro de una salida  \n3. Imprimir historial de salidas \n4. Crear archivo del historial de salidas")
        print("\nCategoría Devoluciones \n1. Registrar devolución de un producto  \n2. Eliminar el registro de una devolución  \n3. Imprimir historial de devoluciones \n4. Crear archivo del historial de devoluciones")
        print("\nCategoría Control \n1. Hacer control extracontable de todo el inventario \n2. Hacer control extracontable de un solo producto")
        print("\nEste sistema se maneja por medio de la consola, al hacer uso de este debe verificar con cuidado que los números y datos que ingresa son los correctos.")
        
    def menu(self):
        while True:
            print("\nSistema de gestión de inventario de la bodega de NOTCLOTHES")
            seleccion_categoria=int(input("\nIngrese el número correspondiente a la categoría a la que desea acceder: \n1. Explicación uso del sistema \n2. Productos \n3. Bodega \n4. Entradas \n5. Salidas \n6. Devoluciones \n7. Control \n8. Salir \nNúmero: "))
            if seleccion_categoria not in range(1,9):
                print("El número ingresado no es válido. Intente nuevamente.")
                continue
            if seleccion_categoria==1:
                print("\nExplicación del uso del sistema")
                self.mostrar_instructivo()
                salir=input("Presione enter para salir ")
            if seleccion_categoria==2:
                while True:
                    print("\nProductos")
                    seleccion_accion=int(input("\nIngrese el número correspondiente a la acción que desea ejecutar: \n1. Imprimir características de todos los productos \n2. Imprimir características de un solo producto \n3. Acceder al instructivo \n4. Salir \nNúmero: "))
                    if seleccion_accion not in range(1,5):
                        print("El número ingresado no es válido. Intente nuevamente.")
                        continue
                    if seleccion_accion==1:
                        print("\nImprimir características de todos los productos")
                        self.imprimir_caracteristicas_productos_bodega()
                        salir=input("\nPresione enter para salir ")
                    if seleccion_accion==2:
                        print("\nImprimir características de un solo producto")
                        self.imprimir_caracteristicas_producto_especifico()
                        salir=input("\nPresione enter para salir ")
                    if seleccion_accion==3:
                        print("\nAcceder al instructivo")
                        self.mostrar_instructivo()
                        salir=input("Presione enter para  salir ")
                    if seleccion_accion==4:
                        break
            if seleccion_categoria==3:
                while True:
                    print("\nBodega")
                    seleccion_accion=int(input("\nIngrese el número correspondiente a la acción que desea ejecutar: \n1. Imprimir información e historial de movimientos de todos los productos en bodega \n2. Imprimir información e historial de movimientos de un producto específico en bodega \n3. Crear archivo de la información e historial de movimientos de todos los productos en bodega \n4. Eliminar todo el historial de movimientos de todos los productos en bodega \n5. Acceder al instructivo \n6. Salir \nNúmero: "))
                    if seleccion_accion not in range(1,7):
                        print("El número ingresado no es válido. Intente nuevamente.")
                        continue
                    if seleccion_accion==1:
                        print("\nImprimir información e historial de movimientos de todos los productos en bodega")
                        self.imprimir_productos_bodega()
                        salir=input("\nPresione enter para salir ")
                    if seleccion_accion==2:
                        print("\nImprimir información e historial de movimientos de un producto específico en bodega")
                        self.imprimir_producto_especifico_bodega()
                        salir=input("\nPresione enter para  salir ")
                    if seleccion_accion==3:
                        print("\nCrear archivo de la información e historial de movimientos de todos los productos en bodega")
                        self.crear_archivo_productos_bodega()
                        salir=input("Presione enter para salir ")
                    if seleccion_accion==4:
                        print("\nEliminar todo el historial de movimientos de todos los productos en bodega ")
                        self.eliminar_todos_los_registros_de_movimientos()
                        self.guardar_informacion()
                        salir=input("Presione enter para  salir ")
                    if seleccion_accion==5:
                        print("\nAcceder al instructivo")
                        self.mostrar_instructivo()
                        salir=input("Presione enter para  salir ")
                    if seleccion_accion==6:
                        break
            if seleccion_categoria==4:
                while True:
                    print("\nEntradas")
                    seleccion_accion=int(input("\nIngrese el número correspondiente a la acción que desea ejecutar: \n1. Registrar entrada de un producto a bodega  \n2. Eliminar el registro de una entrada  \n3. Imprimir historial de entradas \n4. Crear archivo del historial de entradas \n5. Acceder al instructivo \n6. Salir \nNúmero: "))
                    if seleccion_accion not in range(1,7):
                        print("El número ingresado no es válido. Intente nuevamente.")
                        continue
                    if seleccion_accion==1:
                        while True:
                            print("\nRegistrar entrada de un producto a bodega")
                            self.registrar_entrada_producto()
                            self.guardar_informacion()
                            siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Registrar otra entrada a bodega \n2. Salir \nNúmero: "))
                            if siguiente_paso not in range(1,3):
                                while True:
                                    print("El número ingresado no es válido. Intente nuevamente.")
                                    siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Registrar otra entrada a bodega \n2. Salir \nNúmero: "))
                                    if siguiente_paso in range(1,3):
                                        break
                            if siguiente_paso==1:
                                continue
                            if siguiente_paso==2:
                                break
                    if seleccion_accion==2:
                        while True:
                            print("\nEliminar el registro de una entrada ")
                            if len(self.entradas)==0:
                                print("Ninguna entrada a la bodega ha sido registrada.")
                            else:
                                print("\nA continuación se muestran todas las entradas a bodega, ubique el número de registro que desea eliminar.")
                                self.imprimir_entradas_bodega()
                                self.eliminar_registro_entrada()
                                self.guardar_informacion()
                            siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Eliminar el registro de otra entrada \n2. Salir \nNúmero: "))
                            if siguiente_paso not in range(1,3):
                                while True:
                                    print("El número ingresado no es válido. Intente nuevamente.")
                                    siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Eliminar el registro de otra entrada \n2. Salir \nNúmero: "))
                                    if siguiente_paso in range(1,3):
                                        break
                            if siguiente_paso==1:
                                continue
                            if siguiente_paso==2:
                                break
                    if seleccion_accion==3:
                        print("\nImprimir historial de entradas")
                        self.imprimir_entradas_bodega()
                        salir=input("\nPresione enter para salir ")
                    if seleccion_accion==4:
                        print("\nCrear archivo del historial de entradas ")
                        self.crear_archivo_entradas_bodega()
                        salir=input("Presione enter para salir ")
                    if seleccion_accion==5:
                        print("\nAcceder al instructivo")
                        self.mostrar_instructivo()
                        salir=input("Presione enter para  salir ")
                    if seleccion_accion==6:
                        break
            if seleccion_categoria==5:
                while True:
                    print("\nSalidas")
                    seleccion_accion=int(input("\nIngrese el número correspondiente a la acción que desea ejecutar: \n1. Registrar salida de un producto  \n2. Eliminar el registro de una salida  \n3. Imprimir historial de salidas \n4. Crear archivo del historial de salidas \n5. Acceder al instructivo \n6. Salir \nNúmero: "))
                    if seleccion_accion not in range(1,7):
                        print("El número ingresado no es válido. Intente nuevamente.")
                        continue
                    if seleccion_accion==1:
                        while True:
                            print("\nRegistrar salida de un producto")
                            self.registrar_salida_producto()
                            self.guardar_informacion()
                            siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Registrar otra salida \n2. Salir \nNúmero: "))
                            if siguiente_paso not in range(1,3):
                                while True:
                                    print("El número ingresado no es válido. Intente nuevamente.")
                                    siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Registrar otra salida \n2. Salir \nNúmero: "))
                                    if siguiente_paso in range(1,3):
                                        break
                            if siguiente_paso==1:
                                continue
                            if siguiente_paso==2:
                                break
                    if seleccion_accion==2:
                        while True:
                            print("\nEliminar el registro de una salida ")
                            if len(self.salidas)==0:
                                print("Ninguna salida de bodega ha sido registrada")
                            else:
                                print("\nA continuación se muestran todas las salidas, ubique el número de registro que desea eliminar.")
                                self.imprimir_salidas_bodega()
                                self.eliminar_registro_salida()
                                self.guardar_informacion()
                            siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Eliminar el registro de otra salida \n2. Salir \nNúmero: "))
                            if siguiente_paso not in range(1,3):
                                while True:
                                    print("El número ingresado no es válido. Intente nuevamente.")
                                    siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Eliminar el registro de otra salida \n2. Salir \nNúmero: "))
                                    if siguiente_paso in range(1,3):
                                        break
                            if siguiente_paso==1:
                                continue
                            if siguiente_paso==2:
                                break
                    if seleccion_accion==3:
                        print("\nImprimir historial de salidas")
                        self.imprimir_salidas_bodega()
                        salir=input("\nPresione enter para salir ")
                    if seleccion_accion==4:
                        print("\nCrear archivo del historial de salidas ")
                        self.crear_archivo_salidas_bodega()
                        salir=input("Presione enter para salir ")
                    if seleccion_accion==5:
                        print("\nAcceder al instructivo")
                        self.mostrar_instructivo()
                        salir=input("Presione enter para  salir ")
                    if seleccion_accion==6:
                        break
            if seleccion_categoria==6:
                while True:
                    print("\nDevoluciones")
                    seleccion_accion=int(input("\nIngrese el número correspondiente a la acción que desea ejecutar: \n1. Registrar devolución de un producto  \n2. Eliminar el registro de una devolución  \n3. Imprimir historial de devoluciones \n4. Crear archivo del historial de devoluciones \n5. Acceder al instructivo \n6. Salir \nNúmero: "))
                    if seleccion_accion not in range(1,7):
                        print("El número ingresado no es válido. Intente nuevamente.")
                        continue
                    if seleccion_accion==1:
                        while True:
                            print("\nRegistrar devolución de un producto")
                            self.registrar_devolucion_producto()
                            self.guardar_informacion()
                            siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Registrar otra devolución \n2. Salir \nNúmero: "))
                            if siguiente_paso not in range(1,3):
                                while True:
                                    print("El número ingresado no es válido. Intente nuevamente.")
                                    siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Registrar otra devolución \n2. Salir \nNúmero: "))
                                    if siguiente_paso in range(1,3):
                                        break
                            if siguiente_paso==1:
                                continue
                            if siguiente_paso==2:
                                break
                    if seleccion_accion==2:
                        while True:
                            print("\nEliminar el registro de una devolución ")
                            if len(self.devoluciones)==0:
                                print("Ninguna devolución a bodega ha sido registrada")
                            else:
                                print("\nA continuación se muestran todas las devoluciones, ubique el número de registro que desea eliminar.")
                                self.imprimir_devoluciones_bodega()
                                self.eliminar_registro_devolucion()
                                self.guardar_informacion()
                            siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Eliminar el registro de otra devolución \n2. Salir \nNúmero: "))
                            if siguiente_paso not in range(1,3):
                                while True:
                                    print("El número ingresado no es válido. Intente nuevamente.")
                                    siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Eliminar el registro de otra devolución \n2. Salir \nNúmero: "))
                                    if siguiente_paso in range(1,3):
                                        break
                            if siguiente_paso==1:
                                continue
                            if siguiente_paso==2:
                                break
                    if seleccion_accion==3:
                        print("\nImprimir historial de devoluciones")
                        self.imprimir_devoluciones_bodega()
                        salir=input("\nPresione enter para salir ")
                    if seleccion_accion==4:
                        print("\nCrear archivo del historial de devoluciones ")
                        self.crear_archivo_devoluciones_bodega()
                        salir=input("Presione enter para salir ")
                    if seleccion_accion==5:
                        print("\nAcceder al instructivo")
                        self.mostrar_instructivo()
                        salir=input("Presione enter para  salir ")
                    if seleccion_accion==6:
                        break
            if seleccion_categoria==7:
                while True:
                    print("\nControl")
                    seleccion_accion=int(input("\nIngrese el número correspondiente a la acción que desea ejecutar: \n1. Realizar el control extracontable de todo el inventario \n2. Realizar el control extracontable de un solo producto \n3. Acceder al instructivo \n4. Salir \nNúmero: "))
                    if seleccion_accion not in range(1,5):
                        print("El número ingresado no es válido. Intente nuevamente.")
                        continue
                    if seleccion_accion==1:
                        while True:
                            print("\nRealizar el control extracontable de todo el inventario")
                            self.control(1)
                            siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Hacer otro control extracontable \n2. Salir \nNúmero: "))
                            if siguiente_paso not in range(1,3):
                                while True:
                                    print("El número ingresado no es válido. Intente nuevamente.")
                                    siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Hacer otro control extracontable \n2. Salir \nNúmero: "))
                                    if siguiente_paso in range(1,3):
                                        break
                            if siguiente_paso==1:
                                continue
                            if siguiente_paso==2:
                                break
                    if seleccion_accion==2:
                        while True:
                            print("\nRealizar el control extracontable de un solo producto")
                            self.control(2)
                            siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Hacer otro control extracontable \n2. Salir \nNúmero: "))
                            if siguiente_paso not in range(1,3):
                                while True:
                                    print("El número ingresado no es válido. Intente nuevamente.")
                                    siguiente_paso=int(input("\nIngrese el número correspondiente a lo que desea hacer a continuación: \n1. Hacer otro control extracontable \n2. Salir \nNúmero: "))
                                    if siguiente_paso in range(1,3):
                                        break
                            if siguiente_paso==1:
                                continue
                            if siguiente_paso==2:
                                break
                    if seleccion_accion==3:
                        print("\nAcceder al instructivo")
                        self.mostrar_instructivo()
                        salir=input("Presione enter para  salir ")
                    if seleccion_accion==4:
                        break
            if seleccion_categoria == 8:
                print("Se ha cerrado el sistema de gestión de inventario.")
                break


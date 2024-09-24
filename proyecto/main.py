import paquete.bodega as bodega


def main():
    try:
        shirt=bodega.Producto("20-01", "SHIRT", 200, "negro","xs", "algodón")
        pants= bodega.Producto("20-02", "PANTS", 900, "negro","s", "algodón")
        dress= bodega.Producto("20-03", "DRESS", 1200, "negro","m", "algodón")
        jacket= bodega.Producto("20-04", "JACKET", 2200, "negro","xl", "cuero")
        skirt= bodega.Producto("20-05", "SKIRT", 400, "negro","s", "algodón")

        inventario_bodega=bodega.Bodega(shirt, pants, dress, jacket, skirt)

        inventario_bodega.menu()

    except ValueError:
        print("Error: se introdujo un dato que no es valido. Se reiniciará el sistema")
        inventario_bodega.menu()
if __name__=="__main__":
    main()

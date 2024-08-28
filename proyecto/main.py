import paquete.bodega as bodega

def main():
    shirt=bodega.Producto("20-01", "SHIRT", 200)
    pants=bodega.Producto("20-02", "PANTS", 900)
    dress=bodega.Producto("20-03", "DRESS", 1200)
    jacket=bodega.Producto("20-04", "JACKET", 2200)
    skirt=bodega.Producto("20-05", "SKIRT", 400)
    shorts=bodega.Producto("20-06", "SHORTS", 100)
    sweater=bodega.Producto("20-07", "SWEATER", 900)
    blouse=bodega.Producto("20-08", "BLOUSE", 400)
    tshirt=bodega.Producto("20-09", "T-SHIRT", 400)
    coat=bodega.Producto("20-10","COAT",1200)
    jeans=bodega.Producto("20-11", "JEANS", 200)
    hoodie=bodega.Producto("20-12", "HOODIE", 500)
    suit=bodega.Producto("20-13", "SUIT", 3200)
    tracksuit=bodega.Producto("20-14", "TRACKSUIR", 3200)
    sportswear=bodega.Producto("20-15", "SPORTSWEAR", 200)
    footwear=bodega.Producto("20-16","FOOTWEAR",4200)
    underwear=bodega.Producto("20-17", "UNDERWEAR", 100)
    bag=bodega.Producto("20-18", "BAG", 1000)
    jewelry=bodega.Producto("20-19", "JEWELRY", 3200)
    hat=bodega.Producto("20-20", "HAT", 1200)

    productos_en_bodega=bodega.Bodega(shirt, pants, dress, jacket, skirt)
    productos_en_bodega.registrar_entrada_producto("20-01", "28/08/2024", 1000)
    productos_en_bodega.registrar_salida_producto("20-01","28/08/2024",500)
    productos_en_bodega.imprimir_entradas_bodega()
    productos_en_bodega.imprimir_salidas_bodega()
    productos_en_bodega.imprimir_productos_bodega()
    productos_en_bodega.imprimir_producto_especifico_bodega(shirt)

if __name__=="__main__":
    main()

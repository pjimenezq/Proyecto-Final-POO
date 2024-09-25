import paquete.bodega as bodega

def main():
    try:
        PanaSHIRT=bodega.Producto("20-01", "PanaSHIRT", 200, "negro","unica", "seda")
        MilkSHIRT= bodega.Producto("20-02", "MilkSHIRT", 900, "blanco","unica", "seda")
        SkySHIRT= bodega.Producto("20-03", "SkySHIRT", 1200, "gris","unica", "seda")
        DirtySHIRT= bodega.Producto("20-04", "DirtySHIRT", 2200, "beige","unica", "seda")
        NoSHIRT= bodega.Producto("20-05", "NoSHIRT", 400, "transparente","unica", "plastico")
        CargoPANTS=bodega.Producto("19-01", "CargoPANTS", 100, "negro","unica", "algodon")
        NcPANTS= bodega.Producto("19-02", "NCPANTS", 900, "negro","unica", "algodon")
        WidePANTS= bodega.Producto("19-03", "WidePANTS", 400, "negro","unica", "algodon")
        XassPANTS= bodega.Producto("19-04", "XassPANTS", 400, "negro","unica", "algodon")
        DadPANTS= bodega.Producto("19-05", "DadPANTS", 1200, "negro","unica", "cuero")
        SmgsSHOES=bodega.Producto("18-01", "SmgsSHOES", 200, "negro","unica", "cuero")
        HotSHOES= bodega.Producto("18-02", "HotSHOES", 500, "negro","unica", "cuero")
        TracktorSHOES= bodega.Producto("18-03", "TracktorSHOES", 3200, "negro","unica", "cuero")
        AdSHOES= bodega.Producto("18-04", "AdSHOES", 3200, "negro","unica", "cuero")
        NotSHOES= bodega.Producto("18-05", "NotSHOES", 1300, "negro","unica", "cuero")
        CandyNECKLACE=bodega.Producto("17-01", "CandyNECKLACE", 200, "blanco","unica", "plata")
        BulletsNECKLACE= bodega.Producto("17-02", "BulletsNECKLACE", 100, "gris","unica", "titanio")
        NoNECKLACE= bodega.Producto("17-03", "NoNECKLACE", 1000, "plata","unica", "plata")
        MercuryNECKLACE= bodega.Producto("17-04", "MercuryNECKLACE", 3200, "negro","unica", "mercurio")
        SilverNECKLACE= bodega.Producto("17-05", "SilverNECKLACE", 1200, "plata","unica", "plata")

        inventario_bodega=bodega.Bodega(PanaSHIRT, MilkSHIRT, SkySHIRT, DirtySHIRT, NoSHIRT, CargoPANTS, NcPANTS, WidePANTS, XassPANTS, DadPANTS, SmgsSHOES, HotSHOES, TracktorSHOES, AdSHOES, NotSHOES, CandyNECKLACE, BulletsNECKLACE, NoNECKLACE, MercuryNECKLACE, SilverNECKLACE)


        inventario_bodega.menu()

    except ValueError:
        print("Error: se introdujo un dato que no es valido. Se reiniciará el sistema")
        inventario_bodega.menu()
        
if __name__=="__main__":
    main()

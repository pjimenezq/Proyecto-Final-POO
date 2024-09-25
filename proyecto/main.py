import mi_paquete.bodega as bodega

def main():
    try:
        PanaSHIRT=bodega.Producto("20-01", "PanaSHIRT", 200, "negro","xs", "algodón")
        MilkSHIRT= bodega.Producto("20-02", "MilkSHIRT", 900, "negro","s", "algodón")
        SkySHIRT= bodega.Producto("20-03", "SkySHIRT", 1200, "negro","m", "algodón")
        DirtySHIRT= bodega.Producto("20-04", "DirtySHIRT", 2200, "negro","xl", "cuero")
        NoSHIRT= bodega.Producto("20-05", "NoSHIRT", 400, "negro","s", "algodón")
        CargoPANTS=bodega.Producto("19-01", "CargoPANTS", 200, "negro","xs", "algodón")
        NCPANTS= bodega.Producto("19-02", "NCPANTS", 900, "negro","s", "algodón")
        WidePANTS= bodega.Producto("19-03", "WidePANTS", 1200, "negro","m", "algodón")
        XassPANTS= bodega.Producto("19-04", "XassPANTS", 2200, "negro","xl", "cuero")
        DadPANTS= bodega.Producto("19-05", "DadPANTS", 400, "negro","s", "algodón")
        SmgsSHOES=bodega.Producto("18-01", "SmgsSHOES", 200, "negro","xs", "algodón")
        HotSHOES= bodega.Producto("18-02", "HotSHOES", 900, "negro","s", "algodón")
        TracktorSHOES= bodega.Producto("18-03", "TracktorSHOES", 1200, "negro","m", "algodón")
        AdSHOES= bodega.Producto("18-04", "AdSHOES", 2200, "negro","xl", "cuero")
        NotSHOES= bodega.Producto("18-05", "NotSHOES", 400, "negro","s", "algodón")
        CandyNECKLACE=bodega.Producto("17-01", "CandyNECKLACE", 200, "negro","xs", "algodón")
        BulletsNECKLACE= bodega.Producto("17-02", "BulletsNECKLACE", 900, "negro","s", "algodón")
        NoNECKLACE= bodega.Producto("17-03", "NoNECKLACE", 1200, "negro","m", "algodón")
        MercuryNECKLACE= bodega.Producto("17-04", "MercuryNECKLACE", 2200, "negro","xl", "cuero")
        SilverNECKLACE= bodega.Producto("17-05", "SilverNECKLACE", 400, "negro","s", "algodón")

        inventario_bodega=bodega.Bodega(PanaSHIRT, MilkSHIRT, SkySHIRT, DirtySHIRT, NoSHIRT,
            CargoPANTS, NCPANTS, WidePANTS, XassPANTS, DadPANTS, SmgsSHOES, HotSHOES, TracktorSHOES, AdSHOES, NotSHOES,
            CandyNECKLACE, BulletsNECKLACE, NoNECKLACE, MercuryNECKLACE, SilverNECKLACE)

        inventario_bodega.menu()
    except ValueError:
        print("Error: se introdujo un dato que no es valido. Se reiniciará el sistema")
        inventario_bodega.menu()
if __name__=="__main__":
    main()

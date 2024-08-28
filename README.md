# NOTCLOTHES - Proyecto final POO
**Nombre del grupo:**

**Integrantes:**
* Paula Jiménez Quiñones
* Jhon Alejandro Ramirez Diaz
* Sara Sofía Gómez Suárez

## Definición alternativa
### Alternativa 1
Construir una aplicación que emule un sistema de gestión de inventario para una bodega utilizando _Python_.

Condiciones:
+ Código original
+ Uso de herramientas vistas en el curso
+ Interacción y manejo a trabés de la consola
  
Operaciones:
+ Crear objeto a almacenar (+20 objetos, con distintos atributos)
+ Registro de entrada y salida
+ Método para obtener listado de inventario actual
+ Manejo de fechas en los registros
## Cómo se abordo el problema
### Sistema de gestión de inventario
En primer lugar, se hizo una investigación sobre el problema planteado. Este paso es muy importante para definir con claridad el problema y diseñar con mayor precisión los diagramas de clase.

Se investigó sobre lo que es una sistema de gestión de inventario y la forma en la que funciona. El entender este concepto del mundo real facilitó e hizo más eficiente el proceso de abstraer sus características principales, para luego representarlas gráficamente mediante clases, objetos y sus relaciones.

De este paso se obtuvo que un sistema de gestión de inventario es....AQUÍ VA LA DEFINICIÓN
### Empresa
En segundo lugar, se creó el escenario en el que se haría uso del sistema de gestión de inventario. Por lo tanto se ideó una empresa, se pensó en sus características principales y en el tipo de productos que vende.

Es asi como creamos **NOTCLOTHES**

En NotClothes, nos dedicamos a redefinir la alta costura y moda a través de un enfoque sostenible y centrado en el bienestar de nuestros clientes. Nuestro objetivo es crear prendas de diseño exclusivo y alta calidad en sus materiales que no solo realcen la belleza y la elegancia, sino que también promuevan la comodidad, las distintas perspectivas de genero  y el respeto por el medio ambiente 

### Productos
El tercer paso consistió en determinar cada uno de los productos que la empresa maneja y especificar sus atributos (código, costo, AQUI SE ESCRIBE LA LISTA DE LOS OTROS ATRIBUTOS)

En la siguiente tabla se muestra el resultado de este paso.

||Producto|Código|OTROS ATRIBUTOS|Costo|
|---|-----------------|------|-------------------------|--------|
|1|NOMBRE PRODUCTO|CODIGO|CARACTERISTICAS|PRECIO|
|2|||||
|3|||||
|4|||||
|5|||||
|6|||||
|7|||||
|8|||||
|9|||||
|10|||||
|11|||||
|12|||||
|13|||||
|14|||||
|15|||||
|16|||||
|17|||||
|18|||||
|19|||||
|20|||||

### Diagramas de clase
Habiendo entendido la forma en la que funciona un sistema de gestión de inventario y habiendo definido el uso específico que se le va a dar a este en el proyecto, el cuarto paso consistió en modelar, mediante diagramas de clase, las clases, los objetos y sus relaciones.

[![](https://mermaid.ink/img/pako:eNqlVtuO2jAQ_ZUoT61YfgBVlRbQLkLtijas-sLLNBnAwomR4-yKpvvv9QVyIeM1q_LEzInPmbFnPK7jVGQYT-KUQ1nOGewk5Jsi0r-VFFmVqujL3_E4SvZMKsK_gkKVhH8usaT8S0gPSBElB1og2QtJKiSvCAolgUy5qEokgLXNIiKQmQDSv0QoKPGFEBmjJJKKkURrqRMvNUitOZoUdTpUMg9CKA_0XGQoPdgUdmQ6r8jliUoIdGTObyvhgtbOF0Xjn7hFiUWK0Xj8NWKFapAnyJ2zVLJxTiUU2cC7kuxMsOUCWopEifTwo9LFxNRpIDATXMgBV8L-DGW_m5pgwK-B0Qx4WnGNzlmZiqpQnz73Yxg9HzMN20g01tEfPaKaowLGSw00pG_d7bKV1W5WwhFf8BsWu70axPjAhj6dIge5Ph2blKKuvKVvY-h_0gvENmQbyC9gperSdrb8xAdeo2UZevlSOrbBWx1revJN9nAkleyi0M66G6NVcjaVkqFc3hs0GL29bTrHZUxP9N4dtOdy6J2LrzZMf__XmViKoI67EW-swidMD960HFNI0F20dZCSqngj49aHVNZXvfVRlfVV89AqZgLUnXaEq3po2zHSnAYPFpkdHrccuydwuz4Ut5tErYqxSZGVeK9vHE24b_QE69SXtj6SkPk-KNFMypqi692KzafBzmgmbEt6nyr2oqeNtweaNcGQLzO6Hs6m7hjTTYykmqmoC0dQrJn6rVrjIg_D1t1vPY19mTbLg9r6VdGqasPHqKEbusO-RToXu3OQOTxiXipRoHdAnhcHVRfdLteGl3ABZFXFd3GOMgeW6TezZdrEao85buKJ_pvhFiquNvGmMJ9CpURyKtJ4omSFd3FlnxjnV7Zzvv0DH0d9QQ?type=png)](https://mermaid.live/edit#pako:eNqlVtuO2jAQ_ZUoT61YfgBVlRbQLkLtijas-sLLNBnAwomR4-yKpvvv9QVyIeM1q_LEzInPmbFnPK7jVGQYT-KUQ1nOGewk5Jsi0r-VFFmVqujL3_E4SvZMKsK_gkKVhH8usaT8S0gPSBElB1og2QtJKiSvCAolgUy5qEokgLXNIiKQmQDSv0QoKPGFEBmjJJKKkURrqRMvNUitOZoUdTpUMg9CKA_0XGQoPdgUdmQ6r8jliUoIdGTObyvhgtbOF0Xjn7hFiUWK0Xj8NWKFapAnyJ2zVLJxTiUU2cC7kuxMsOUCWopEifTwo9LFxNRpIDATXMgBV8L-DGW_m5pgwK-B0Qx4WnGNzlmZiqpQnz73Yxg9HzMN20g01tEfPaKaowLGSw00pG_d7bKV1W5WwhFf8BsWu70axPjAhj6dIge5Ph2blKKuvKVvY-h_0gvENmQbyC9gperSdrb8xAdeo2UZevlSOrbBWx1revJN9nAkleyi0M66G6NVcjaVkqFc3hs0GL29bTrHZUxP9N4dtOdy6J2LrzZMf__XmViKoI67EW-swidMD960HFNI0F20dZCSqngj49aHVNZXvfVRlfVV89AqZgLUnXaEq3po2zHSnAYPFpkdHrccuydwuz4Ut5tErYqxSZGVeK9vHE24b_QE69SXtj6SkPk-KNFMypqi692KzafBzmgmbEt6nyr2oqeNtweaNcGQLzO6Hs6m7hjTTYykmqmoC0dQrJn6rVrjIg_D1t1vPY19mTbLg9r6VdGqasPHqKEbusO-RToXu3OQOTxiXipRoHdAnhcHVRfdLteGl3ABZFXFd3GOMgeW6TezZdrEao85buKJ_pvhFiquNvGmMJ9CpURyKtJ4omSFd3FlnxjnV7Zzvv0DH0d9QQ)

Para una mejor visualización: https://www.mermaidchart.com/raw/f10fee59-590a-438b-94d8-877d5570daf4?theme=light&version=v0.1&format=svg

AQUI VAN LOS DIAGRAMAS Y SI ES NECESARIO SU EXPLICACIÓN
### Código
Para finalizar, teniendo en cuenta los diagramas de clase creados anteriormente, se realizó el código en python que emula el sistema de gestión de inventario para una bodega de la empresa creada.

AQUI VA EL CÓDIGO
## Solución y la explicación
AQUI SE EXPLICA EL CÓDIGO
## Cómo instalar y usar el desarrollo
## Rquerimientos para crear un entorno virtual
## Conclusiones

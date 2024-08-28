# NOTCLOTHES - Proyecto final POO
**Nombre del grupo:** );

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
+ Interacción y manejo a través de la consola
  
Operaciones:
+ Crear objeto a almacenar (+20 objetos, con distintos atributos)
+ Registro de entrada y salida
+ Método para obtener listado de inventario actual
+ Manejo de fechas en los registros
## Cómo se abordo el problema
### Sistema de gestión de inventario
En primer lugar, se hizo una investigación sobre el problema planteado. Este paso es muy importante para definir con claridad el problema y diseñar con mayor precisión los diagramas de clase.

Se investigó sobre lo que es una sistema de gestión de inventario y la forma en la que funciona. El entender este concepto del mundo real facilitó e hizo más eficiente el proceso de abstraer sus características principales, para luego representarlas gráficamente mediante clases, objetos y sus relaciones.


De acuerdo con Gabriel Baca (2014) en su libro _Introducción a la Ingenieria Industrial_, **el inventario** consiste en la acumulación de diversos artículos, materiales o productos que tienen valor y utilidad para una empresa. Estos materiales pueden ser utilizados como insumos (materias primas) para la producción de otros productos; también pueden ser productos intermedios (que están en proceso de transformación y serán trasladados a la siguiente etapa del proceso productivo), o productos terminados (que han completado el proceso productivo y están listos para ser enviados al cliente).

Sobre este contexto se entiende el **Sistema de Gestión de Inventario** como la acumulación y administración de artículos, materiales o productos que representan valor y utilidad para una empresa. El propósito de administrar el inventario de una empresa surge como forma de combatir la incertidumbre en la demanda y el suministro, asegurando que la empresa tenga los materiales necesarios para la producción y pueda satisfacer las necesidades de los clientes.

Por otro lado, el hecho de establecer un sistema de gestión de inventario implica algunos aspectos fundamentales como, el uso de **revisiones continuas**, reducción de niveles de inventario de seguridad, y métodos cuantitativos para equilibrar costos y niveles de servicio, asimismo formular un **conjunto de políticas y controles** que determinan las cantidades adecuadas de inventario, el tamaño de los pedidos y la frecuencia de compra y finalmente es importante mencionar que el hecho de mantener inventarios implica **riesgos** como obsolescencia, deterioro y costos de almacenamiento, de aqui la importancia de incluir costos de mantenimiento, pedidos y penalización.


### Empresa
En segundo lugar, se creó el escenario en el que se haría uso del sistema de gestión de inventario. Por lo tanto se ideó una empresa, se pensó en sus características principales y en el tipo de productos que vende.

Es así como creamos **NOTCLOTHES**.

En NotClothes, nos dedicamos a redefinir la alta costura y moda a través de un enfoque sostenible y centrado en el bienestar de nuestros clientes. Nuestro objetivo es crear prendas de diseño exclusivo y alta calidad en sus materiales que no solo realcen la belleza y la elegancia, sino que también promuevan la comodidad, las distintas perspectivas de género  y el respeto por el medio ambiente.

**MÉTRICAS** 

NOTCLOTHES, en su primer año de operaciones, generó ingresos por $4  millones USD, con un margen de beneficio bruto del 60% y una tasa de conversión del 3.5%. Con un valor promedio de pedido de $350 USD, ha capturado un 5% del mercado de alta costura sostenible en América Latina y mantiene una tasa de retención de clientes del 70%. **Su inventario rotativo** de 10,000 unidades tiene un ciclo de rotación de 90 días, y el coste de adquisición de clientes es de $50 USD. La tasa de devoluciones es del 5%, y cuenta con una comunidad activa de 500,000 seguidores en Instagram y 200,000 en TikTok. La base de clientes crece un 30% trimestre a trimestre, con un NPS de 85. Las ventas internacionales representan un 40% de los ingresos totales, NotClothes introduce 5 nuevos productos cada trimestre y ha reducido los costos operativos en un 20%. Las ventas online crecen un 40% año tras año, y participa en 10 eventos de moda anualmente. Su programa de fidelización tiene una participación del 50%, y ha reducido su huella de carbono en un 30% mediante el uso de materiales reciclados y procesos sostenibles.

### Productos
El tercer paso consistió en determinar cada uno de los productos que la empresa maneja y especificar sus atributos (nombre del producto, referencia, marca, precio, color, talla y material)

En la siguiente tabla se muestra el resultado de este paso.

||Producto|Ref.|Marca|Precio|Color|Talla|Material|
|---|-----------------|------|---------|---------|--------|------|--------|
|1|Shirt|20-01|NOTCLOTHES|$200 USD|Negro|S-M-L|Poliéster|
|2|Pants|20-02|NOTCLOTHES|$900 USD|Negro|S-M-L|Poliéster|
|3|Dress|20-03|NOTCLOTHES|$1200 USD|Negro|S-M-L|Poliéster|
|4|Jacket|20-04|NOTCLOTHES|$2200 USD|Negro|S-M-L|Poliéster|
|5|Skirt|20-05|NOTCLOTHES|$400 USD|Negro|S-M-L|Poliéster|
|6|Shorts|20-06|NOTCLOTHES|$100 USD|Negro|S-M-L|Poliéster|
|7|Sweater|20-07|NOTCLOTHES|$900 USD|Negro|S-M-L|Poliéster|
|8|Blouse|20-08|NOTCLOTHES|$400 USD|Negro|S-M-L|Poliéster|
|9|T-Shirt|20-09|NOTCLOTHES|$400 USD|Negro|S-M-L|Poliéster|
|10|Coat|20-10|NOTCLOTHES|$1200 USD|Negro|S-M-L|Poliéster|
|11|Jeans|20-11|NOTCLOTHES|$200 USD|Negro|S-M-L|Poliéster|
|12|Hoodie|20-12|NOTCLOTHES|$500 USD|Negro|S-M-L|Poliéster|
|13|Suit|20-13|NOTCLOTHES|$3200 USD|Negro|S-M-L|Poliéster|
|14|Tracksuit|20-14|NOTCLOTHES|$3200 USD|Negro|S-M-L|Poliéster|
|15|Sportswear|20-15|NOTCLOTHES|$200 USD|Negro|S-M-L|Poliéster|
|16|Footwear|20-16|NOTCLOTHES|$4200 USD|Negro|S-M-L|Poliéster|
|17|Underwear|20-17|NOTCLOTHES|$100 USD|Negro|S-M-L|Poliéster|
|18|Bag|20-18|NOTCLOTHES|$1000 USD|Negro|S-M-L|Poliéster|
|19|Jewelry|20-19|NOTCLOTHES|$3200 USD|Negro|S-M-L|Poliéster|
|20|Hat|20-20|NOTCLOTHES|$1200 USD|Negro|S-M-L|Poliéster|

### Diagramas de clase
Habiendo entendido la forma en la que funciona un sistema de gestión de inventario y habiendo definido el uso específico que se le va a dar a este en el proyecto, el cuarto paso consistió en modelar, mediante diagramas de clase, las clases, los objetos y sus relaciones.

[![](https://mermaid.ink/img/pako:eNqlVtuO2jAQ_ZUoT61YfgBVlRbQLkLtijas-sLLNBnAwomR4-yKpvvv9QVyIeM1q_LEzInPmbFnPK7jVGQYT-KUQ1nOGewk5Jsi0r-VFFmVqujL3_E4SvZMKsK_gkKVhH8usaT8S0gPSBElB1og2QtJKiSvCAolgUy5qEokgLXNIiKQmQDSv0QoKPGFEBmjJJKKkURrqRMvNUitOZoUdTpUMg9CKA_0XGQoPdgUdmQ6r8jliUoIdGTObyvhgtbOF0Xjn7hFiUWK0Xj8NWKFapAnyJ2zVLJxTiUU2cC7kuxMsOUCWopEifTwo9LFxNRpIDATXMgBV8L-DGW_m5pgwK-B0Qx4WnGNzlmZiqpQnz73Yxg9HzMN20g01tEfPaKaowLGSw00pG_d7bKV1W5WwhFf8BsWu70axPjAhj6dIge5Ph2blKKuvKVvY-h_0gvENmQbyC9gperSdrb8xAdeo2UZevlSOrbBWx1revJN9nAkleyi0M66G6NVcjaVkqFc3hs0GL29bTrHZUxP9N4dtOdy6J2LrzZMf__XmViKoI67EW-swidMD960HFNI0F20dZCSqngj49aHVNZXvfVRlfVV89AqZgLUnXaEq3po2zHSnAYPFpkdHrccuydwuz4Ut5tErYqxSZGVeK9vHE24b_QE69SXtj6SkPk-KNFMypqi692KzafBzmgmbEt6nyr2oqeNtweaNcGQLzO6Hs6m7hjTTYykmqmoC0dQrJn6rVrjIg_D1t1vPY19mTbLg9r6VdGqasPHqKEbusO-RToXu3OQOTxiXipRoHdAnhcHVRfdLteGl3ABZFXFd3GOMgeW6TezZdrEao85buKJ_pvhFiquNvGmMJ9CpURyKtJ4omSFd3FlnxjnV7Zzvv0DH0d9QQ?type=png)](https://mermaid.live/edit#pako:eNqlVtuO2jAQ_ZUoT61YfgBVlRbQLkLtijas-sLLNBnAwomR4-yKpvvv9QVyIeM1q_LEzInPmbFnPK7jVGQYT-KUQ1nOGewk5Jsi0r-VFFmVqujL3_E4SvZMKsK_gkKVhH8usaT8S0gPSBElB1og2QtJKiSvCAolgUy5qEokgLXNIiKQmQDSv0QoKPGFEBmjJJKKkURrqRMvNUitOZoUdTpUMg9CKA_0XGQoPdgUdmQ6r8jliUoIdGTObyvhgtbOF0Xjn7hFiUWK0Xj8NWKFapAnyJ2zVLJxTiUU2cC7kuxMsOUCWopEifTwo9LFxNRpIDATXMgBV8L-DGW_m5pgwK-B0Qx4WnGNzlmZiqpQnz73Yxg9HzMN20g01tEfPaKaowLGSw00pG_d7bKV1W5WwhFf8BsWu70axPjAhj6dIge5Ph2blKKuvKVvY-h_0gvENmQbyC9gperSdrb8xAdeo2UZevlSOrbBWx1revJN9nAkleyi0M66G6NVcjaVkqFc3hs0GL29bTrHZUxP9N4dtOdy6J2LrzZMf__XmViKoI67EW-swidMD960HFNI0F20dZCSqngj49aHVNZXvfVRlfVV89AqZgLUnXaEq3po2zHSnAYPFpkdHrccuydwuz4Ut5tErYqxSZGVeK9vHE24b_QE69SXtj6SkPk-KNFMypqi692KzafBzmgmbEt6nyr2oqeNtweaNcGQLzO6Hs6m7hjTTYykmqmoC0dQrJn6rVrjIg_D1t1vPY19mTbLg9r6VdGqasPHqKEbusO-RToXu3OQOTxiXipRoHdAnhcHVRfdLteGl3ABZFXFd3GOMgeW6TezZdrEao85buKJ_pvhFiquNvGmMJ9CpURyKtJ4omSFd3FlnxjnV7Zzvv0DH0d9QQ)

Para una mejor visualización: https://www.mermaidchart.com/raw/f10fee59-590a-438b-94d8-877d5570daf4?theme=light&version=v0.1&format=svg

### Código
Para finalizar, teniendo en cuenta los diagramas de clase creados anteriormente, se realizó el código en python que emula el sistema de gestión de inventario para una bodega de la empresa creada.

AQUI VA EL CÓDIGO
## Solución y la explicación
AQUI SE EXPLICA EL CÓDIGO
## Cómo instalar y usar el desarrollo
## Rquerimientos para crear un entorno virtual
## Conclusiones
## Bibliografía
Baca Urbina, G., Cruz Valderrama, M., Cristóbal Vázquez, M. A., Baca Cruz, G., Gutiérrez Matus, J. C., Pacheco Espejel, A. A., Rivera González, Á. E., Rivera González, I. A., & Obregón Sánchez, M. G. (2014)Introducción a la Ingeniería Industrial (2ª ed.)1. Grupo Editorial Patria. ISBN 978-607-438-919-72.

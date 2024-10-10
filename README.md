***Conjunto de datos\***

Cuando configure su repositorio específico del proyecto, recibirá automáticamente el conjunto de datos para este proyecto.

Este proyecto tiene dos conjuntos de datos, uno donde los descuentos **no** se asignaron aleatoriamente y otro más pequeño donde el descuento se asignó aleatoriamente.

El primer archivo, `non_rand_discount.csv`, contiene datos históricos de una empresa de comercio electrónico. En este conjunto de datos, el descuento **no se asignó de forma aleatoria** . El segundo archivo, `random_data.csv`, contiene datos en los que el descuento se asignó de forma aleatoria. Debido a que los datos experimentales suelen ser difíciles de obtener cuando se realiza una inferencia causal en la industria, a menudo utilizamos datos no experimentales para estimar nuestros modelos (datos de entrenamiento) y guardamos todos los datos experimentales para fines de validación (datos de prueba).

Aquí se muestran todas las columnas y una breve descripción de lo que representan. Las `xm`columnas representan el gasto total en los últimos x meses para esa categoría.

- spend_1m_baby: gasto del último mes en la categoría bebé;
- spend_2m_baby: gasto de los últimos 2 meses en la categoría bebé;
- gasta_3m_bebe;
- gastar_4m_bebe;
- gastar_5m_bebe;
- gastar_6m_bebe;
- spend_1m_clothes: gasto del último mes en la categoría ropa;
- gastar_2m_ropa;
- gastar_3m_ropa;
- gastar_4m_ropa;
- gastar_5m_ropa;
- gastar_6m_ropa;
- gastar_1m_salud;
- gastar_2m_salud;
- gastar_3m_salud;
- gastar_4m_salud;
- gastar_5m_salud;
- gastar_6m_salud;
- gastar_1m_mascota;
- gastar_2m_mascota;
- gastar_3m_mascota;
- gastar_4m_mascota;
- gastar_5m_mascota;
- gastar_6m_mascota;
- gastar_1m_en_comestibles;
- gastar_2m_en_comestibles;
- gastar_3m_en_comestibles;
- gastar_4m_en comestibles;
- gastar_5m_en comestibles;
- gastar_6m_en comestibles;
- gastar_1m_eletronico;
- gastar_2m_eletronico;
- gastar_3m_eletronico;
- gastar_4m_eletronico;
- gastar_5m_eletronico;
- gastar_6m_eletronico;
- ventas: ventas a largo plazo de ese cliente; esta es una posible variable de resultado; no debe utilizarse como una característica;
- descuento: monto de descuento que se le otorga al cliente en el momento de unirse a la plataforma;
- beneficio: beneficio a largo plazo para ese cliente – el beneficio se da mediante la fórmula 5% ventas - descuento;
- edad: edad del cliente – autoinformada;
- género: género del cliente – autoinformado;
- cust_state: estado de la dirección del cliente (última dirección utilizada para la entrega); se proporciona en la etapa de incorporación del cliente;
- tenencia: tiempo desde que el cliente se unió a la plataforma en meses;
- sales_prediction_bins: discretización de la puntuación del modelo de aprendizaje automático;
- sales_prediction: puntuación del modelo de aprendizaje automático.

```
random_data.csv`no tiene las columnas `sales_prediction_bins`y `sales_prediction
```

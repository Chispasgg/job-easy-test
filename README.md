# Prueba de Codificación - Desarrollador Python

## Objetivo
Desarrollar un script en Python que se conecte a la API del archivo api.py, obtenga datos aleatorios, los almacene en una base de datos MongoDB y, por último, obtenga todos los datos almacenados en dicha base de datos y los muestre. El entorno de base de datos esta en Docker.

## Requerimientos

- Utilizar Python para realizar las solicitudes a la API.
- Obtener datos aleatorios, almacenar datos en la base de datos y consultar una base de datos MongoDB.
- Configurar un entorno de desarrollo utilizando Docker.
- Documentar el proceso de configuración y ejecución del script.

## Instrucciones

- Utilice la API aque genera el archivo api.py.
- La API tiene 2 metodos implementados que devuelven objetos JSON con información. Cada objeto tiene campos especificos.
- Extraiga los datos relevantes de la respuesta de la API y almacénelos en una colección en una base de datos MongoDB mediante la API.
- Generar un nuevo metodo GET para obtener todos los datos almacenados en la base de datos.
- Asegúrese de que el script pueda ejecutarse de forma independiente y sin errores.
- Proporcione instrucciones claras sobre cómo se ha levantado el entorno Docker y ejecutar el script.
- Documente cualquier suposición o decisión de diseño importante que haya tomado durante el desarrollo.

## Criterios de Evaluación

- Correcta conexión y obtención de datos desde la API.
- Almacenamiento adecuado de los datos en la base de datos MongoDB.
- Correcta configuración del entorno Docker.
- Claridad y precisión en la documentación proporcionada.
- Eficiencia y organización del código.

## Entrega
Envíe el código fuente junto con la documentación en archivo zip.

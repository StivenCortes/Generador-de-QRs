# Generador de Códigos QR

Este proyecto es una herramienta en Python para crear códigos QR a partir de URLs o texto plano y guardarlos como imágenes en el formato que el usuario elija.

Se utiliza la librería `qrcode` para generar el contenido visual del QR y `Pillow` para manejar la imagen resultante. Es una solución útil para compartir enlaces, mensajes, información breve o accesos rápidos de forma visual y práctica.

## ¿Qué problema resuelve?

La aplicación ayuda a:

- Generar códigos QR de manera rápida sin escribir lógica compleja.
- Convertir enlaces web o textos en imágenes QR listas para compartir.
- Guardar los archivos en el disco con nombres personalizados.
- Reutilizar una ruta de carpeta previamente seleccionada para crear varios QR en una sola sesión.
- Validar entradas del usuario para evitar errores comunes, como rutas vacías, extensiones no permitidas o nombres inválidos.

## ¿Cómo funciona?

El programa se ejecuta desde la terminal y ejecuta un flujo interactivo en consola:

1. Pide la cantidad de códigos QR que deseas crear.
2. Solicita el texto o la URL que se convertirá en QR.
3. Pide un nombre para el archivo con extensión `.png`, `.jpg` o `.jpeg`.
4. Solicita la carpeta donde se guardará la imagen.
5. Verifica si la ubicación existe y si el archivo ya existe.
6. Genera el QR y lo guarda en disco.
7. Pregunta si quiere abrir la imagen generada.
8. Repite el proceso hasta completar la cantidad pedida.

Además, incluye validaciones para evitar errores como:

- Valores vacíos.
- Números menores o iguales a cero.
- Extensiones no soportadas.
- Rutas inexistentes.
- Nombres de archivo sin extensión.
- Sobrescrituras accidentales.

## Dependencias

Necesitas tener Python instalado en tu equipo. En este proyecto también se incluye un archivo llamado `requirements.txt` con todas las librerías necesarias. Puedes instalar todo de forma fácil con este comando:

```bash
pip install -r requirements.txt
```

Si quieres ver qué contiene ese archivo, aquí está:

```txt
colorama==0.4.6
pillow==12.3.0
qrcode==8.2
```

También puedes instalar cada librería manualmente si prefieres:

```bash
pip install qrcode pillow colorama
```

## Guía de uso (sin conocimientos de programación)

Si no sabes mucho de programación, sigue estos pasos:

1. Descarga el proyecto: haz clic en el botón verde "Code" y luego en "Download ZIP".
2. Descomprime la carpeta en tu computadora.
3. Abre la carpeta del proyecto y busca el archivo `crear_qr.py`.
4. Abre ese archivo con VS Code o cualquier editor de Python.
5. En la terminal del proyecto, ejecuta esta instrucción para instalar lo necesario:

```bash
pip install -r requirements.txt
```

6. Luego ejecuta el programa con:

```bash
python crear_qr.py
```

7. Sigue las instrucciones de la consola:
   - cuántos QRs quieres crear,
   - la URL o el texto,
   - el nombre del archivo,
   - la carpeta donde se guardará.

8. Cuando termine, la imagen QR quedará guardada en la ruta que elegiste.

## Ejecución

Desde la carpeta del proyecto, ejecuta:

```bash
python crear_qr.py
```

Si el archivo principal tiene otro nombre dentro del proyecto, sustitúyelo por el correcto.

## Ejemplo de uso

El programa pedirá algo similar a esto:

```text
¿Cuántos códigos QR quieres hacer?: 2
Ingrese la URL o el texto que desea convertir en código QR: https://example.com
Ingrese el nombre del archivo QR (con extensión .png, .jpg, o .jpeg): ejemplo.png
Ingrese la ruta donde se guardará el QR: C:\Users\TuUsuario\Desktop
¿Quieres guardar esta ruta para usarla después? s/n: s
```

Y al finalizar generará la imagen con el contenido indicado.

## Funcionalidades principales

- Generación de QR desde texto o URL.
- Guardado en formato `.png`, `.jpg` o `.jpeg`.
- Validación de datos de entrada.
- Confirmación antes de reemplazar un archivo existente.
- Opción para reutilizar una carpeta previamente guardada.
- Apertura automática de la imagen al terminar cada QR.

## Librerías utilizadas

- `qrcode`: genera el código QR a partir del texto o URL.
- `Pillow`: permite procesar y guardar imágenes compatibles con `qrcode`.
- `pathlib`: facilita la manipulación segura de rutas de archivo y directorios.

## Estructura del proyecto

```text
CreadorQRs/
├── crear_qr.py
├── README.md
└── otros archivos o carpetas según el proyecto
```

## Notas

- El programa está pensado para uso local y en consola.
- Es ideal para generar varios QR en una sola ejecución.
- La salida se guarda como imagen, lo que facilita su uso en presentaciones, redes sociales, impresiones o compartir enlaces rápidamente.

## Créditos

Proyecto desarrollado por Cristian Stiven Cortes Landazuri. Estudiante de ingeniería de Sistemas y Computación de la Universidad Nacional de Colombia.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.

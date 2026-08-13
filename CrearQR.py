"""
Creador de QRs

En este archivo vamos a crear un código QR a partir de un texto o una URL. 
Utilizamos la librería qrcode para generar códigos QR de manera sencilla.
Esto nos puede ser muy útil cuando necesitamos generar QRs para compartir información.

Librerías utilizadas:
- qrcode: Genera códigos QR
"""

# ============================================================================
# SECCIÓN 1: IMPORTACIÓN DE LIBRERÍAS
# ============================================================================
# Importamos 'qrcode' para generar los códigos QR
import qrcode


# ============================================================================
# SECCIÓN 2: MENSAJES DE BIENVENIDA
# ============================================================================
# Mostramos mensajes en la consola para informar al usuario qué hace el programa
print("\nBienvenido al generador de códigos QR") 
print("Este programa le permitirá generar un código QR a partir de un texto o una URL")
print("Ejemplo de nombre de archivo: mi_codigo_qr.png\n")


# ============================================================================
# SECCIÓN 3: ENTRADA DE DATOS DEL USUARIO
# ============================================================================
# Solicitamos al usuario que ingrese el texto o URL que desea convertir en QR
# Esta información se almacena en la variable 'dato'
dato = input("Ingrese la URL o el texto que desea convertir en código QR: ")

# Solicitamos el nombre que tendrá el archivo de imagen del QR
# El usuario debe incluir la extensión (.png, .jpg, etc.)
nombre_qr = input("Ingrese el nombre del archivo QR (con extensión .png, .jpg, etc.): ")


# ============================================================================
# SECCIÓN 4: DEFINICIÓN DE LA RUTA
# ============================================================================
# Definimos la ruta donde se guardará el código QR
# Usamos \\ porque en Windows \ es un carácter especial (carácter de escape)
# Ejemplo de ruta: Proyectos\CrearQRs\QRs\
ruta = "Proyectos\\CrearQRs\\QRs\\"


# ============================================================================
# SECCIÓN 5: CREACIÓN DEL CÓDIGO QR
# ============================================================================
# Usamos qrcode.make() para crear directamente un código QR
# Este es el método más simple: recibe los datos y devuelve una imagen
qr = qrcode.make(dato)


# ============================================================================
# SECCIÓN 6: GUARDADO DEL CÓDIGO QR
# ============================================================================
# Construimos la ruta completa del archivo (carpeta + nombre)
ruta_completa = ruta + nombre_qr

# Guardamos la imagen del QR en el archivo especificado
# .save() escribe la imagen en disco
qr.save(ruta_completa)

# Mostramos un mensaje confirmando que se guardó correctamente
print(f"\n✓ El código QR se ha generado correctamente")
print(f"Ha sido guardado en: {ruta_completa}")


# ============================================================================
# SECCIÓN 7: MOSTRAR EL QR EN PANTALLA
# ============================================================================
# Mostramos el código QR en una ventana emergente, así verificamos si todo esta perfecto
# .show() abre la imagen con el visor de imágenes predeterminado del sistema
qr.show()

# Mensajes finales
print("✓ Programa terminado correctamente")

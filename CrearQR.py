"""
Generador de códigos QR

Este programa toma un texto o una URL y la convierte en un código QR.
Para hacerlo, usamos la librería qrcode, que facilita mucho la creación
de imágenes QR sin tener que escribir un montón de lógica complicada.

Es útil cuando queremos compartir enlaces, datos o información rápida
de forma visual y práctica.

Librerías utilizadas:
- qrcode: genera el código QR final
"""

# Importamos qrcode para generar los códigos y Path para trabajar con rutas
# de archivos de una forma clara y compatible con distintos sistemas.
import qrcode
from pathlib import Path


def CreadorQR():
    # Primero mostramos una bienvenida para que el usuario sepa qué puede hacer
    # el programa y qué tipo de nombre puede usar para guardar el archivo.
    print(" ")
    print("=" * 80)
    print("Bienvenido al generador de códigos QR")
    print("Este programa te permitirá crear un código QR a partir de una URL y un nombre del archivo junto con su extensión")
    print("Ejemplo de nombre de archivo: mi_codigo_qr.png\n")

    # Repetimos la pregunta hasta recibir un número entero mayor que cero.
    while True:
        try:
            # Esta cantidad controla cuántas veces se repetirá la creación del QR.
            cantidad = int(input("¿Cuántos códigos QR quieres hacer?: "))
            if cantidad <= 0:
                raise ValueError
            break
        except ValueError:
            print("Ingrese un número entero mayor que 0.\n")

    contador = 0
    ruta_guardada = None
    extensiones_permitidas = [".png", ".jpg", ".jpeg"]

    # Cada vuelta del ciclo crea un código QR. El contador avanza solo cuando el archivo se guarda correctamente.
    while contador < cantidad:
        try:
            # El usuario puede introducir una URL, un mensaje o cualquier texto. strip() elimina espacios innecesarios al principio y al final.
            url = input("Ingrese la URL o el texto que desea convertir en código QR: ").strip()

            # Pedimos el nombre final del archivo, incluida su extensión.
            nombre_qr = input("Ingrese el nombre del archivo QR (con extensión .png, .jpg, o .jpeg): ").strip()

            # Antes de crear el código comprobamos que los datos sean útiles.
            # Si algo está vacío o tiene un formato no permitido, volvemos a intentarlo.
            if not url.strip():
                raise ValueError("La URL no puede estar vacía.")
            elif not nombre_qr.strip():
                raise ValueError("El nombre del archivo junto con su tipo, no pueden estar vacíos.")
            elif Path(nombre_qr).suffix.lower() not in extensiones_permitidas:
                raise ValueError("Usa una extensión .png, .jpg, .jpeg")

            # La ruta solo se solicita en el primer código. Después podemos reutilizarla para no obligar al usuario a escribirla varias veces.
            if ruta_guardada is None:
                pedir_ruta = input("Ingrese la ruta donde se guardará el QR: ").strip()
                if not pedir_ruta:
                    raise ValueError("La ruta no puede estar vacía.")

                # Convertimos el texto recibido en un objeto Path para trabajar con él.
                ruta = Path(pedir_ruta)
                # No podemos guardar el archivo si la carpeta no existe.
                if not ruta.is_dir():
                    raise ValueError("La ruta indicada no existe.")
                
                pregunta_ruta = input("¿Quieres guardar esta ruta para usarla después? s/n: ").strip().lower()

                # Insistimos hasta recibir una respuesta clara: sí o no.
                while pregunta_ruta not in {"s", "n"}:
                    print("Carácter incorrecto.")
                    pregunta_ruta = input("¿Quieres guardar esta ruta para usarla después? s/n: ").strip().lower()

                if pregunta_ruta == "s":
                    ruta_guardada = ruta
                    print("✓ Ruta guardada con éxito.")
                else:
                    print("X Ruta no guardada.")
            else:
                # En los siguientes códigos usamos la ruta que el usuario ya eligió.
                ruta = ruta_guardada

            # Unimos la carpeta y el nombre para obtener la ubicación completa del archivo.
            ruta_completa = ruta / nombre_qr

            # qrcode.make() transforma el texto introducido en una imagen QR.
            qr = qrcode.make(url)

            try:
            # Intentamos guardar la imagen en la ubicación elegida.
                qr.save(ruta_completa)
            except(OSError, ValueError) as error:
                print(f"No se pudo guardar el código QR: {error}")
                continue

            # Mostramos la imagen para que el usuario pueda comprobar el resultado.
            qr.show()

            # Confirmamos dónde quedó guardado el archivo.
            print(f"\n✓ El código QR se ha generado correctamente")
            print(f"Ha sido guardado en: {ruta_completa}\n")

            # Solo contamos este QR porque ya fue guardado correctamente.
            contador += 1

            # Este mensaje aparece cuando se han creado todos los códigos solicitados.
            print("✓ Programa terminado correctamente")
        # Si los datos de este QR no son válidos, mostramos el error y repetimos
        # la vuelta sin perder los códigos que ya se hayan creado.
        except ValueError:
            # Los códigos ANSI colorean el aviso de error en la terminal.
            print("\n!" + "-" * 30 + "\033[31m Ocurrio un error. Intentalo de nuevo \033[0m" + "-" * 30 + "!")
            continue
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
from pathlib import Path
import qrcode



def creador_qr():
    # Esta funcion contiene todo el flujo interactivo del programa.
    # Se ejecuta desde ejecutar.py, que importa este archivo y la llama.

    # Primero mostramos una bienvenida para que el usuario sepa qué puede hacer
    # el programa y qué tipo de nombre puede usar para guardar el archivo.
    print("\n" + "=" * 80)
    print("Bienvenido al generador de códigos QR")
    print("Este programa te permitirá crear un código QR a partir de una URL," \
    " y tambien ponerle un nombre al archivo junto con su extensión.")
    print("Ejemplo de nombre de archivo: mi_codigo_qr.png\n")

    # Repetimos la pregunta hasta recibir un numero entero mayor que cero.
    # El bloque try permite detectar entradas como texto o numeros negativos.
    while True:
        try:
            # Esta cantidad controla cuántas veces se repetirá la creación del QR.
            cantidad = int(input("¿Cuántos códigos QR quieres hacer?: "))
            if cantidad <= 0:
                raise ValueError
            break
        except ValueError:
            print("Ingrese un número entero mayor que 0.\n")

    # contador indica cuantos QR se han guardado correctamente.
    contador = 0

    # Si el usuario decide guardar la ruta, esta variable conserva la carpeta
    # para reutilizarla durante las siguientes generaciones.
    ruta_guardada = None

    # Solo aceptamos estos formatos porque son los formatos que ofrece el programa.
    extensiones_permitidas = [".png", ".jpg", ".jpeg"]

    # Cada vuelta intenta crear un QR. El ciclo termina cuando contador alcanza
    # la cantidad solicitada; si ocurre un error, contador no aumenta.
    while contador < cantidad:
        try:
            # El usuario puede introducir una URL, un mensaje o cualquier texto.
            # strip() elimina espacios innecesarios al principio y al final.
            url = input("Ingrese la URL o el texto que desea convertir en código QR: ").strip()
            # No se puede generar un QR util si no existe texto para codificar.
            if not url.strip():
                raise ValueError("La URL no puede estar vacía")

            # Pedimos el nombre final del archivo, incluida su extension.
            # El nombre se valida antes de crear la imagen para evitar archivos invalidos.
            nombre_qr = input("Ingrese el nombre del archivo QR (con extensión .png, .jpg, o .jpeg): ").lower().strip()
            if not nombre_qr.strip():
                raise ValueError("El nombre del archivo junto con su tipo, no pueden estar vacíos")
            elif Path(nombre_qr).suffix.lower() not in extensiones_permitidas:
                raise ValueError("Usa una extensión .png, .jpg, .jpeg")
            elif Path(nombre_qr).name != nombre_qr:
                raise ValueError("Escribe solo el nombre del archivo, sin carpetas")

            # La ruta solo se solicita cuando no hay una ruta guardada.
            # Asi evitamos pedir la misma carpeta para cada QR.
            if ruta_guardada is None:
                pedir_ruta = input("Ingrese la ruta donde se guardará el QR: ").strip()
                if not pedir_ruta:
                    raise ValueError("La ruta no puede estar vacía")

                # Convertimos el texto recibido en un objeto Path para combinarlo
                # de forma segura con el nombre del archivo.
                ruta = Path(pedir_ruta)
                # No podemos guardar el archivo si la carpeta no existe.
                if not ruta.is_dir():
                    raise ValueError("La ruta indicada no existe")
                # Normalizamos la respuesta para aceptar "S" y "N" como válidas.
                pregunta_ruta = input("¿Quieres guardar esta ruta para usarla después? s/n: ").lower().strip()
                # Insistimos hasta recibir una respuesta clara: s ó n.
                while pregunta_ruta not in {"s", "n"}:
                    print("Carácter incorrecto.")
                    pregunta_ruta = input("¿Quieres guardar esta ruta para usarla después? s/n: ").lower().strip()

                # Si el usuario decide guardar la ruta, la almacenamos en ruta_guardada.
                if pregunta_ruta == "s":
                    ruta_guardada = ruta
                    print("✓ Ruta guardada con éxito.")
                # Si el usuario no desea guardar la ruta el programa continua
                # Por lo tanto la variable ruta_guardada se mantiene en None
                # Así que se pedirá la ruta en la siguiente vuelta.
                else:
                    print("X Ruta no guardada.")
            else:
                # Como el usuario ya guardó una ruta, no se la pedimos de nuevo.
                # En los siguientes códigos usamos la ruta que el usuario ya eligió.
                ruta = ruta_guardada

            # Unimos la carpeta y el nombre para obtener la ubicacion completa.
            # Así evitamos errores de sintaxis al escribir la ruta manualmente.
            ruta_completa = ruta / nombre_qr

            # qrcode.make() transforma el texto introducido en una imagen QR.
            # La imagen se mantiene en memoria hasta guardarla o mostrarla.
            qr = qrcode.make(url)

            try:
                # Comprobamos si ya hay un archivo con ese nombre.
                #  Aspi evitamos sobrescribirlo sin pedir permiso antes.
                if ruta_completa.exists():
                    print("Ya existe un archivo con ese nombre.")
                    reemplazar = input("¿Desea reemplazarlo? s/n: ").lower().strip()
                    # La respuesta se normaliza con lower(),
                    # Así que se acepta respuestas como "S" ó "N".
                    if reemplazar == "s":
                        qr.save(ruta_completa)
                        print("Archivo reemplazado.")
                    elif reemplazar == "n":
                        print("OK, no se reemplazará el archivo.")
                        continue
                    else:
                        # Si el usuario ingresa algo distinto a s ó n, lanzamos un error.
                        raise ValueError("Solo se puede ingresar s ó n")
                else:
                    # Si todo esta correcto, guardamos el QR en la ruta indicada.
                    qr.save(ruta_completa)

            except PermissionError:
                print("No tienes permisos para guardar en esa carpeta.")
                continue
            except(OSError, ValueError) as error:
                print(f"No se pudo guardar el código QR: {error}")
                continue

            while True:
                # Preguntamos si el usuario quiere abrir la imagen despues de guardarla.
                # Este ciclo solo repite esta pregunta; no vuelve a crear el QR.
                mostrar_qr = input("¿Desea ver la imagen? s/n: ").strip().lower()
                if mostrar_qr == "s":
                    qr.show()
                    break
                elif mostrar_qr == "n":
                    print("OK, no se mostrará la imagen.")
                    break
                else:
                    print("Solo puedes ingresar s ó n")
                    continue

            # Confirmamos donde quedo guardado el archivo.
            print("\n✓ El código QR se ha generado correctamente")
            print(f"Ha sido guardado en: {ruta_completa}\n")

            # Solo contamos este QR porque ya fue guardado correctamente.
            contador += 1

        # Si los datos de este QR no son validos, mostramos el error y repetimos
        # la vuelta sin perder los codigos que ya se hayan creado.
        except ValueError as error:
            # Si ocurre un error, el programa no se detiene; solo se repite la vuelta.
            # Por lo tanto los códigos ya guardados no se pierden.
            # Si ocurre algún error, el mensaje de error se muestra en rojo para mayor visibilidad.
            # Tambien le mostramos al usuario el error que ocurrió para que pueda corregirlo.
            print("\n!" + "-" * 30 + f"\033[31m Error: {error}. " \
                  "Intentalo de nuevo \033[0m" + "-" * 30 + "!")
            continue
    # Este mensaje aparece cuando se han creado todos los codigos solicitados.
    print("✓ Programa terminado correctamente")

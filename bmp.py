import struct

unpack = lambda buffer: struct.unpack("=l", buffer)[0]
color = lambda r, g, b: bytes([b, g, r])

# Función que lee un archivo .bmp.
def read_bmp(path):

    # Apertura del archivo .bmp a leer.
    with open(path, "rb") as image:

        # Definición del ancho y alto de la imagen.
        image.seek(2 + 4 + 2 + 2)
        header_size = unpack(image.read(4))
        image.seek(2 + 4 + 2 + 2 + 4 + 4)
        width = unpack(image.read(4))
        height = unpack(image.read(4))

        # Salto del header para leer los pixeles de la imagen.
        image.seek(header_size)

        # Lista de pixeles a retornar al finalizar el proceso.
        pixels = []

        # Iteración sobre todas las "filas" del archivo.
        for y in range(height):

            # Nueva fila de pixeles del archivo.
            pixels.append([])

            # Iteración sobre los pixeles de cada "fila".
            for _ in range(width):

                # Tonalidades azul, verde y roja del pixel leído.
                b, g, r = (ord(image.read(1)), ord(image.read(1)), ord(image.read(1)))

                # Almacenamiento del pixel en su respectiva posición en la lista.
                pixels[y].append(color(r, g, b))

    # Retorno del ancho, alto y pixeles de la imagen.
    return width, height, pixels

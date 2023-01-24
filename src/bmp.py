import struct

color = lambda r, g, b: bytes([b, g, r])
char = lambda character: struct.pack("=c", character.encode("ascii"))
word = lambda word: struct.pack("=h", word)
dword = lambda dword: struct.pack("=l", dword)
unpack = lambda buffer: struct.unpack("=l", buffer)[0]

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

# Función que escribe un archivo .bmp.
def write_bmp(filename, framebuffer, width, height):
  
    # Constantes teóricas utilizadas para escribir un .bmp.
    HEADER_SIZE, IMAGE_HEADER_SIZE, COLORS_PER_PIXEL = 54, 40, 3

    # Apertura del archivo.
    file = open(filename, "bw")

    # Escritura preliminar del header del archivo.
    file.write(char("B"))
    file.write(char("M"))
    file.write(dword(HEADER_SIZE + (width * height * COLORS_PER_PIXEL)))
    file.write(dword(0))
    file.write(dword(HEADER_SIZE))

    # Finalización de la escritura del header del archivo.
    file.write(dword(IMAGE_HEADER_SIZE))
    file.write(dword(width))
    file.write(dword(height))
    file.write(word(1))
    file.write(word(24))
    file.write(dword(0))
    file.write(dword(width * height * COLORS_PER_PIXEL))
    file.write(dword(0))
    file.write(dword(0))
    file.write(dword(0))
    file.write(dword(0))

    # Escritura de cada pixel del archivo mediante los valores del framebuffer.
    for y in range(height):
        for x in range(width):
            file.write(framebuffer[y][x])

    # Cierre del archivo.
    file.close()

    # Retorno del nombre del archivo para futuras operaciones.
    return filename

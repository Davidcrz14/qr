import qrcode

def generar_codigo_qr(url, nombre_archivo):
    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(nombre_archivo)
    print(f"Código QR guardado como {nombre_archivo}")

if __name__ == "__main__":
    url = input("Ingresa la URL que deseas convertir en un código QR: ")

    nombre_archivo = input("Ingresa el nombre del archivo para guardar el código QR (ej. qr.png): ")

    generar_codigo_qr(url, nombre_archivo)

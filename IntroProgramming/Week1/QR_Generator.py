import qrcode
import os
import urllib.parse

# URL que quieres convertir a código QR
url = input("Please enter your link: ")

# Crear el código QR
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

# Generar la imagen del código QR
img = qr.make_image(fill="black", back_color="white")

# Extraer un identificador del enlace (puede ser la última parte del path del URL)
parsed_url = urllib.parse.urlparse(url)
identifier = os.path.basename(
    parsed_url.path
)  # Usa la última parte del path como identificador

# Si no hay un identificador claro, usa 'default' para evitar errores
if not identifier:
    identifier = "default"

# Crear la ruta para guardar en el escritorio
desktop_path = os.path.join(
    os.path.expanduser("~"), "Desktop", "QR_Codes"
)  # Carpeta "QR_Codes" en el escritorio
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)  # Crear la carpeta si no existe

# Nombre del archivo usando el identificador del link
filename = f"qr_{identifier}.png"

# Ruta completa para guardar el archivo
save_path = os.path.join(desktop_path, filename)

# Guardar la imagen
img.save(save_path)

print(f"Código QR guardado en: {save_path}")

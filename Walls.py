import os
import random
import requests
import cloudinary
import cloudinary.api
import cloudinary.uploader
import schedule
import time
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv('cloud'),
    api_key= os.getenv('Api_key'),
    api_secret= os.getenv('Api_secret')
)
LOCAL_IMAGE_DIR = "/tmp/wallpapers"
os.makedirs(LOCAL_IMAGE_DIR, exist_ok=True)

def get_images_from_cloudinary():
    """Obtiene una lista de URLs de imágenes desde la carpeta 'walls' en Cloudinary"""
    response = cloudinary.api.resources(
        type="upload",
        resource_type="image"
    )
    images = [img["url"] for img in response.get("resources", [])]
    return images
def set_wallpaper(image_url):
    """Descarga una imagen y la configura como wallpaper"""
    image_name = os.path.join(LOCAL_IMAGE_DIR, "current_wallpaper.jpg")
    
    # Descarga la imagen
    response = requests.get(image_url)
    with open(image_name, "wb") as f:
        f.write(response.content)
    
    # Cambia el fondo de pantalla usando feh
    os.system(f"feh --bg-scale {image_name}")
def update_wallpaper():
    """Actualiza el fondo de pantalla con una imagen aleatoria"""
    print("Actualizando wallpaper...")
    images = get_images_from_cloudinary()
    if images:
        image_url = random.choice(images)
        set_wallpaper(image_url)
    else:
        print("No se encontraron imágenes en la carpeta 'walls' en Cloudinary.")

# Programa la actualización cada 30 minutos
schedule.every(1).minutes.do(update_wallpaper)

# Ejecuta el ciclo del servicio
if __name__ == "__main__":
    update_wallpaper()  # Configurar un wallpaper inicial
    while True:
        schedule.run_pending()
        time.sleep(1)


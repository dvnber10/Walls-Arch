# Wallpaper Service

Este proyecto es un servicio que cambia automáticamente el fondo de pantalla en Linux utilizando `feh` y las imágenes almacenadas en la carpeta `walls` de tu cuenta de Cloudinary.

## Requisitos

1. **Sistema operativo**: Linux (probado en Arch Linux).
2. **Dependencias**:
   - Python 3.x
   - Módulos de Python: `cloudinary`, `requests`, `schedule`
   - Herramienta `feh` para gestionar wallpapers.
3. **Cuenta en Cloudinary**:
   - Configura una cuenta gratuita en [Cloudinary](https://cloudinary.com).
   - Crea una carpeta llamada `walls` y sube tus imágenes allí.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/wallpaper-service.git
   cd wallpaper-service
   ```

2. Instala las dependencias de Python:

   ```bash
   pip install cloudinary requests schedule
   ```

3. Instala `feh` (si no lo tienes):

   ```bash
   sudo pacman -S feh  # En Arch Linux
   ```

4. Configura las credenciales de Cloudinary. Crea un archivo `.env` en el mismo directorio que el script con el siguiente contenido:

   ```env
   CLOUD_NAME=tu_cloud_name
   API_KEY=tu_api_key
   API_SECRET=tu_api_secret
   ```

   Reemplaza `tu_cloud_name`, `tu_api_key` y `tu_api_secret` con tus credenciales de Cloudinary.

## Uso Manual

1. Ejecuta el script para probarlo manualmente:

   ```bash
   python3 Walls.py
   ```

2. Asegúrate de que el fondo de pantalla cambie correctamente.

## Configuración como Servicio

Puedes configurar el script como un servicio de systemd para que se ejecute automáticamente cada vez que inicie tu sistema.

1. Crea un archivo de servicio:

   ```bash
   sudo nano /etc/systemd/system/wallpaper.service
   ```

2. Copia y pega el siguiente contenido, asegurándote de ajustar las rutas:

   ```ini
   [Unit]
   Description=Servicio de Wallpapers con feh y Cloudinary
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /home/duvan/Documentos/Desarrollo/Python/System-scripts/Wallpaper/Walls.py
   Restart=always
   User=tu_usuario
   Group=tu_grupo

   [Install]
   WantedBy=multi-user.target
   ```

   - Cambia `/home/duvan/Documentos/Desarrollo/Python/System-scripts/Wallpaper/Walls.py` por la ruta real del script.
   - Cambia `tu_usuario` y `tu_grupo` por tu nombre de usuario y grupo. Puedes obtener tu grupo principal con el comando `id -g -n`.

3. Habilita y arranca el servicio:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable wallpaper.service
   sudo systemctl start wallpaper.service
   ```

4. Verifica que el servicio esté funcionando:

   ```bash
   sudo systemctl status wallpaper.service
   ```

## Personalización

- Para cambiar el intervalo de actualización del wallpaper, modifica el tiempo en el script (`schedule.every(30).minutes.do(update_wallpaper)`).

## Solución de Problemas

1. Revisa los logs del servicio para depuración:

   ```bash
   sudo journalctl -u wallpaper.service
   ```

2. Asegúrate de que las imágenes estén disponibles en la carpeta `walls` de Cloudinary.

3. Verifica que `feh` esté instalado correctamente y funcionando.

# Publicar el proyecto en GitHub y entregarlo por Canvas

> Cuenta GitHub conectada y verificada: **manosalvajoan**. El repositorio ya fue creado con el nombre `Proyecto-final-ciencia-de-datos`. Actualmente figura como privado y vacío; cambiar a público y subir el contenido antes de entregarlo.

**Repositorio creado:** https://github.com/manosalvajoan/Proyecto-final-ciencia-de-datos

**URL del repositorio existente:** https://github.com/manosalvajoan/Proyecto-final-ciencia-de-datos

## Método web (sin instalar Git)

1. Abre https://github.com/manosalvajoan/Proyecto-final-ciencia-de-datos y entra en **Settings > General > Danger Zone > Change repository visibility**, selecciona **Change to public** y confirma.
2. Regresa a **Code** y haz clic en **uploading an existing file / sube uno existente**.
3. Descomprime el ZIP, entra en la carpeta `proyecto_ciencia_datos_salarios` y arrastra **todo su contenido** (no solamente el ZIP ni la carpeta contenedora) a GitHub.
4. Confirma cambios con **Commit changes**. Comprueba que aparezcan `README.md`, `datos`, `notebook`, `presentacion` y `video`.
6. Si el navegador limita la subida o los archivos MP4 pesan demasiado, usa Git de escritorio o el enlace público del video definitivo. No es obligatorio que el archivo de video quede alojado directamente en GitHub si enlazas uno accesible.
7. Cambia los nombres de los participantes. Reemplaza el video de voz sintética por el video del equipo y modifica el enlace de README.
8. Copia la URL `https://github.com/manosalvajoan/Proyecto-final-ciencia-de-datos`. Cada integrante debe pegar exactamente esta URL en Canvas.

## Método con Git (línea de comandos)

En la carpeta `proyecto_ciencia_datos_salarios` extraída:

```bash
git init
git add .
git commit -m "Proyecto final ciencia de datos: analisis salarial"
git branch -M main
git remote add origin https://github.com/manosalvajoan/Proyecto-final-ciencia-de-datos.git
git push -u origin main
```

El repositorio ya existe; necesitas tener Git instalado y configurado. Sustituye `manosalvajoan`. Dependiendo del método de autenticación, GitHub te solicitará iniciar sesión o usar un token; **no incluyas tokens en el repositorio**.

## Comprobación final

Abre la URL del repo desde una ventana de incógnito; visualiza datos, abre el notebook, descarga el PPTX, consulta el video y confirma que cada enlace de README funcione. **La entrega no se efectúa al crear este ZIP: se efectúa cuando cada integrante publica la URL pública en Canvas.**

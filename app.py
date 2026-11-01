from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

VIDEOS_DIR = "videos"

# =====================================================
# PORTADA
# =====================================================

@app.route("/")
def inicio():
    return render_template("index.html")

# =====================================================
# CATEGORIAS
# =====================================================

@app.route("/categoria/<categoria>")
def categoria(categoria):

    ruta_categoria = os.path.join(
        VIDEOS_DIR,
        categoria
    )

    videos = []

    if os.path.exists(ruta_categoria):

        for archivo in os.listdir(ruta_categoria):

            if archivo.lower().endswith(".mp4"):

                nombre = os.path.splitext(
                    archivo
                )[0]

                videos.append({
                    "nombre": nombre,
                    "thumb": nombre + ".jpg"
                })

    videos.sort(
        key=lambda x: x["nombre"]
    )

    return render_template(
        "categoria.html",
        categoria=categoria,
        videos=videos
    )

# =====================================================
# VIDEO
# =====================================================

@app.route("/video/<categoria>/<nombre>")
def video(categoria, nombre):

    ruta_categoria = os.path.join(
        VIDEOS_DIR,
        categoria
    )

    videos = [
        os.path.splitext(f)[0]
        for f in os.listdir(ruta_categoria)
        if f.lower().endswith(".mp4")
    ]

    videos.sort()

    indice = videos.index(nombre)

    anterior = videos[
        (indice - 1) % len(videos)
    ]

    siguiente = videos[
        (indice + 1) % len(videos)
    ]

    ruta_video = (
        f"/videos/{categoria}/"
        f"{nombre}.mp4"
    )

    return render_template(
        "video.html",
        categoria=categoria,
        ruta_video=ruta_video,
        anterior=anterior,
        siguiente=siguiente
    )
# =====================================================
# SERVIR VIDEOS
# =====================================================

@app.route("/videos/<categoria>/<archivo>")
def servir_video(categoria, archivo):

    carpeta_video = os.path.join(
        VIDEOS_DIR,
        categoria
    )

    return send_from_directory(
        carpeta_video,
        archivo
    )

# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
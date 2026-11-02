from flask import Flask, render_template
import os

app = Flask(__name__)

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

    carpeta = os.path.join(
        "static",
        "thumbnails",
        categoria
    )

    videos = []

    if os.path.exists(carpeta):

        for archivo in os.listdir(carpeta):

            if archivo.lower().endswith(".jpg"):

                nombre = os.path.splitext(
                    archivo
                )[0]

                videos.append({
                    "nombre": nombre,
                    "thumb": archivo
                })

    videos.sort(key=lambda x: x["nombre"])

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

    carpeta = os.path.join(
        "static",
        "thumbnails",
        categoria
    )

    videos = []

    if os.path.exists(carpeta):

        for archivo in os.listdir(carpeta):

            if archivo.lower().endswith(".jpg"):

                videos.append(
                    os.path.splitext(archivo)[0]
                )

    videos.sort()

    indice = videos.index(nombre)

    anterior = videos[
        (indice - 1) % len(videos)
    ]

    siguiente = videos[
        (indice + 1) % len(videos)
    ]

    ruta_video = (
        f"https://res.cloudinary.com/"
        f"mh5fkptg/video/upload/"
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
# MAIN
# =====================================================

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
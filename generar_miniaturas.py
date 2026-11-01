import cv2
import os

VIDEOS_DIR = "videos"
THUMB_DIR = os.path.join("static", "thumbnails")

os.makedirs(THUMB_DIR, exist_ok=True)

for categoria in os.listdir(VIDEOS_DIR):

    ruta_categoria = os.path.join(
        VIDEOS_DIR,
        categoria
    )

    if not os.path.isdir(ruta_categoria):
        continue

    thumb_categoria = os.path.join(
        THUMB_DIR,
        categoria
    )

    os.makedirs(
        thumb_categoria,
        exist_ok=True
    )

    for archivo in os.listdir(
        ruta_categoria
    ):

        if not archivo.lower().endswith(".mp4"):
            continue

        video_path = os.path.join(
            ruta_categoria,
            archivo
        )

        nombre = os.path.splitext(
            archivo
        )[0]

        thumb_path = os.path.join(
            thumb_categoria,
            nombre + ".jpg"
        )

        if os.path.exists(thumb_path):
            continue

        cap = cv2.VideoCapture(
            video_path
        )

        success, frame = cap.read()

        if success:

            cv2.imwrite(
                thumb_path,
                frame
            )

            print(
                f"Miniatura creada: {thumb_path}"
            )

        cap.release()

print("Proceso finalizado.")
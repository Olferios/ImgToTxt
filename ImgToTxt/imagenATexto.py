import easyocr
import os

reader = easyocr.Reader(['es', 'en'])

def read_images_from_folder(folder_path):
    results_folder = "Resultados"
    os.makedirs(results_folder, exist_ok=True)

    for file in os.listdir(folder_path):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            full_path = os.path.join(folder_path, file)
            print("Leyendo:", file)

            text = reader.readtext(full_path, detail=0)
            text_joined = "\n".join(text)

            # Crear archivo .txt por cada imagen
            output_path = os.path.join(results_folder, f"{file}.txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text_joined)

            print(f"✔ Texto guardado en: {output_path}")


# Carpeta donde tienes las imágenes
folder = "Imagenes"

read_images_from_folder(folder)

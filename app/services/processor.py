import os
import pandas as pd
import json

def process_data(file_path: str) -> str:
    """
    Procesa un archivo CSV o JSON subido por el usuario y devuelve un resumen legible.

    Args:
        file_path (str): Ruta al archivo cargado.

    Returns:
        str: Resumen del contenido o errores detectados.
    """
    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext == ".csv":
            df = pd.read_csv(file_path)
        elif ext == ".json":
            with open(file_path, "r") as f:
                data = json.load(f)
                if isinstance(data, list):
                    df = pd.DataFrame(data)
                else:
                    return "⚠️ El archivo JSON debe contener una lista de objetos."
        else:
            return "❌ Formato no soportado. Solo se aceptan archivos CSV o JSON."

        resumen = {
            "archivo": os.path.basename(file_path),
            "filas": df.shape[0],
            "columnas": df.shape[1],
            "columnas_nombres": list(df.columns),
        }

        return f"✅ Archivo procesado correctamente:\n\n{json.dumps(resumen, indent=2, ensure_ascii=False)}"

    except Exception as e:
        return f"❌ Error al procesar el archivo:\n{str(e)}"

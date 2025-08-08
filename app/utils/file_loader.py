from pathlib import Path
from fastapi import UploadFile
from uuid import uuid4

async def save_uploaded_file(file: UploadFile, folder: str) -> str:
    """
    Guarda un archivo subido por el usuario en una carpeta local.

    Args:
        file (UploadFile): Archivo recibido desde el formulario.
        folder (str): Ruta relativa a la carpeta donde se debe guardar el archivo.

    Returns:
        str: Ruta completa del archivo guardado.
    """
    # Asegura que la carpeta exista
    Path(folder).mkdir(parents=True, exist_ok=True)

    # Genera un nombre único para evitar sobrescritura
    ext = file.filename.split(".")[-1]
    filename = f"{uuid4()}.{ext}"
    path = Path(folder) / filename

    # Guarda el archivo en disco
    with open(path, "wb") as buffer:
        buffer.write(await file.read())

    return str(path)

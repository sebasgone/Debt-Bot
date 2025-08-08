from fastapi import APIRouter, UploadFile, File, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.processor import process_data
from app.utils.file_loader import save_uploaded_file
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

UPLOAD_FOLDER = "data/uploads"

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    """
    Muestra la página principal con el formulario de subida.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    """
    Maneja la carga del archivo, lo guarda y lo procesa.
    """
    file_path = await save_uploaded_file(file, UPLOAD_FOLDER)
    result = process_data(file_path)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "filename": file.filename
    })

from app.services.evaluator import get_applicable_scenarios


@router.get("/clientes/{customer_id}/escenarios")
def escenarios_cliente(customer_id: str):
    """
    Retorna los escenarios de pago mínimo, plan optimizado y consolidación para un cliente dado.
    """
    try:
        result = get_applicable_scenarios(customer_id)
        prompt = f"""Explica estos escenarios financieros para un cliente en lenguaje claro y entendible, en español:\n\n{result}"""

        # Llamada a OpenAI
        response = client.chat.completions.create(model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un asesor financiero que explica resumenes de opciones financieras a clientes"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2)

        explicacion = response.choices[0].message.content

        #return {
        #    "cliente_id": customer_id,
        #    "escenarios": result,
        #    "explicacion": explicacion
        #}
        return explicacion
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

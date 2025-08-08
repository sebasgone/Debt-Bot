# 🧩 Ingesta y Evaluación de Escenarios Financieros

Esta aplicación permite:

- 📂 Subir archivos CSV o JSON con información financiera de clientes
- 🔍 Consultar escenarios personalizados por cliente (`pago mínimo`, `plan optimizado`, `consolidación`)
- 🧠 Obtener explicaciones en lenguaje natural generadas por un modelo de OpenAI (GPT)

---

## ⚙️ Requisitos

- Python 3.9 o superior
- FastAPI

---

## 📁 Estructura del proyecto

```bash
finance-assistant/
├── app/
│ ├── api/routes.py
│ ├── main.py
│ ├── services/
│ │ ├── processor.py
│ │ └── evaluator.py
│ ├── templates/index.html
│ ├── static/style.css
│ └── utils/file_loader.py
├── data/
│ ├── uploads/ # Archivos de entrada (CSV/JSON)
│ └── offers_catalog.json # Catálogo de ofertas fijas
├── .env # Variables sensibles
├── requirements.txt
└── README.md

```

---

## 🚀 Instrucciones de ejecución local

```bash
# 1. Clona el repositorio
git clone git@github.com:sebasgone/Debt-Bot.git

# 2. Crea y activa un entorno virtual
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Crea el archivo .env y agrega tu clave de OpenAI
echo "OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" > .env

# 5. Ejecuta la aplicación
uvicorn app.main:app --reload

Abrir el navegador en http://127.0.0.1:8000 para acceder a la interfaz.

```
---

## 👤 Autor

Sebastián García  
Ingeniero Mecatrónico especializado en desarrollo de aplicaciones con Python y agentes conversacionales.

- 💼 GitHub: [@sebasgone](https://github.com/sebasgone)
- 🧠 Tecnologías clave: Python, FastAPI y LangChain
- 📫 Contacto: [https://www.linkedin.com/in/sebasgone21/]



Editar


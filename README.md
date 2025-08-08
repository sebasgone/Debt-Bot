# 🧩 Ingesta y Evaluación de Escenarios Financieros

Esta aplicación permite:

- 📂 Subir archivos CSV/JSON con información financiera de clientes
- 🔍 Consultar escenarios personalizados por cliente (`pago mínimo`, `plan optimizado`, `consolidación`)
- 🧠 Obtener explicaciones en lenguaje natural generadas por un modelo de OpenAI (GPT)

---

## ⚙️ Requisitos

- Python 3.9+

---

## 📁 Estructura del proyecto

app_ingesta/
├── app/
│ ├── api/routes.py
│ ├── main.py
│ ├── services/
│ │ └── scenarios.py
│ ├── templates/index.html
│ ├── static/style.css
│ └── utils/file_loader.py
├── data/
│ ├── uploads/ # Archivos de entrada (CSV/JSON)
│ └── offers_catalog.json # Catálogo de ofertas fijo
├── .env
├── requirements.txt
└── README.md


---

## 🚀 Instrucciones de ejecución local

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo


python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

pip install -r requirements.txt

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

### 2. Ejecuta la app

uvicorn app.main:app --reload





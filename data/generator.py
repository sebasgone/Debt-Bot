# Re-generar los archivos CSV directamente en la carpeta `data/uploads/` como ruta relativa
from pathlib import Path
import pandas as pd

# Ruta relativa recomendada
uploads_dir = Path("data/uploads")
uploads_dir.mkdir(parents=True, exist_ok=True)

# 1. loans.csv
pd.DataFrame([
    {"loan_id": "L-101", "customer_id": "CU-001", "product_type": "personal", "principal": 18000.0, "annual_rate_pct": 28.5, "remaining_term_months": 36, "collateral": False, "days_past_due": 0},
    {"loan_id": "L-102", "customer_id": "CU-002", "product_type": "micro", "principal": 5000.0, "annual_rate_pct": 35.0, "remaining_term_months": 24, "collateral": False, "days_past_due": 15},
]).to_csv(uploads_dir / "loans.csv", index=False)

# 2. cards.csv
pd.DataFrame([
    {"card_id": "C-201", "customer_id": "CU-001", "balance": 3500.0, "annual_rate_pct": 45.0, "min_payment_pct": 5.0, "payment_due_day": 15, "days_past_due": 0},
    {"card_id": "C-202", "customer_id": "CU-002", "balance": 1200.0, "annual_rate_pct": 39.9, "min_payment_pct": 4.0, "payment_due_day": 10, "days_past_due": 5},
]).to_csv(uploads_dir / "cards.csv", index=False)

# 3. payments_history.csv
pd.DataFrame([
    {"product_id": "L-101", "product_type": "loan", "customer_id": "CU-001", "date": "2024-03-01", "amount": 600.0},
    {"product_id": "C-201", "product_type": "card", "customer_id": "CU-001", "date": "2024-03-05", "amount": 200.0},
]).to_csv(uploads_dir / "payments_history.csv", index=False)

# 4. credit_score_history.csv
pd.DataFrame([
    {"customer_id": "CU-001", "date": "2024-03-01", "credit_score": 720},
    {"customer_id": "CU-002", "date": "2024-03-01", "credit_score": 650},
]).to_csv(uploads_dir / "credit_score_history.csv", index=False)

# 5. customer_cashflow.csv
pd.DataFrame([
    {"customer_id": "CU-001", "monthly_income_avg": 3500.0, "income_variability_pct": 10.0, "essential_expenses_avg": 1800.0},
    {"customer_id": "CU-002", "monthly_income_avg": 2500.0, "income_variability_pct": 15.0, "essential_expenses_avg": 1600.0},
]).to_csv(uploads_dir / "customer_cashflow.csv", index=False)

list(uploads_dir.glob("*.csv"))

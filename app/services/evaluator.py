from pathlib import Path
import pandas as pd
import json

DATA_DIR = Path("data/uploads")
OFFERS_PATH = Path("data/offers_catalog.json")

def load_offers():
    with open(OFFERS_PATH, "r") as f:
        return json.load(f)

def get_applicable_scenarios(customer_id: str):
    loans = pd.read_csv(DATA_DIR / "loans.csv")
    cards = pd.read_csv(DATA_DIR / "cards.csv")
    scores = pd.read_csv(DATA_DIR / "credit_score_history.csv")
    cashflow = pd.read_csv(DATA_DIR / "customer_cashflow.csv")

    offers_catalog = load_offers()

    customer_loans = loans[loans["customer_id"] == customer_id]
    customer_cards = cards[cards["customer_id"] == customer_id]
    customer_score = scores[scores["customer_id"] == customer_id].iloc[0]["credit_score"]
    customer_cash = cashflow[cashflow["customer_id"] == customer_id].iloc[0]

    deuda_total = customer_loans["principal"].sum() + customer_cards["balance"].sum()
    tasa_promedio = (
        customer_loans["annual_rate_pct"].sum() + customer_cards["annual_rate_pct"].sum()
    ) / (len(customer_loans) + len(customer_cards))

    # Escenario 1: pago mínimo
    min_payment = (customer_cards["balance"] * (customer_cards["min_payment_pct"] / 100)).sum()
    pago_minimo = {
        "total_deuda": deuda_total,
        "tasa_promedio": tasa_promedio,
        "pago_mensual_estimado": round(min_payment + customer_loans["principal"].sum() / 36, 2),
    }

    # Escenario 2: optimizado
    cash_disponible = customer_cash["monthly_income_avg"] - customer_cash["essential_expenses_avg"]
    optimizado = {
        "pago_maximo_mensual": round(cash_disponible * 0.9, 2),
        "estrategia": "Priorizar mora y tasas altas"
    }

    # Escenario 3: consolidación
    mora_activa = (customer_loans["days_past_due"] > 0).any() or (customer_cards["days_past_due"] > 0).any()
    deuda_consolidable = pd.concat([
        customer_loans[["principal", "product_type"]].rename(columns={"principal": "amount"}),
        customer_cards[["balance"]].rename(columns={"balance": "amount"}).assign(product_type="card")
    ])

    aplicables = []
    for offer in offers_catalog:
        total_consolidable = deuda_consolidable[
            deuda_consolidable["product_type"].isin(offer["product_types_eligible"])
        ]["amount"].sum()

        if total_consolidable <= offer["max_consolidated_balance"]:
            if offer["offer_id"] == "OF-CONSO-24M" and not mora_activa:
                aplicables.append((offer, total_consolidable))
            elif offer["offer_id"] == "OF-CONSO-36M" and customer_score > 650 and not mora_activa:
                aplicables.append((offer, total_consolidable))

    if aplicables:
        mejor_oferta = sorted(aplicables, key=lambda x: x[0]["new_rate_pct"])[0]
        ahorro_estimado = round((tasa_promedio - mejor_oferta[0]["new_rate_pct"]) * mejor_oferta[1] / 100, 2)
        consolidacion = {
            "oferta": mejor_oferta[0]["offer_id"],
            "nuevo_monto": mejor_oferta[1],
            "nueva_tasa": mejor_oferta[0]["new_rate_pct"],
            "plazo": mejor_oferta[0]["max_term_months"],
            "ahorro_estimado": ahorro_estimado
        }
    else:
        consolidacion = "No aplica consolidación para este cliente"

    return {
        "cliente_id": customer_id,
        "escenario_pago_minimo": pago_minimo,
        "escenario_optimizado": optimizado,
        "escenario_consolidacion": consolidacion
    }

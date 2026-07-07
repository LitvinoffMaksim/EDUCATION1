# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: InvoiceFlow
import json, os

DATA_FILE = "invoices.json"

def save_invoices(invoices):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({"clients": clients_dict(invoices), "invoices": invoices}, f, ensure_ascii=False, indent=2)

def load_invoices():
    if not os.path.exists(DATA_FILE):
        return [], {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    clients_map = {c["id"]: c for c in data.get("clients", [])}
    invoices = data.get("invoices", [])
    for inv in invoices:
        if isinstance(inv, dict):
            inv["client"] = clients_map.get(inv.get("clientId"), {})
    return invoices, clients_map

def clients_dict(invoices):
    seen = set()
    out = []
    for inv in invoices:
        cid = inv.get("clientId")
        if cid not in seen and isinstance(cid, str) and len(cid) > 0:
            seen.add(cid)
            out.append({"id": cid})
    return out

# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: InvoiceFlow
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "clients": clients,
        "invoices": invoices,
        "settings": settings
    }
    return json.dumps(data, indent=2, ensure_ascii=False)

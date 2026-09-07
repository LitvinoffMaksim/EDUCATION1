# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: InvoiceFlow
def verify_and_repair(data):
    """Проверяет целостность данных и ремонтирует простые проблемы."""
    issues = []
    if not isinstance(data, dict):
        return "Ошибка: данные не являются словарём"
    clients = data.get("clients", [])
    invoices = data.get("invoices", [])
    if not isinstance(clients, list) or not isinstance(invoices, list):
        return "Ошибка: клиенты и счета не являются списками"
    for c in clients:
        if not isinstance(c, dict) or "id" not in c or "name" not in c:
            issues.append(f"Некорректный клиент: {c}")
    for inv in invoices:
        if not isinstance(inv, dict) or "id" not in inv or "client_id" not in inv:
            issues.append(f"Некорректный счёт: {inv}")
    return issues if issues else "Данные целостны"

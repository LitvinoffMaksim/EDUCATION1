# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: InvoiceFlow
def get_app_config():
    """Возвращает словарь глобальной конфигурации приложения."""
    return {
        "currency": "USD",
        "default_discount": 0.0,
        "late_fee": 5.0,
        "payment_terms_days": 30,
        "statuses": ["draft", "issued", "paid", "overdue", "cancelled"],
        "max_items_per_invoice": 100,
        "decimal_precision": 2,
    }

# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: InvoiceFlow
def reset_demo_data():
    """Сбросить демо-данные и очистить все структуры."""
    import random
    global clients, positions, invoices, payments, statuses, next_id

    clients = [
        {"id": 1, "name": "ООО 'Заря'", "balance": 0, "email": "zarya@example.com"},
        {"id": 2, "name": "ИП Иванов", "balance": 0, "email": "ivanov@example.com"},
        {"id": 3, "name": "ООО 'Вектор'", "balance": 0, "email": "vektor@example.com"},
    ]
    next_id = 4

    statuses = ["draft", "sent", "paid", "overdue", "cancelled"]

    def make_position(client_id, desc, price, qty=1):
        return {
            "id": next_id,
            "client_id": client_id,
            "description": desc,
            "price": price,
            "quantity": qty,
            "total": price * qty,
        }

    positions = [
        make_position(1, "Консультация", 5000),
        make_position(1, "Аудит", 25000),
        make_position(2, "Разработка", 100000),
        make_position(3, "Дизайн", 15000),
    ]
    next_id = 5

    invoices = [
        {"id": 1, "client_id": 1, "positions": [], "date": "2024-01-15", "due_date": "2024-02-15", "status": "paid"},
        {"id": 2, "client_id": 1, "positions": [], "date": "2024-02-10", "due_date": "2024-03-10", "status": "overdue"},
        {"id": 3, "client_id": 2, "positions": [], "date": "2024-01-20", "due_date": "2024-02-20", "status": "sent"},
        {"id": 4, "client_id": 3, "positions": [], "date": "2024-03-01", "due_date": "2024-04-01", "status": "draft"},
    ]
    next_id = 5

    payments = []

    random.seed(42)

def clear_all():
    """Полная очистка: все структуры становятся пустыми."""
    import random
    global clients, positions, invoices, payments, statuses, next_id

    clients = []
    positions = []
    invoices = []
    payments = []
    statuses = []
    next_id = 0

    random.seed(0)

# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: InvoiceFlow
import json, random


def run_demo():
    clients = [
        {"id": 1, "name": "ООО «Вектор»", "balance": 0},
        {"id": 2, "name": "ИП Сидоров", "balance": 0},
        {"id": 3, "name": "ЗАО «ТехноПром»", "balance": 0},
    ]
    items = [
        {"desc": "Ремонт оборудования", "price": 15000, "qty": 2},
        {"desc": "Замена фильтров", "price": 3500, "qty": 4},
        {"desc": "Техническое обслуживание", "price": 8000, "qty": 1},
    ]
    statuses = ["Ожидает оплаты", "Выплатили", "Отклонено"]

    print("=== Демо InvoiceFlow ===\n")

    for i in range(3):
        c = random.choice(clients)
        it = random.choice(items)
        total = it["price"] * it["qty"]
        due_days = random.randint(7, 60)

        invoice = {
            "id": len([x for x in clients]) + i + 1,
            "client_id": c["id"],
            "items": [{"desc": it["desc"], "price": it["price"], "qty": it["qty"]}],
            "total": total,
            "due_date": (2025 - random.randint(0, 3), random.randint(1, 12), due_days),
            "status": random.choice(statuses),
        }

        print(f"Счёт #{invoice['id']} клиенту «{c['name']}»")
        print(f"  Позиции: {', '.join([f'{x[0]} x{x[1]} = {x[2]:,.0f}' for x in invoice['items']])}")
        print(f"  Итого: {total:,.0f} руб., срок: +{due_days} дн.")
        print(f"  Статус: {invoice['status']}")

    print("\nДемо завершён. Используйте функции модуля для работы с реальными данными.")

# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: InvoiceFlow
import json, uuid
from datetime import date, timedelta
from dataclasses import dataclass, field, asdict
from enum import Enum

class Status(Enum):
    DRAFT = "draft"
    SENT = "sent"
    PAID = "paid"
    OVERDUE = "overdue"

@dataclass
class Item:
    name: str
    quantity: int
    price: float

@dataclass
class Invoice:
    id: str
    client_name: str
    items: list[Item]
    due_date: date
    status: Status = Status.DRAFT
    notes: str = ""

def get_demo_data():
    today = date.today()
    invoices = [
        Invoice(
            id=str(uuid.uuid4())[:8],
            client_name="ООО Ромашка",
            items=[Item("Консультация", 2, 5000.0), Item("Отчётность", 1, 3000.0)],
            due_date=today + timedelta(days=7),
            status=Status.SENT,
            notes="Оплата до конца месяца"
        ),
        Invoice(
            id=str(uuid.uuid4())[:8],
            client_name="ИП Иванов",
            items=[Item("Разработка API", 10, 250.0)],
            due_date=today - timedelta(days=3),
            status=Status.OVERDUE
        )
    ]
    return invoices

if __name__ == "__main__":
    demo = get_demo_data()
    for inv in demo:
        print(f"Счёт #{inv.id} для {inv.client_name}, статус: {inv.status.value}")

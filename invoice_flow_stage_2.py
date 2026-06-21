# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: InvoiceFlow
from dataclasses import dataclass, field
import re
from datetime import date
from enum import Enum
from typing import Optional

class Status(Enum):
    DRAFT = "draft"
    SENT = "sent"
    PAID = "paid"
    OVERDUE = "overdue"

@dataclass
class Customer:
    name: str
    email: str
    balance: float = 0.0
    
    def validate(self) -> bool:
        if not re.fullmatch(r"[A-Za-z\s]+", self.name): return False
        if "@" not in self.email or "." not in self.email.split("@")[-1]: return False
        return True

@dataclass
class LineItem:
    description: str
    quantity: float
    unit_price: float
    
    def validate(self) -> bool:
        if len(self.description.strip()) < 3: return False
        try:
            q = float(self.quantity); p = float(self.unit_price)
            return q > 0 and p >= 0
        except ValueError: return False

@dataclass
class Invoice:
    invoice_number: str
    customer: Customer
    items: list[LineItem] = field(default_factory=list)
    status: Status = Status.DRAFT
    due_date: Optional[date] = None
    
    def validate(self) -> bool:
        if not self.customer.validate(): return False
        for item in self.items:
            if not item.validate(): return False
        if self.status == Status.OVERDUE and (self.due_date is None or date.today() < self.due_date):
             # Logic to determine overdue status would go here, simplified validation
             pass 
        return True
    
    def calculate_total(self) -> float:
        total = 0.0
        for item in self.items:
            total += item.quantity * item.unit_price
        return round(total, 2)

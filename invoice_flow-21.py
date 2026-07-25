# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: InvoiceFlow
class Reminder:
    def __init__(self, due_date: datetime.date):
        self.due = due_date

    @property
    def is_overdue(self) -> bool:
        return datetime.date.today() > self.due

    def to_text(self) -> str:
        status = "просрочен" if self.is_overdue else "в срок"
        return f"[напоминание] оплата к {self.due} — статус: {status}"

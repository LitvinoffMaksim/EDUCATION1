# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: InvoiceFlow
def check_overdue_reminders(self):
        """Проверяет просроченные напоминания по всем документам."""
        now = datetime.now()
        for doc in self.documents:
            if not isinstance(doc, Invoice) and not isinstance(doc, Contract):
                continue
            for item in doc.items:
                due_date = item.due_date or invoice_item_due_date_default
                days_left = (due_date - now).days
                if days_left <= 0 and doc.status != "paid":
                    print(f"⚠️ Просроченный документ: {doc.get_name()}, позиция: {item.description} ({-days_left} дн.)")

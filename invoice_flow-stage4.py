# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: InvoiceFlow
def edit_invoice(invoice_id: int, updates: dict) -> Invoice | None:
    for invoice in invoices:
        if invoice.id == invoice_id:
            allowed_fields = {'client_name', 'items', 'due_date', 'status'}
            for key, value in updates.items():
                if key in allowed_fields:
                    setattr(invoice, key, value)
            return invoice
    raise ValueError(f"Счёт с ID {invoice_id} не найден")

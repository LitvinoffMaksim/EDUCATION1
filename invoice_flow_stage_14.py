# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: InvoiceFlow
def print_summary():
    """Выводит краткую сводку по всем записям."""
    print(f"=== Сводка {len(invoices)} счетов ===")
    for inv in invoices:
        due = "СРРОЧНО!" if inv.due_date and (date.today() > inv.due_date) else "в срок"
        total = f"{inv.total:.2f}"
        print(f"[{inv.id}] {inv.client} | {total} руб. | статус: {inv.status} | оплата: {due}")

print_summary()

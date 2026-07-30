# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: InvoiceFlow
def print_invoice_summary(invoice):
    """Компактный вывод одной записи счета."""
    status_symbols = {
        'paid': '[✓]', 'overdue': '[✗]', 'partial': '[~]', 'pending': '[!]',
    }
    sym = status_symbols.get(invoice['status'], '?')
    print(f"  #{invoice['id']} | {sym} {invoice['client']} | "
          f"{invoice['total']:.2f} руб. | Срок: {invoice['due_date']}")

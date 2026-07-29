# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: InvoiceFlow
def print_invoice_table(invoice):
    """Выводит информацию о счете в виде отформатированной таблицы."""
    lines = []
    sep = '=' * 70
    header = f'{sep}\nИнвойс #{invoice.id}\n{sep}'
    body = (
        f'Клиент: {invoice.client_name:<36} '
        f'Сумма: {invoice.total_amount:>12,.2f} руб.\n'
        f'Статус: {invoice.status:<20} '
        f'Дата оплаты: {invoice.due_date.strftime("%d.%m.%Y") if invoice.due_date else "Не задан"}\n'
    )
    lines = [header, body]

    for i, item in enumerate(invoice.items):
        desc = (item.description[:25] + '..') if len(item.description) > 30 else item.description
        line = f'{i+1:>2}. {desc:<36} {item.quantity:>4} шт. x {item.unit_price:>8,.2f} = {item.total:>8,.2f}'
        lines.append(line)

    total_line = f'\n{"-"*70}\nИтого: {invoice.total_amount:>12,.2f} руб.\n{sep}'
    return '\n'.join(lines + [total_line])

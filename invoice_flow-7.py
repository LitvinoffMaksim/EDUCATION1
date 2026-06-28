# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: InvoiceFlow
def sort_invoices(invoices, key='due_date', reverse=False):
    """Сортирует список счетов по указанному полю."""
    if not invoices:
        return []
    
    # Определяем ключ сортировки с обработкой None для даты
    def get_sort_key(item):
        val = item.get(key)
        if key == 'due_date' and isinstance(val, str):
            try:
                return datetime.strptime(val, '%Y-%m-%d').date()
            except ValueError:
                return float('inf')
        elif key == 'priority':
            # Преобразуем строковые приоритеты в числа для корректной сортировки
            priority_map = {'high': 1, 'medium': 2, 'low': 3}
            try:
                return priority_map.get(val.lower(), float('inf'))
            except (KeyError, AttributeError):
                return val or float('inf')
        else:
            return val
    
    sorted_invoices = sorted(invoices, key=get_sort_key)
    
    if reverse and key != 'priority':
        # Для даты и текста обратная сортировка меняет порядок логически
        # Но для приоритета (числа) reverse=True означает от низкого к высокому
        # Обычно "важные" счета идут первыми, поэтому при reverse=True мы хотим low -> high?
        # Давайте сделаем так: если reverse=True и ключ не priority, то сортируем по убыванию даты.
        # Если ключ priority и reverse=True, то от низкого приоритета к высокому (low first).
        if key == 'priority':
            sorted_invoices = sorted(sorted_invoices, key=lambda x: -get_sort_key(x))
        else:
            sorted_invoices = sorted(invoices, key=get_sort_key, reverse=True)
            
    return sorted_invoices

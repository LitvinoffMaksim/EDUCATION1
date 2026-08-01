# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: InvoiceFlow
def parse_date(date_str):
    """Parse a date string in 'YYYY-MM-DD' or 'DD.MM.YYYY' format."""
    try:
        if "-" in str(date_str):
            return datetime.strptime(str(date_str), "%Y-%m-%d").date()
        elif "." in str(date_str):
            return datetime.strptime(str(date_str), "%d.%m.%Y").date()
        else:
            raise ValueError("Неподдерживаемый формат даты")
    except (ValueError, TypeError) as e:
        return f"Ошибка: '{str(date_str)}' — некорректная дата. Используйте формат YYYY-MM-DD или DD.MM.YYYY."

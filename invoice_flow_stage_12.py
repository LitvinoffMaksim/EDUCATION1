# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: InvoiceFlow
def load_data_from_json(filepath):
    """Загружает данные из JSON-файла с обработкой ошибок."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Данные успешно загружены из '{filepath}'")
        return data
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка форматирования JSON в файле: {filepath}")
        return None
    except PermissionError:
        print(f"Нет доступа к файлу: {filepath}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных: {e}")
        return None

if __name__ == "__main__":
    sample_data = [
        {"id": 1, "client": "ACME Corp", "amount": 1500.00, "due_date": "2024-03-15"},
        {"id": 2, "client": "Globex Inc", "amount": 2300.50, "due_date": "2024-04-10"}
    ]

    with open('invoices.json', 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, ensure_ascii=False)

    loaded = load_data_from_json('invoices.json')
    if loaded:
        for invoice in loaded:
            print(f"Счёт #{invoice['id']}: клиент={invoice['client']}, сумма=${invoice['amount']:.2f}")

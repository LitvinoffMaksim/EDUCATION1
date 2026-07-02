# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: InvoiceFlow
import json, sys

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        clients = {c['id']: c for c in data.get('clients', [])}
        invoices = {}
        invoice_items = []
        
        for inv in data.get('invoices', []):
            inv_id = inv['invoice_number']
            if inv_id not in invoices:
                invoices[inv_id] = {'items': [], 'status': inv.get('status', 'draft')}
            
            item = {
                'description': inv['item_description'],
                'quantity': float(inv['quantity']),
                'unit_price': float(inv['unit_price']),
                'total': float(inv['quantity']) * float(inv['unit_price']),
                'due_date': inv.get('due_date')
            }
            invoices[inv_id]['items'].append(item)
            invoice_items.append({**item, 'invoice_number': inv_id})
        
        return {
            'clients': clients,
            'invoices': invoices,
            'all_invoice_items': invoice_items
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)

# Пример использования (раскомментируйте для теста):
if __name__ == "__main__":
    sample_json = '''
    {
      "clients": [
        {"id": 1, "name": "ООО Ромашка", "email": "info@romashka.ru"}
      ],
      "invoices": [
        {"invoice_number": "INV-001", "client_id": 1, "item_description": "Услуги консалтинга", "quantity": 10, "unit_price": 5000.0, "due_date": "2024-12-31", "status": "paid"},
        {"invoice_number": "INV-002", "client_id": 1, "item_description": "Лицензионное ПО", "quantity": 1, "unit_price": 15000.0, "due_date": "2024-11-30", "status": "pending"}
      ]
    }
    '''
    
    loaded_data = load_initial_data(sample_json)
    print(f"Загружено клиентов: {len(loaded_data['clients'])}")
    print(f"Загружено счетов: {len(loaded_data['invoices'])}")

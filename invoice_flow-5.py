# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: InvoiceFlow
def remove_invoice(invoice_id):
    if invoice_id not in invoices:
        print(f"Счёт #{invoice_id} не найден.")
        return False
    
    client_id = invoices[invoice_id]['client_id']
    del invoices[invoice_id]
    
    clients[client_id]['invoices'].remove(invoice_id)
    print(f"Счёт #{invoice_id} успешно удалён у клиента {clients[client_id]['name']}")
    return True

def remove_client(client_id):
    if client_id not in clients:
        print(f"Клиент #{client_id} не найден.")
        return False
    
    for invoice_id in list(clients[client_id].get('invoices', [])):
        del invoices[invoice_id]
    
    del clients[client_id]
    print(f"Клиент #{client_id} и все его счета успешно удалены.")
    return True

def remove_item(invoice_id, item_id):
    if invoice_id not in invoices:
        print(f"Счёт #{invoice_id} не найден.")
        return False
    
    items = invoices[invoice_id].get('items', [])
    for i, item in enumerate(items):
        if item['id'] == item_id:
            del items[i]
            print(f"Позиция #{item_id} удалена из счёта #{invoice_id}")
            return True
    
    print(f"Позиция #{item_id} не найдена в счёте #{invoice_id}.")
    return False

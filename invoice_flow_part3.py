# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: InvoiceFlow
class InvoiceFlow:
    def __init__(self):
        self.clients = {}
        self.invoices = []

    def add_client(self, name: str, email: str) -> int:
        client_id = len(self.clients) + 1
        self.clients[client_id] = {"name": name, "email": email}
        return client_id

    def create_invoice(self, client_id: int, items: list, due_date: str, status: str = "draft") -> dict:
        if client_id not in self.clients:
            raise ValueError(f"Client {client_id} not found.")
        
        invoice_id = len(self.invoices) + 1
        total_amount = sum(item["amount"] for item in items)
        
        invoice = {
            "id": invoice_id,
            "client_id": client_id,
            "items": items,
            "due_date": due_date,
            "status": status,
            "total_amount": total_amount
        }
        self.invoices.append(invoice)
        return invoice

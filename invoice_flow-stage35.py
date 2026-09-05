# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: InvoiceFlow
def get_next_action(invoice, clients_db, positions_db):
    """Recommend the next step based on the current invoice state."""
    client = clients_db.get(invoice["client_id"])
    if not client:
        return "Unknown client. Check client records."
    if invoice["status"] == "draft":
        return f"Finalize invoice for client {client['name']}."
    if invoice["status"] == "sent":
        days_overdue = (datetime.now() - invoice["due_date"]).days
        if days_overdue > 30:
            return f"Urgent: Follow up on overdue payment from {client['name']} ({days_overdue} days overdue)."
        elif days_overdue > 0:
            return f"Remind {client['name']} about upcoming payment due in {days_overdue} days."
        else:
            return f"Wait for payment from {client['name']}."
    if invoice["status"] == "paid":
        return f"Invoice for {client['name']} is fully paid. Archive it."
    if invoice["status"] == "refunded":
        return f"Invoice for {client['name']} was refunded. No further action needed."
    return "Review invoice status and take appropriate action."

# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: InvoiceFlow
def search_invoices(self, query):
    """Поиск счетов по нескольким полям без учёта регистра."""
    if not query:
        return list(self._invoices.values())
    
    q = query.lower().strip()
    results = []
    for invoice_id, inv in self._invoices.items():
        searchable_fields = [
            inv['client_name'],
            inv['invoice_number'],
            (inv.get('items', []) and ', '.join([item['description'] for item in inv['items']])),
            inv['status'],
        ]
        if any(q in sf.lower() for sf in searchable_fields):
            results.append(inv)
    return results

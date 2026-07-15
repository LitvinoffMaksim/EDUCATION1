# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: InvoiceFlow
def monthly_stats(invoices):
    """Calculate and return monthly statistics grouped by month."""
    from collections import defaultdict
    
    stats = defaultdict(lambda: {'count': 0, 'total_value': 0.0})
    
    for inv in invoices:
        if inv.created_at is None or inv.due_date is None:
            continue
        
        # Extract year-month tuple
        month_key = (inv.created_at.year, inv.created_at.month)
        
        stats[month_key]['count'] += 1
        stats[month_key]['total_value'] += inv.amount
    
    return dict(sorted(stats.items()))

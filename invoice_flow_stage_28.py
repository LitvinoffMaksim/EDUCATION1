# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: InvoiceFlow
def compute_metrics(invoices: list[Invoice]) -> dict[str, Any]:
    """Calculate key metrics for the invoice system."""
    total_amount = sum(inv.total for inv in invoices)
    overdue = [inv for inv in invoices if inv.status == InvoiceStatus.PAID and inv.due_date < datetime.now()]
    overdue_amount = sum(inv.total for inv in overdue)
    avg_days_to_pay = (
        sum((datetime.now() - inv.due_date).days for inv in invoices if inv.status == InvoiceStatus.PAID and inv.due_date < datetime.now())
        / len(overdue) if overdue else 0
    )
    return {
        "total_amount": total_amount,
        "overdue_amount": overdue_amount,
        "avg_days_to_pay": avg_days_to_pay,
        "total_invoices": len(invoices),
        "paid_invoices": len([inv for inv in invoices if inv.status == InvoiceStatus.PAID]),
        "overdue_percentage": (overdue_amount / total_amount * 100) if total_amount else 0,
    }

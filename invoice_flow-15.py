# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: InvoiceFlow
def weekly_stats(invoices):
    """Return dict: week_start_date -> {total, count, avg} for each completed invoice."""
    from datetime import timedelta
    stats = {}
    today = date.today()
    for inv in invoices:
        if inv.status != "completed":
            continue
        due = inv.due_date - timedelta(days=inv.payment_days)
        week_start = due.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(
            weeks=(today.weekday() + 1) % 7 if today.weekday() < 5 else ((today - timedelta(days=6)).weekday()),
        )
        # Simpler approach: use isocalendar to get ISO week start
        iso = due.isocalendar()
        year, week_num, _ = iso
        week_start = date(year, 1, 1) + timedelta(weeks=(week_num - 1))
        key = week_start.isoformat()
        if key not in stats:
            stats[key] = {"total": 0.0, "count": 0}
        stats[key]["total"] += inv.amount
        stats[key]["count"] += 1
    for k in stats:
        s = stats[k]
        s["avg"] = round(s["total"] / s["count"], 2) if s["count"] else 0.0
    return sorted(stats.items())

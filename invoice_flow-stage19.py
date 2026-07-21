# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: InvoiceFlow
def archive_records(db, days=90):
    """Archive completed or older records from the database."""
    import datetime
    cutoff = datetime.datetime.now() - datetime.timedelta(days=days)
    archived = []
    for record in db.records:
        if (record.status == "paid" or record.status == "cancelled") and record.created_at < cutoff:
            archived.append(record)
    return archived

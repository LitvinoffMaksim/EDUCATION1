# === Stage 20: Добавь восстановление записей из архива ===
# Project: InvoiceFlow
def recover_archived_invoices(archive_path="archive.csv"):
    """Восстанавливает записи из архива в основной файл."""
    import csv, os
    if not archive_path or not os.path.exists(archive_path):
        return 0
    count = 0
    with open(archive_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames) if reader.fieldnames else ["id","client_id","items","due_date","status"]
        main_rows = []
        with open("invoices.csv", "a", newline="", encoding="utf-8") as out:
            writer = csv.DictWriter(out, fieldnames=fieldnames)
            for row in reader:
                clean_row = {k: row.get(k, "") for k in fieldnames}
                main_rows.append(clean_row)
                count += 1
        if main_rows:
            with open("invoices.csv", "w", newline="", encoding="utf-8") as out2:
                writer = csv.DictWriter(out2, fieldnames=fieldnames)
                writer.writeheader()
                for r in main_rows:
                    writer.writerow(r)
    return count

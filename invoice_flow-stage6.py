# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: InvoiceFlow
from typing import Callable, Optional
def filter_invoices(
    records: list[dict],
    status: Optional[str] = None,
    category: Optional[str] = None,
    tags: Optional[list[str]] = None,
) -> list[dict]:
    def matches(record):
        if status and record.get("status") != status: return False
        if category and record.get("category") != category: return False
        if tags is not None:
            rec_tags = record.get("tags", [])
            if any(t in rec_tags for t in tags) or (not tags): pass
            elif not any(t in rec_tags for t in tags): return False
        return True
    return [r for r in records if matches(r)]

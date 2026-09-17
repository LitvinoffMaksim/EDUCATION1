# === Stage 43: Добавь пагинацию длинных списков ===
# Project: InvoiceFlow
def paginate(items, page_size=10):
    if not items:
        return {"data": [], "total": 0, "page": 1, "pages": 0}
    total = len(items)
    pages = (total + page_size - 1) // page_size
    start = (page - 1) * page_size
    end = start + page_size
    return {"data": items[start:end], "total": total, "page": page, "pages": pages}

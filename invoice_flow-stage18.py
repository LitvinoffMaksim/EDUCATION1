# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: InvoiceFlow
def add_tag(invoice, tag):
    if not isinstance(tag, str) or not tag.strip():
        return invoice
    tags = invoice.tags.copy()
    if tag not in tags:
        tags.append(tag)
    invoice.tags = tags
    return invoice


def remove_tag(invoice, tag):
    if not isinstance(tag, str) or not tag.strip():
        return invoice
    tags = [t for t in invoice.tags if t != tag]
    invoice.tags = tags
    return invoice

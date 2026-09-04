# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: InvoiceFlow
class Template:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

    def __repr__(self):
        return f"Template({self.name}, {self.fields})"

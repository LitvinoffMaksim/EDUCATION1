# === Stage 17: Добавь группировку записей по категориям ===
# Project: InvoiceFlow
class CategoryGroup:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, record):
        self.items.append(record)

    @property
    def count(self):
        return len(self.items)


def group_records(records, categories=None):
    if categories is None:
        categories = {}
    for r in records:
        cat_name = getattr(r, 'category', 'default') or ('default' if not hasattr(r, 'category') else str(getattr(r, 'category')))
        if cat_name not in categories:
            categories[cat_name] = CategoryGroup(cat_name)
        categories[cat_name].add(r)
    return categories


def list_categories(groups):
    for name, group in groups.items():
        print(f"[{name}] ({group.count} записей)")

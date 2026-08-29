# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: InvoiceFlow
class UserProfile:
    def __init__(self, name, role, permissions=None):
        self.name = name
        self.role = role
        self.permissions = permissions or []

    def __repr__(self):
        return f"UserProfile(name={self.name!r}, role={self.role!r}, permissions={self.permissions!r})"

    def has_permission(self, perm):
        return perm in self.permissions

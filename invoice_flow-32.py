# === Stage 32: Добавь журнал действий пользователя ===
# Project: InvoiceFlow
class ActionLog:
    _log = []
    @classmethod
    def log(cls, action, user, details=None):
        cls._log.append({"action": action, "user": user, "details": details or ""})
    @classmethod
    def get_log(cls):
        return cls._log.copy()
    @classmethod
    def clear(cls):
        cls._log.clear()
    @classmethod
    def find(cls, action, user=None):
        return [e for e in cls._log if e["action"] == action and (user is None or e["user"] == user)]

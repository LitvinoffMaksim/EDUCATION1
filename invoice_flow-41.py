# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: InvoiceFlow
def dry_run(operation, **kwargs):
    """Simulate a write operation without persisting it.

    Returns a dict with the original request data and a 'simulated' flag.
    """
    return {
        "operation": operation,
        "data": kwargs,
        "simulated": True,
    }

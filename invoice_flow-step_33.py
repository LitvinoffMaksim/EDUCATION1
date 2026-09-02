# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: InvoiceFlow
import sys
from contextlib import contextmanager
from io import StringIO

@contextmanager
def undoable(action, *args, **kwargs):
    """Context manager that captures stdout/stderr and calls undo on exit."""
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = StringIO()
    sys.stderr = StringIO()
    try:
        yield
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        stdout_output = sys.stdout.getvalue()
        stderr_output = sys.stderr.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr

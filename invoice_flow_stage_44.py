# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: InvoiceFlow
import json, os, shutil
def backup_data_file(data_file: str, backup_dir: str = "backups", suffix: str = "backup") -> str:
    if not os.path.isfile(data_file):
        return ""
    os.makedirs(backup_dir, exist_ok=True)
    base, ext = os.path.splitext(data_file)
    timestamp = os.path.basename(data_file).replace(f"{suffix}_", "")
    backup_name = f"{base}_{suffix}_{timestamp}{ext}"
    backup_path = os.path.join(backup_dir, backup_name)
    shutil.copy2(data_file, backup_path)
    return backup_path

def restore_from_backup(backup_dir: str = "backups", suffix: str = "backup") -> str | None:
    backups = [f for f in os.listdir(backup_dir) if f.startswith(f"{suffix}_")]
    if not backups:
        return None
    latest = max(backups, key=lambda f: os.path.getmtime(os.path.join(backup_dir, f)))
    return os.path.join(backup_dir, latest)

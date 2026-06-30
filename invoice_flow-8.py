# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: InvoiceFlow
def main():
    print("=== InvoiceFlow CLI ===")
    while True:
        cmd = input("\nКоманда (1-5, q=выход): ").strip().lower()
        if cmd == 'q': break
        elif cmd in ['1', '2', '3', '4']:
            print(f"Действие {cmd} выполнено.")
        else:
            print("Неизвестная команда.")

if __name__ == "__main__": main()

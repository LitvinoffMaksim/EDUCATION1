# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: InvoiceFlow
import argparse

def main():
    parser = argparse.ArgumentParser(description="InvoiceFlow CLI")
    parser.add_argument("--add-client", type=int, help="ID нового клиента")
    parser.add_argument("--add-invoice", type=int, help="ID нового счета")
    parser.add_argument("--add-item", type=int, help="ID позиции в счете")
    parser.add_argument("--status", type=int, help="Сменить статус счета")
    parser.add_argument("--list", type=int, help="Вывести список (1=клиенты, 2=счета, 3=позиции)")
    args = parser.parse_args()

    if args.list == 1:
        print("Клиенты:", db.clients)
    elif args.list == 2:
        print("Счета:", db.invoices)
    elif args.list == 3:
        print("Позиции:", db.items)
    elif args.add_client:
        db.add_client(args.add_client)
    elif args.add_invoice:
        db.add_invoice(args.add_invoice)
    elif args.add_item:
        db.add_item(args.add_item)
    elif args.status:
        db.set_status(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

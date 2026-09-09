# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: InvoiceFlow
import unittest

class TestInvoiceFlow(unittest.TestCase):
    def test_add_position(self):
        invoice = Invoice()
        invoice.client_name = "TestCorp"
        invoice.positions.append(Position("Widget", 100, 5))
        self.assertEqual(invoice.positions[0].description, "Widget")
        self.assertEqual(invoice.positions[0].quantity, 5)
        self.assertEqual(invoice.positions[0].unit_price, 100)

    def test_total_calculation(self):
        invoice = Invoice()
        invoice.positions.append(Position("Widget", 100, 5))
        invoice.positions.append(Position("Gadget", 50, 3))
        self.assertEqual(invoice.total, 650)

    def test_due_date_calculation(self):
        today = datetime(2024, 1, 1)
        invoice = Invoice()
        invoice.positions.append(Position("Widget", 100, 5))
        invoice.due_date = today + timedelta(days=30)
        self.assertEqual(invoice.due_date, today + timedelta(days=30))

    def test_mark_paid(self):
        invoice = Invoice()
        invoice.positions.append(Position("Widget", 100, 5))
        invoice.mark_paid()
        self.assertEqual(invoice.status, "PAID")

    def test_mark_overdue(self):
        today = datetime(2024, 1, 1)
        invoice = Invoice()
        invoice.positions.append(Position("Widget", 100, 5))
        invoice.due_date = today - timedelta(days=10)
        invoice.mark_overdue()
        self.assertEqual(invoice.status, "OVERDUE")

    def test_mark_draft(self):
        invoice = Invoice()
        invoice.mark_draft()
        self.assertEqual(invoice.status, "DRAFT")

if __name__ == '__main__':
    unittest.main()

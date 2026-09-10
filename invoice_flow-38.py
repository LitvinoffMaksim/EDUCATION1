# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: InvoiceFlow
import unittest

class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        from invoiceflow import InvoiceFlow
        self.flow = InvoiceFlow()
        self.flow.add_client("Test Corp")
        self.flow.add_client("Small Biz")

    def test_add_duplicate_client_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_client("Test Corp")

    def test_add_client_no_name_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_client("")

    def test_add_client_only_spaces_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_client("   ")

    def test_add_item_no_client_raises(self):
        self.flow.add_item("Widget", 10, 1, "Test Corp")

    def test_add_item_no_client_name_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 10, 1)

    def test_add_item_no_description_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 10, 1, "Test Corp", desc="")

    def test_add_item_no_description_only_spaces_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 10, 1, "Test Corp", desc="   ")

    def test_add_item_no_quantity_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 10, 0, "Test Corp")

    def test_add_item_no_price_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 0, 1, "Test Corp")

    def test_add_item_no_due_date_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 10, 1, "Test Corp", due="")

    def test_add_item_no_due_date_only_spaces_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 10, 1, "Test Corp", due="   ")

    def test_add_item_no_due_date_only_commas_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 10, 1, "Test Corp", due=",")

    def test_add_item_no_due_date_only_slashes_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 10, 1, "Test Corp", due="/")

    def test_add_item_no_due_date_only_underscores_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 10, 1, "Test Corp", due="_")

    def test_add_item_no_due_date_only_dashes_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 10, 1, "Test Corp", due="-")

    def test_add_item_no_due_date_only_hyphens_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item("Widget", 10, 1, "Test Corp", due="-")

    def test_add_item_no_due_date_only_colons_raises(self):
        with self.assertRaises(ValueError):
            self.flow.add_item

from odoo.tests.common import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestPaymentNumber(TransactionCase):
    def test_payment_number_field_is_defined(self):
        self.assertIn("payment_number", self.env["account.move"]._fields)

    def test_payment_number_views_are_vendor_bill_scoped(self):
        form_view = self.env.ref(
            "autoinfo_account_move_link_payment_number.view_vendor_bill_form_inherit_payment_number"
        )
        tree_view = self.env.ref(
            "autoinfo_account_move_link_payment_number.view_vendor_bill_tree_inherit_payment_number"
        )

        self.assertIn("move_type", form_view.arch_db)
        self.assertIn("default_move_type", tree_view.arch_db)


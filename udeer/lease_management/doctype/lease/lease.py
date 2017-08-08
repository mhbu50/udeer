# -*- coding: utf-8 -*-
# Copyright (c) 2015, moosa and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, getdate, add_months


class Lease(Document):

    def after_insert(self):
        installment = self.annual_rent / self.installment_number
        for i in range(self.installment_number,0,-1):
            new_installment = frappe.new_doc("Lease Installment")
            new_installment.lease = self.name
            new_installment.status = "Not Paid"
            new_installment.number = i
            new_installment.due_date = add_months(self.lease_starting_date, i)
            new_installment.amount = installment
            new_installment.insert()

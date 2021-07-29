# -*- coding: utf-8 -*-
# Copyright (c) 2015, moosa and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class PropertyUnit(Document):

	def before_insert(self):
		self.parent = self.property
		self.parentfield = 'property_units'
		self.parenttype = 'property'

	def on_update(self):
		self.parent = self.property
		self.parentfield = 'property_units'
		self.parenttype = 'property'

	def copy_unit(self,arg):
		for i in range(arg):
			current_doc = frappe.get_doc("Property Unit",self.name)
			new_doc = frappe.copy_doc(current_doc)
			new_doc.unit_number = new_doc.unit_number + i + 1
			new_doc.insert()

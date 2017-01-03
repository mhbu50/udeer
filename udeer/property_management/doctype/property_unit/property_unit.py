# -*- coding: utf-8 -*-
# Copyright (c) 2015, moosa and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class propertyunit(Document):
	
	def before_insert(self):
	
		self.parent = self.property
		self.parentfield = 'property_units'
		self.parenttype = 'property'

	def on_update(self):	
		self.parent = self.property
		self.parentfield = 'property_units'
		self.parenttype = 'property'



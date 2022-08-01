# -*- coding: utf-8 -*-
# Copyright (c) 2015, moosa and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe.utils import flt, getdate, add_months,cint



class Lease(Document):

    def validate(self):
        monthly_rent = self.annual_rent / 12
        lease_duration = cint(self.lease_duration.split('-')[0])
        rent = monthly_rent * lease_duration
        self.full_payment = (self.annual_water_usage + self.insuranse + rent) -  self.received_payment

    def after_insert(self):
        monthly_rent = self.annual_rent / 12
        lease_duration = cint(self.lease_duration.split('-')[0])
        payment_every = cint(self.payment_every.split('-')[0])
        due_date = self.lease_starting_date

        if lease_duration == 1:
            new_installment = frappe.new_doc("Lease Installment")
            new_installment.lease = self.name
            new_installment.status = "Not Active"
            new_installment.number = i + 1  
            new_installment.due_date = add_months(self.lease_starting_date, i)
            new_installment.amount = monthly_rent
            new_installment.property = self.property
            new_installment.property_unit = self.property_unit
            new_installment.property_owner = self.property_owner
            new_installment.insert()

        if lease_duration == 3:
            if payment_every == 1:
                for i in range(3):
                    new_installment = frappe.new_doc("Lease Installment")
                    new_installment.lease = self.name
                    new_installment.status = "Not Active"
                    new_installment.number = i + 1  
                    new_installment.due_date = add_months(self.lease_starting_date, i)
                    new_installment.amount = monthly_rent 
                    new_installment.property = self.property
                    new_installment.property_unit = self.property_unit
                    new_installment.property_owner = self.property_owner
                    new_installment.insert()
           
        if lease_duration == 6:
            if payment_every == 1:
                        for i in range(6):
                            new_installment = frappe.new_doc("Lease Installment")
                            new_installment.lease = self.name
                            new_installment.status = "Not Active"
                            new_installment.number = i + 1
                            if( i != 0):
                                due_date = add_months(due_date, payment_every)                        
                            new_installment.due_date = due_date
                            new_installment.amount = monthly_rent 
                            new_installment.property = self.property
                            new_installment.property_unit = self.property_unit
                            new_installment.property_owner = self.property_owner
                            new_installment.insert()
            if payment_every == 3:                 
                for i in range(2):                                                  
                    new_installment = frappe.new_doc("Lease Installment")
                    new_installment.lease = self.name
                    new_installment.status = "Not Active"
                    new_installment.number = i  + 1  
                    if( i != 0):
                        due_date = add_months(due_date, payment_every)
                    new_installment.due_date = due_date
                    new_installment.amount = monthly_rent * 3 
                    new_installment.property = self.property
                    new_installment.property_unit = self.property_unit
                    new_installment.property_owner = self.property_owner
                    new_installment.insert()
        if lease_duration == 12:
            if payment_every == 1:
                        for i in range(12):
                            new_installment = frappe.new_doc("Lease Installment")
                            new_installment.lease = self.name
                            new_installment.status = "Not Active"
                            new_installment.number = i + 1  
                            new_installment.due_date = add_months(self.lease_starting_date, i)
                            new_installment.amount = monthly_rent 
                            new_installment.property = self.property
                            new_installment.property_unit = self.property_unit
                            new_installment.property_owner = self.property_owner
                            new_installment.insert()
            if payment_every == 3: 

                for i in range(4):                                                  
                    new_installment = frappe.new_doc("Lease Installment")
                    new_installment.lease = self.name
                    new_installment.status = "Not Active"
                    new_installment.number = i + 1
                    if( i != 0):
                        due_date = add_months(due_date, payment_every)
                    new_installment.due_date = due_date
                    new_installment.amount = monthly_rent * 3 
                    new_installment.property = self.property
                    new_installment.property_unit = self.property_unit
                    new_installment.property_owner = self.property_owner
                    new_installment.insert()
            if payment_every == 6: 

                for i in range(2):                                                  
                    new_installment = frappe.new_doc("Lease Installment")
                    new_installment.lease = self.name
                    new_installment.status = "Not Active"
                    new_installment.number = i + 1  
                    if( i != 0):
                        due_date = add_months(due_date, payment_every)
                    new_installment.due_date = due_date
                    new_installment.amount = monthly_rent * 6 
                    new_installment.property = self.property
                    new_installment.property_unit = self.property_unit
                    new_installment.property_owner = self.property_owner
                    new_installment.insert()
        if lease_duration == 24:
            if payment_every == 1:
                        for i in range(24):
                            new_installment = frappe.new_doc("Lease Installment")
                            new_installment.lease = self.name
                            new_installment.status = "Not Active"
                            new_installment.number = i + 1
                            if( i != 0):
                                due_date = add_months(due_date, payment_every)  
                            new_installment.due_date = due_date
                            new_installment.amount = monthly_rent 
                            new_installment.property = self.property
                            new_installment.property_unit = self.property_unit
                            new_installment.property_owner = self.property_owner
                            new_installment.insert()
            if payment_every == 3: 

                for i in range(8):                                                  
                    new_installment = frappe.new_doc("Lease Installment")
                    new_installment.lease = self.name
                    new_installment.status = "Not Active"
                    new_installment.number = i + 1  
                    if( i != 0):
                        due_date = add_months(due_date, payment_every) 
                    new_installment.due_date = due_date
                    new_installment.amount = monthly_rent * 3 
                    new_installment.property = self.property
                    new_installment.property_unit = self.property_unit
                    new_installment.property_owner = self.property_owner
                    new_installment.insert()
            if payment_every == 6: 

                for i in range(4):                                                  
                    new_installment = frappe.new_doc("Lease Installment")
                    new_installment.lease = self.name
                    new_installment.status = "Not Active"
                    new_installment.number = i + 1 
                    if( i != 0):
                        due_date = add_months(due_date, payment_every) 
                    new_installment.due_date = due_date
                    new_installment.amount = monthly_rent * 6 
                    new_installment.property = self.property
                    new_installment.property_unit = self.property_unit
                    new_installment.property_owner = self.property_owner
                    new_installment.insert()                        

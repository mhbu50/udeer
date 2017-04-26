from __future__ import unicode_literals
import frappe
import frappe.utils
from frappe.utils.oauth import get_oauth2_authorize_url, get_oauth_keys, login_via_oauth2, login_oauth_user as _login_oauth_user, redirect_post_login
import json
from frappe import _
from frappe.auth import LoginManager
from frappe.integrations.doctype.ldap_settings.ldap_settings import get_ldap_settings
import time
from datetime import date, timedelta
from frappe.model.document import Document

from udeer.custom_functions.custom import get_units_by_customer , get_property_by_unit


@frappe.whitelist(allow_guest=True)
def next_payment(customer):
  customer = json.loads(customer)
  leases = frappe.get_list('lease',fields=["*"], filters = [['renter','=',customer]] )
  next_payments = []
  for lease in leases:
    print lease.name
    lease_instalments = frappe.get_list('lease_instalment',fields=["*"], filters = [['lease','=',lease.name],['status','=','not paid']] )
    for lease_instalment in lease_instalments:
      print lease_instalment.name
      next_payments.append(lease_instalment.due_date)
  return next_payments

@frappe.whitelist(allow_guest=True)
def activity(customer):
  customer = json.loads(customer)
  leases = frappe.get_list('lease',fields=["*"], filters = [['renter','=',customer]] )
  for lease in leases:
    lease_instalments = frappe.get_list('lease_instalment',fields=["*"], filters = [['lease','=',lease.name],['status','=','paid']] )
    for lease_instalment in lease_instalments:
      next_payments.append(lease_instalment.due_date)
  activity['leases'] = leases
  activity['lease_instalment'] = lease_instalments
  # next_payments = frappe.get_list('lease_instalment',fields=["due_date"], filters = [["status", "=", "not paid"]["lease", "in", user_leases]])
  # filters = [["modified", ">", "2014-01-01"]]
  return activity

@frappe.whitelist(allow_guest=True)
def my_leases(customer):
  customer = json.loads(customer)
  leases = frappe.get_list('lease',fields=["*"], filters = [['renter','=',customer]] )
  
  # next_payments = frappe.get_list('lease_instalment',fields=["due_date"], filters = [["status", "=", "not paid"]["lease", "in", user_leases]])
  # filters = [["modified", ">", "2014-01-01"]]
  return leases

@frappe.whitelist(allow_guest=True)
def my_address(customer):
  customer = json.loads(customer)
  customer = frappe.get_doc('Customer', customer)
  units = get_units_by_customer(customer.name)
  responde = {}
  for unit in units:
    responde[unit.name] = {}
    responde[unit.name]['unit'] = 'unit'
    responde[unit.name]['property'] =  get_property_by_unit(unit.name)

  return responde



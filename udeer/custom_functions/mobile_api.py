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
  lease_instalments = []
  maintenance_order = maintenance_list = frappe.get_list('Issue',fields=["*"], filters = [['Customer','=', customer ],['type','=', 'maintenance']])
  for lease in leases:
    lease_instalments = frappe.get_list('lease_instalment',fields=["*"], filters = [['lease','=',lease.name],['status','=','paid']] )
    for lease_instalment in lease_instalments:
      next_payments.append(lease_instalment.due_date)
  result = {'leases' : leases ,'maintenance_order' : maintenance_order,'lease_instalments':lease_instalments } 
  return result

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


@frappe.whitelist(allow_guest=True)
def index_owner(owner):
  owner = json.loads(owner)
  owner = frappe.get_doc('property_owner', owner)
  result = {}
  properties = frappe.get_list('property', filters = [['property_owner','=',owner.name]] )
  property_units = frappe.get_list('property unit', filters = [['property','in',dic_to_array(properties)]] )
  leases = frappe.get_list('lease', filters = [['property_unit','in',dic_to_array(property_units)]] )
  result = {'properties':properties,'property_units':property_units,'leases':leases}
  return result

@frappe.whitelist(allow_guest=True)
def index_manager():
  properties = frappe.get_list('property')
  leases = frappe.get_list('lease',fields=["*"])
  expired_leases = frappe.get_list('lease',fields=["*"], filters = [['active','=',0]])
  empty_property_units = frappe.get_list('property unit',filters = [['name','not in',dic_to_array__property_unit(leases)]])
  full_property_units = frappe.get_list('property unit',filters = [['name','in',dic_to_array__property_unit(leases)]])
  income = frappe.get_list('receipt',fields=["*"], filters = [['type','=','catch']] )
  outcome = frappe.get_list('receipt',fields=["*"], filters = [['type','=','pay']] )
  result = { 'leases':leases,'expired_leases':expired_leases,'empty_property_units':empty_property_units,
             'full_property_units':full_property_units,'income':income,'outcome':outcome }
  return result
#report page
@frappe.whitelist(allow_guest=True)
def maintenance_list(owner):
  owner = json.loads(owner)
  properties = dic_to_array( frappe.get_list('property', filters = [['property_owner','=',owner]]) )
  property_units = dic_to_array( frappe.get_list('property unit', filters = [['property','in', properties ]]) )
  maintenance_list = frappe.get_list('Issue',fields=["*"], filters = [['property_unit','in', property_units ],['type','=', 'maintenance']])
  return maintenance_list

#report page
@frappe.whitelist(allow_guest=True)
def properties_report(owner):
  owner = json.loads(owner)
  properties =  frappe.get_list('property',fields=["*"], filters = [['property_owner','=',owner]]) 
  property_units =  frappe.get_list('property unit',fields=["*"], filters = [['property','in', dic_to_array(properties) ]]) 
  leases = frappe.get_list('lease',fields=["*"], filters = [['property_unit','in', dic_to_array(property_units) ]])
  lease_instalments = frappe.get_list('lease_instalment',fields=["*"], filters = [['lease','in', dic_to_array(leases) ]])
  result = {'properties' : properties,'property_units':property_units,
            'leases': leases,'lease_instalments':lease_instalments }
  return result  

#report page



def dic_to_array(dics):
  array = []
  for dic in dics:
    array.append(dic.name)
  return array

def dic_to_array__property_unit(dics):
  array = []
  for dic in dics:
    array.append(dic.property_unit)
  return array  




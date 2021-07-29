
import frappe
import frappe.utils
from frappe.utils.oauth import get_oauth2_authorize_url, get_oauth_keys, login_via_oauth2, login_oauth_user as _login_oauth_user, redirect_post_login
import json
from frappe import _
from frappe.auth import LoginManager
from frappe.integrations.doctype.ldap_settings.ldap_settings import get_ldap_settings
import time
import datetime
from datetime import date, timedelta
from frappe.model.document import Document

from udeer.custom_functions.custom import get_units_by_customer, get_property_by_unit, get_m_issues_by_customer, dic_to_array, dic_to_array__property_unit, get_company, get_current_user


@frappe.whitelist(allow_guest=True)
def next_payment(customer):
    customer = json.loads(customer)
    leases = frappe.get_list(
        'Lease', fields=["*"], filters=[['renter', '=', customer]])
    # next_payments = []
    next_payment = None
    for lease in leases:
        lease_instalments = frappe.get_list(
            'Lease Instalment',
            fields=["*"],
            filters=[['lease', '=', lease.name], ['status', '=', 'not paid']])
        for lease_instalment in lease_instalments:
            # next_payments.append(lease_instalment.due_date)
            if (str(lease_instalment.due_date) < str(next_payment)):
                next_payment = lease_instalment.due_date
    return next_payment


def all_next_payments(customer):
    leases = frappe.get_list(
        'Lease', fields=["*"], filters=[['renter', '=', customer]])
    next_payments = []
    for lease in leases:
        lease_instalments = frappe.get_list(
            'Lease Instalment',
            fields=["*"],
            filters=[['lease', '=', lease.name], ['status', '=', 'not paid']])
        for lease_instalment in lease_instalments:
            next_payments.append(lease_instalment.due_date)
    return next_payments


@frappe.whitelist(allow_guest=True)
def activity(customer):
    customer = json.loads(customer)
    leases = frappe.get_list(
        'Lease', fields=["*"], filters=[['renter', '=', customer]])
    lease_instalments = frappe.get_list(
        'Lease Instalment',
        fields=["*"],
        filters=[['lease', 'in', dic_to_array(leases)],
                 ['status', '=', 'paid']])
    maintenance_order = frappe.get_list(
        'Issue',
        fields=["*"],
        filters=[['Customer', '=', customer], ['type', '=', 'maintenance']])
    result = {
        'leases': leases,
        'maintenance_order': maintenance_order,
        'lease_instalments': lease_instalments
    }
    return result


@frappe.whitelist(allow_guest=True)
def my_leases(customer):
    customer = json.loads(customer)
    expired_leases = frappe.get_list(
        'Lease',
        fields=["*"],
        filters=[['renter', '=', customer], ['active', '=', 0]])
    active_leases = frappe.get_list(
        'Lease',
        fields=["*"],
        filters=[['renter', '=', customer], ['active', '=', 1]])
    result = {'active_leases': active_leases, 'expired_leases': expired_leases}
    return result


@frappe.whitelist(allow_guest=True)
def calender(customer):
    customer = json.loads(customer)
    next_payments = all_next_payments(customer)
    maintinance = get_m_issues_by_customer(customer)
    result = {'maintinance': maintinance, 'next_payments': next_payments}
    return result


@frappe.whitelist(allow_guest=True)
def my_address(customer):
    customer = json.loads(customer)
    customer = frappe.get_doc('Customer', customer)
    units = get_units_by_customer(customer.name)
    responde = {}
    for unit in units:
        responde[unit.name] = {}
        responde[unit.name]['unit'] = unit
        responde[unit.name]['property'] = get_property_by_unit(unit.name)
    return responde


@frappe.whitelist(allow_guest=True)
def office_contact():
    user = get_current_user()
    company = frappe.get_doc('Company', user.company)
    return company


@frappe.whitelist(allow_guest=True)
def customer_properties(customer):
    customer = json.loads(customer)
    leases = frappe.get_list(
        'Lease', fields=["*"], filters=[['renter', '=', customer]])
    properties = frappe.get_list('Property', fields=["*"])
    property_units = frappe.get_list(
        'Property Unit',
        fields=["*"],
        filters=[['property', 'in', dic_to_array(properties)]])
    leases = frappe.get_list(
        'Lease',
        fields=["*"],
        filters=[['property_unit', 'in', dic_to_array(property_units)]])
    lease_instalments = frappe.get_list(
        'Lease Instalment',
        fields=["*"],
        filters=[['lease', 'in', dic_to_array(leases)]])

    result = {
        'properties': properties,
        'property_units': property_units,
        'leases': leases,
        'lease_instalments': lease_instalments
    }
    return result


@frappe.whitelist(allow_guest=True)
def index_owner(owner):
    owner = json.loads(owner)
    owner = frappe.get_doc('Property Owner', owner)
    result = {}
    properties = frappe.get_list(
        'Property', filters=[['property_owner', '=', owner.name]])
    property_units = frappe.get_list(
        'Property Unit',
        filters=[['property', 'in', dic_to_array(properties)]])
    leases = frappe.get_list(
        'Lease',
        filters=[['property_unit', 'in', dic_to_array(property_units)]])
    # empty_property_units,full_property_units = []
    # for unit in property_units:
    #   full_property_units.append(unit)
    result = {
        'properties': properties,
        'property_units': property_units,
        'leases': leases
    }
    return result


@frappe.whitelist(allow_guest=True)
def index_manager():
    properties = frappe.get_list('Property')
    leases = frappe.get_list('Lease', fields=["*"])
    expired_leases = frappe.get_list(
        'Lease', fields=["*"], filters=[['active', '=', 0]])
    empty_property_units = frappe.get_list(
        'Property Unit',
        filters=[['name', 'not in', dic_to_array__property_unit(leases)]])
    full_property_units = frappe.get_list(
        'Property Unit',
        filters=[['name', 'in', dic_to_array__property_unit(leases)]])
    income = frappe.get_list(
        'Receipt', fields=["*"], filters=[['type', '=', 'catch']])
    outcome = frappe.get_list(
        'Receipt', fields=["*"], filters=[['type', '=', 'pay']])
    result = {
        'leases': leases,
        'expired_leases': expired_leases,
        'empty_property_units': empty_property_units,
        'full_property_units': full_property_units,
        'income': income,
        'outcome': outcome
    }
    return result


@frappe.whitelist(allow_guest=True)
def property_report(owner):
    owner = json.loads(owner)
    properties = frappe.get_list(
        'Property', fields=["*"], filters=[['property_owner', '=', owner]])
    return properties


@frappe.whitelist(allow_guest=True)
def leases_report(owner):
    owner = json.loads(owner)
    properties = frappe.get_list(
        'Property', filters=[['property_owner', '=', owner]])

    return result


@frappe.whitelist(allow_guest=True)
def property_data(owner):
    property_name = json.loads(property_name)
    property_data = frappe.get_doc('Property', property_name)
    units = frappe.get_list(
        'Property Unit', filters=[['property_owner', '=', owner]])
    result = {"property_data": property_data, 'units': units}
    return result


@frappe.whitelist(allow_guest=True)
def property_unit_data(owner):
    owner = json.loads(owner)
    properties = frappe.get_list(
        'Property', fields=["*"], filters=[['property_owner', '=', owner]])
    return properties


@frappe.whitelist(allow_guest=True)
def open_maintenance_issues(owner):
    owner = json.loads(owner)
    properties = dic_to_array(
        frappe.get_list('Property', filters=[['property_owner', '=', owner]]))
    property_units = dic_to_array(
        frappe.get_list(
            'Property Unit', filters=[['property', 'in', properties]]))
    maintenance_list = frappe.get_list(
        'Issue',
        fields=["*"],
        filters=[['property_unit', 'in', property_units],
                 ['type', '=', 'maintenance'], ['status', '=', 'Open']])
    return maintenance_list


@frappe.whitelist(allow_guest=True)
def maintenance_issues(owner):
    owner = json.loads(owner)
    properties = dic_to_array(
        frappe.get_list('Property', filters=[['property_owner', '=', owner]]))
    property_units = dic_to_array(
        frappe.get_list(
            'Property Unit', filters=[['property', 'in', properties]]))
    maintenance_list = frappe.get_list(
        'Issue',
        fields=["*"],
        filters=[['property_unit', 'in', property_units],
                 ['type', '=', 'maintenance']])
    return maintenance_list


# report page
@frappe.whitelist(allow_guest=True)
def properties_report(owner):
    owner = json.loads(owner)
    properties = frappe.get_list(
        'Property', fields=["*"], filters=[['property_owner', '=', owner]])
    property_units = frappe.get_list(
        'Property Unit',
        fields=["*"],
        filters=[['property', 'in', dic_to_array(properties)]])
    leases = frappe.get_list(
        'Lease',
        fields=["*"],
        filters=[['property_unit', 'in', dic_to_array(property_units)]])
    lease_instalments = frappe.get_list(
        'Lease Instalment',
        fields=["*"],
        filters=[['lease', 'in', dic_to_array(leases)]])
    result = {
        'properties': properties,
        'property_units': property_units,
        'leases': leases,
        'lease_instalments': lease_instalments
    }
    return result


@frappe.whitelist(allow_guest=True)
def lease_report(owner):
    owner = json.loads(owner)
    properties = frappe.get_list(
        'Property', fields=["*"], filters=[['property_owner', '=', owner]])
    property_units = frappe.get_list(
        'Property Unit',
        fields=["*"],
        filters=[['property', 'in', dic_to_array(properties)]])
    leases = frappe.get_list(
        'Lease',
        fields=["*"],
        filters=[['property_unit', 'in', dic_to_array(property_units)]])
    lease_instalments = frappe.get_list(
        'Lease Instalment',
        fields=["*"],
        filters=[['lease', 'in', dic_to_array(leases)]])
    result = {'leases': leases, 'lease_instalments': lease_instalments}
    return result


# customer page

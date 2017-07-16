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

no_cache = True


@frappe.whitelist(allow_guest=True)
def registration(data):
    data = json.loads(data)
    role = frappe.get_doc({"doctype": "DocPerm", "role": "Administrator"})
    company = frappe.get_doc({
        "doctype": "Company",
        "company_name": data["company_name"],
        "abbr": data["abbr"],
        "default_currency": data["currency"]
    })

    company = company.insert()
    address = frappe.get_doc({
        "doctype": "Address",
        "address_type": "Personal",
        "address_title": company.name + "_address",
        "address_line1": data["address"],
        "country": data["country"],
        "city": data["city"],
        "company": company.name,
    })
    address = address.insert()
    user = frappe.get_doc({
        "doctype": "User",
        "company": company.name,
        "email": data["email"],
        "first_name": data["first_name"],
    })
    user.append("permissions", role)
    user = user.insert()
    contact = frappe.get_doc({
        "doctype": "Contact",
        "first_name": data["first_name"],
        "phone": data["mobile_number"],
        "mobile_no": data["telephone_number"],
        "user": user.name,
    })
    contact.append("permissions", role)
    contact = contact.insert()
    return contact


@frappe.whitelist(allow_guest=True)
def add_cumpany_balance(docname, amount):
    role = frappe.get_doc({"doctype": "DocPerm", "role": "Administrator"})
    company = frappe.get_doc("Company", docname)
    company.balance += int(amount)
    company.append("permissions", role)
    result = company.save()
    return result


@frappe.whitelist(allow_guest=True)
def get_current_user():
    user_id = frappe.auth.get_logged_user()
    user = frappe.get_doc('User', user_id)
    return user


@frappe.whitelist(allow_guest=True)
def update_user(name, data):
    data = json.loads(data)
    name = json.loads(name)
    user = frappe.get_doc('User', name)
    user.mobile_number = data['mobile_number']
    user.first_name = data['first_name']
    if (data.user_roles):
        user.roles = data.user_roles
    user.save()
    return user


@frappe.whitelist(allow_guest=True)
def update_company(name, data):
    data = json.loads(data)
    name = json.loads(name)
    company = frappe.get_doc('Company', name)
    if (company.logo):
        company.logo = data['logo']
    company.longitude = data['longitude']
    company.latitude = data['latitude']
    company.save()
    return company


@frappe.whitelist(allow_guest=True)
def get_company():
    user = get_current_user()
    company = frappe.get_doc('Company', user.company)
    return company


@frappe.whitelist(allow_guest=True)
def get_current_company():
    user = get_current_user()
    company = frappe.get_doc('Company', user.company)
    return company


@frappe.whitelist()
def test(doc_name):
    doc_name = json.loads(doc_name)
    doctype = frappe.get_doc('DocType', doc_name)
    return doctype.fields


@frappe.whitelist()
def get_units_by_customer(customer):
    leases = frappe.get_list(
        'lease', fields=["*"], filters=[['renter', '=', customer]])
    units = []
    for lease in leases:
        units.append(frappe.get_doc('property unit', lease.property_unit))
    return units


@frappe.whitelist(allow_guest=True)
def get_m_issues_by_customer(customer):
    leases = frappe.get_list(
        'Lease', fields=["*"], filters=[['renter', '=', customer]])
    issues = frappe.get_list(
        'Issue',
        fields=["*"],
        filters=[['property_unit', 'in', dic_to_array__property_unit(leases)],
                 ['type', '=', 'maintenance']])
    return issues


@frappe.whitelist()
def get_property_by_unit(unit_name):
    unit = frappe.get_doc('Property Unit', unit_name)
    property_doc = frappe.get_doc('Property', unit.property)
    return property_doc


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


@frappe.whitelist()
def delete_role(doctype, d):
    print '////////////////////////////'
    admin = frappe.get_doc('User', 'Administrator')
    for role in admin.roles:
        print role.role
        if (role.role == doctype.name):
            admin.roles.remove(role)
            print 'remove'
            admin.save()


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
       "address_title": company.name+"_address",
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
def add_cumpany_balance(docname,amount):
  role = frappe.get_doc({"doctype": "DocPerm", "role": "Administrator"})
  company = frappe.get_doc("Company",docname)
  company.balance += int(amount)
  company.append("permissions", role)
  result = company.save()
  return result

@frappe.whitelist(allow_guest=True)
def get_user():
  role = frappe.get_doc({"doctype": "DocPerm", "role": "Administrator"})
  user_id = frappe.auth.get_logged_user()
  user = frappe.get_doc('User',user_id)
  return user  

@frappe.whitelist(allow_guest=True)
def update_user(data):
  data = json.loads(data)
  role = frappe.get_doc({"doctype": "DocPerm", "role": "Administrator"})
  user_id = frappe.auth.get_logged_user()
  user = frappe.get_doc('User',user_id)
  user.mobile_number = data['mobile_number']
  user.first_name = data['first_name']
  user.save()
  return user  

@frappe.whitelist(allow_guest=True)
def update_company(data):
  data = json.loads(data)
  role = frappe.get_doc({"doctype": "DocPerm", "role": "Administrator"})
  user = get_user()
  company = frappe.get_doc('Company',user.company)
  company.logo = data['logo']
  company.save()
  return company  

@frappe.whitelist(allow_guest=True)
def get_company():
  role = frappe.get_doc({"doctype": "DocPerm", "role": "Administrator"})
  user = get_user()
  company = frappe.get_doc('Company',user.company)
  return company  

@frappe.whitelist(allow_guest=True)
def test():
  return "result"


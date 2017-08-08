
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

@frappe.whitelist()
def custom_re(data):
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
    return "sss"


@frappe.whitelist()
def late_payment(lease_id):
    lease = frappe.get_doc("Lease",lease_id)
    mos_period = daterange(date.today(),lease.lease_starting_date )
    rents = frappe.get_all("Lease Rent Payment", fields=["from_date", "to_date"],filters = {"lease": ("like", lease_id)})
    for r in rents:
      period = daterange(r.from_date,r.to_date)
      for p in period:
        mos_period.remove(p)

    return mos_period

@frappe.whitelist()
def late_payment_p(p_id):
    p_u = frappe.get_all("Property Unit", fields=["name"], filters = {"property": ("like", p_id)})
    pu_ids=[]
    for p in p_u:
      pu_ids.append(p["name"])
    mos_period = {}
    leases = frappe.get_all("Lease", fields=["name","lease_starting_date"], filters = {"property_unit": ("in", pu_ids)})
    for lease in leases:
      mos_period[lease.name] = daterange(date.today(),lease.lease_starting_date )
      rents = frappe.get_all("Lease Rent Payment", fields=["from_date", "to_date"], filters = {"lease": ("like", lease.name)})
      for r in rents:
        period = daterange(r.from_date,r.to_date)
        for p in period:
          mos_period[lease.name].remove(p)


    return mos_period


def daterange( start_date, end_date ):
    c_list = []
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            c_list.append(start_date + timedelta( n ))
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            c_list.append(start_date - timedelta( n ))
    return c_list

@frappe.whitelist()
def add_company_balance(docname,amount):
  role = frappe.get_doc({"doctype": "DocPerm", "role": "Administrator"})
  company = frappe.get_doc("Company",docname)
  company.balance += int(amount)
  company.append("permissions", role)
  result = company.save()
  return result

@frappe.whitelist(allow_guest=True)
def test():
  return "result"

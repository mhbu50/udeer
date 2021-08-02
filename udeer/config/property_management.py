from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Property"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Property",
                    "label": _("Property")
                },
                {
                    "type": "doctype",
                    "name": "Property Unit",
                    "label": _("Property Unit")
                },
                {
                    "type": "doctype",
                    "name": "Property Document",
                    "label": _("Property Document")
                },
                {
                    "type": "doctype",
                    "name": "Property Expense",
                    "label": _("Property Expense")
                },
                  {
                    "type": "doctype",
                    "name": "Sell Agreement",
                    "label": _("Sell Agreement"),
                },
                {
                    "type": "doctype",
                    "name": "Property Management Contract",
                    "label": _("Property Management Contract")
                },              
                {
                    "type": "doctype",
                    "name": "Pay Receipt",
                    "label": _("Pay Receipt")
                },
                {
                    "type": "doctype",
                    "name": "Property Image",
                    "label": _("Property Image")
                },

                {
                    "type": "doctype",
                    "name": "Unit Activity",
                    "label": _("Unit Activity")
                }
            ]
        },
        {
            "label": _("Master Data"),
            "items": [
                
                {
                    "type": "doctype",
                    "name": "Property Type",
                    "label": _("Property Type")
                }, 
                {
                    "type": "doctype",
                    "name": "Unit Type",
                    "label": _("Unit Type")
                },
                {
                    "type": "doctype",
                    "name": "Property Status",
                    "label": _("Property Status")
                },
                          {
                    "type": "doctype",
                    "name": "Store Type",
                    "label": _("Store Type")
                },
                {
                    "type": "doctype",
                    "name": "File Type",
                    "label": _("File Type"),
                    "description": _("To make Customer based incentive schemes.")
                },
                {
                    "type": "doctype",
                    "name": "Property Owner",
                    "label": _("Property Owner")
                },
            ]
        }
    ]

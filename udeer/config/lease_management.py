from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Lease"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Lease",
                    "label": _("Property")
                },
                {
                    "type": "doctype",
                    "name": "Lease Installment",
                    "label": _("Lease Installment")
                },
                {
                    "type": "doctype",
                    "name": "Lease Rent Payment ",
                    "label": _("Lease Rent Payment ")
                },
                {
                    "type": "doctype",
                    "name": "Lease Documents",
                    "label": _("Lease Documents")
                },
                {
                    "type": "doctype",
                    "name": "Lease Expenses",
                    "label": _("Lease Expenses")
                },
                {
                    "type": "doctype",
                    "name": "Lease Pattern",
                    "label": _("Lease Pattern"),
                },

                {
                    "type": "doctype",
                    "name": "Lease Receipt",
                    "label": _("Lease Receipt")
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

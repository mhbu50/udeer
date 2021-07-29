# coding=utf-8

from frappe import _

def get_data():
	return [
		{
			"module_name": "Udeer",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Udeer")
		},
		{
			"module_name": "Property Management",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"hidden": 0,
			"label": _("Property Management")
		},
		{
			"module_name": "Lease Management",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"hidden": 0,
			"label": _("Lease Management")
		},
		{
			"module_name": "Shared Management",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"hidden": 0,
			"label": _("Shared Management")
		},
		{
			"module_name": "Complain Management",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"hidden": 0,
			"label": _("Complain Management")
		},
		{
			"module_name": "Sales and Shares",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"hidden": 0,
			"label": _("Sales and Shares")
		}

	]

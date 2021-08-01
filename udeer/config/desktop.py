# coding=utf-8

from frappe import _

def get_data():
	return [
		{
			"module_name": "Udeer",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"category": "Modules",
			"label": _("Udeer")
		},
		{
			"module_name": "Property Management",
			"category": "Modules",
			"label": _("Property Management"),
			"color": "#3498db",
			"icon": "octicon octicon-file-directory",
			"type": "module",			
			"description": "Property Management, maintainance and tools."
		},
		{
			"module_name": "Lease Management",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"category": "Modules",
			"type": "module",
			"label": _("Lease Management")
		},
		{
			"module_name": "Shared Management",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"category": "Modules",
			"type": "module",
			"label": _("Shared Management")
		},
		{
			"module_name": "Complain Management",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"category": "Modules",
			"type": "module",
			"label": _("Complain Management")
		},
		{
			"module_name": "Sales and Shares",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"category": "Modules",
			"type": "module",
			"label": _("Sales and Shares")
		}

	]

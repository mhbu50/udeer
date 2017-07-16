from frappe import _

def get_data():
	return [
		{
			"label": _("properties & Units"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "property",
					"description": _("Property"),
				},
				{
					"type": "doctype",
					"name": "property unit",
					"description": _("Uint"),
				}
			]
		},
		{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Lead Details",
					"doctype": "Lead"
				},
				{
					"type": "page",
					"name": "sales-funnel",
					"label": _("Sales Funnel"),
					"icon": "fa fa-bar-chart",
				},
				{
					"type": "report",
					"name": "Prospects Engaged But Not Converted",
					"doctype": "Lead",
					"is_query_report": True
				},

			]
		},
		{
			"label": _("Leases"),
			"icon": "fa fa-star",
			"items": [
            {
                "type": "doctype",
                "name": "lease",
                "description": _("lease"),
            },
				{
					"type": "doctype",
					"name": "external_lease",
					"description": _("external_lease"),
				},
                {
                    "type": "doctype",
                    "name": "sell_agreement",
                    "description": _("sell_agreement"),
                },
                {
                    "type": "doctype",
                    "name": "property_management_contract",
                    "description": _("property_management_contract"),
                },

			]
		},
		{
			"label": _("Setup"),
			"icon": "fa fa-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Campaign",
					"description": _("Sales campaigns."),
				},
				{
					"type": "doctype",
					"label": _("Customer Group"),
					"name": "Customer Group",
					"icon": "fa fa-sitemap",
					"link": "Tree/Customer Group",
					"description": _("Manage Customer Group Tree."),
				},
				{
					"type": "doctype",
					"label": _("Territory"),
					"name": "Territory",
					"icon": "fa fa-sitemap",
					"link": "Tree/Territory",
					"description": _("Manage Territory Tree."),
				},
				{
					"type": "doctype",
					"label": _("Sales Person"),
					"name": "Sales Person",
					"icon": "fa fa-sitemap",
					"link": "Tree/Sales Person",
					"description": _("Manage Sales Person Tree."),
				},
			]
		},
		{
			"label": _("SMS"),
			"icon": "fa fa-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "SMS Center",
					"description":_("Send mass SMS to your contacts"),
				},
				{
					"type": "doctype",
					"name": "SMS Log",
					"description":_("Logs for maintaining sms delivery status"),
				},
				{
					"type": "doctype",
					"name": "SMS Settings",
					"description": _("Setup SMS gateway settings")
				}
			]
		},
		{
			"label": _("Help"),
			"items": [
				{
					"type": "help",
					"label": _("Lead to Quotation"),
					"youtube_id": "TxYX4r4JAKA"
				},
				{
					"type": "help",
					"label": _("Newsletters"),
					"youtube_id": "muLKsCrrDRo"
				},
			]
		},
	]

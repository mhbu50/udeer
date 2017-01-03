# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "udeer"
app_title = "Udeer"
app_publisher = "moosa"
app_description = "udeer app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "moosabukhamsin@gmail.com"
app_license = "MIT"

fixtures = ["Custom Field"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "assets/css/udeer.css"


app_include_js = "assets/js/udeer.js"



# include js, css files in header of web template
# web_include_css = "/assets/udeer/css/udeer.css"
# web_include_js = "/assets/udeer/js/udeer.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "udeer.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "udeer.install.before_install"
# after_install = "udeer.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "udeer.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"udeer.tasks.all"
# 	],
# 	"daily": [
# 		"udeer.tasks.daily"
# 	],
# 	"hourly": [
# 		"udeer.tasks.hourly"
# 	],
# 	"weekly": [
# 		"udeer.tasks.weekly"
# 	]
# 	"monthly": [
# 		"udeer.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "udeer.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "udeer.event.get_events"
# }


// Copyright (c) 2016, moosa and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property Unit', {
	refresh: function (frm) {
		frm.add_custom_button(__('Add Extra'), function () {
			if (frm.is_dirty()) {
				msgprint(__("Please save before make new copy"));
			}
			else {
				var dialog = new frappe.ui.Dialog({
					title: __("Add Many Unit"),
					fields: [
						{
							"fieldtype": "Int", "label": __("Number of Copy"), "fieldname": "number_copy",
							"reqd": 1
						},
						{ "fieldtype": "Button", "label": __("Copy"), "fieldname": "copy" },
					]
				});

				dialog.fields_dict.copy.$input.click(function () {
					var args = dialog.get_values();
					if (!args) return;
					return cur_frm.call({
						doc: cur_frm.doc,
						method: "copy_unit",
						args: args.number_copy,
						callback: function (r) {
							if (r.exc) {
								msgprint(__("There were errors."));
							} else {
								dialog.hide();
								cur_frm.refresh();
							}
						},
						btn: this
					})
				});
				dialog.show();
			}
		});

	}
});

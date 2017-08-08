// Copyright (c) 2017, moosa and contributors
// For license information, please see license.txt

frappe.ui.form.on('Lease Installment', {
	onload: function(frm) {
		frm.set_indicator_formatter('status',
			function(doc) {
				let indicator = 'orange';
				if (doc.status == 'Overdue') {
					indicator = 'red';
				}
				else if (doc.status == 'Not Paid') {
					indicator = 'dark grey';
				}
				else if (doc.status == 'Paid') {
					indicator = 'green';
				}
				return indicator;
			}
		);

	}
});

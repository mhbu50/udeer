// Copyright (c) 2016, moosa and contributors
// For license information, please see license.txt

frappe.ui.form.on('Lease', {
  onload: function (frm) {
    console.log("frm.doc.property_unit", frm.doc.property_unit);
    if (frm.doc.property_unit && frm.doc.__islocal) {
      frappe.db.get_doc("Property Unit", frm.doc.property_unit)
        .then(doc => frm.set_value("property", doc.property),
          frm.refresh_field('property'))
    }
  }
});
// Copyright (c) 2016, moosa and contributors
// For license information, please see license.txt

frappe.ui.form.on('Lease', {
  onload: function(frm) {
    console.log("frm.doc.property_unit", frm.doc.property_unit);
    if (frm.doc.property_unit && frm.doc.__islocal) {
      let pu = frappe.get_doc("Property Unit", frm.doc.property_unit);
      frm.set_value("property", pu.property);
      frm.refresh_field('property');
      console.log("pu", pu);


    }

  }
});
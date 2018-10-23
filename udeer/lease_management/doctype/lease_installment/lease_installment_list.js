frappe.listview_settings['Lease Installment'] = {
  add_fields: ["status"],
  filters: {
    "status": ["!=", "Not Active"]
  },
  get_indicator: function(doc) {
    if (doc.status == "Paid") {
      return [__("Paid"), "green"];
    } else if (doc.status == "Not Paid") {
      return [__("Not Paid"), "orange"];
    } else if (doc.status == "Not Active") {
      return [__("Not active"), "darkgrey"];
    } else if (doc.status == "Overdue") {
      return [__("Overdue"), "red"];
    }
  }
};

frappe.set_route('Lease Installment', {
  "status": ["!=", "Not Active"]
});
frappe.listview_settings['Lease Installment'] = {
  add_fields: ["status"],
  filters:[["status","!=","Not Active"]],
  get_indicator: function (doc) {
    if(doc.status == "Draft") {
			return [__("Draft"), "red", "status,=,Draft"];
		}
    if (doc.status == "Paid") {
      return [__("Paid"), "green", "status,=,Paid"];
    } 
    else if (doc.status == "Not Paid") {
      return [__("Not Paid"), "orange", "status,=,Not Paid"];
    } else if (doc.status == "Not Active") {
      return [__("Not active"), "darkgrey", "status,=,Not Active"];
    } else if (doc.status == "Overdue") {
      return [__("Overdue"), "red","status,=,Overdue"];
    }
  }
};
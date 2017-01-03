frappe.pages['test'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,

		single_column: true
	});
	$(frappe.render_template("test")).appendTo(page.body);
	
	
}
frappe.pages['dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: 0,
		title: 'None',
		single_column: true
	});
	var dash = frappe.render_template('dashboard');
	$('#body_div').append( dash )

}
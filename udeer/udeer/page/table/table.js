frappe.pages['table'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'None',
		single_column: true
	});
	$(frappe.render_template('test', {
			modules: frappe.get_desktop_icons(true)
	})).appendTo(page.main);


	var modules = frappe.get_desktop_icons(true);
	var count=0;
	//var module_name = "Stock";
	for(var i=0;i < modules.length;i++){
		if(modules[i].type==="module" && !modules[i].blocked) {
			callCallbackfunction(modules[i].module_name,count);
			count++;
		}
	}




}
function callCallbackfunction(module_name , i){
	frappe.call({
		method: "frappe.desk.moduleview.get",
		args: {
			module: module_name
		},
		callback: function(r) {

			m = frappe.get_module(module_name);
			// console.log("r.message ",r.message);
			m.data = r.message.data;
      		 console.log("m = ", m);
						$(frappe.render_template('section', m)).appendTo(".sec:eq("+i+")");

		},
		freeze: true,
	});
}


var process_data = function(module_name, data) {
	frappe.module_links[module_name] = [];
	data.forEach(function(section) {
			section.items.forEach(function(item) {
					item.style = '';
					if (item.type === "doctype") {
							item.doctype = item.name;

							// map of doctypes that belong to a module
							frappe.module_links[module_name].push(item.name);
					}
					if (!item.route) {
							if (item.link) {
									item.route = strip(item.link, "#")
							} else if (item.type === "doctype") {
									if (frappe.model.is_single(item.doctype)) {
											item.route = 'Form/' + item.doctype;
									} else {
											if (item.filters) {
													frappe.route_options = item.filters;
											}
											item.route = "List/" + item.doctype
													//item.style = 'font-weight: 500;';
									}
									// item.style = 'font-weight: bold;';
							} else if (item.type === "report" && item.is_query_report) {
									item.route = "query-report/" + item.name
							} else if (item.type === "report") {
									item.route = "Report/" + item.doctype + "/" + item.name
							} else if (item.type === "page") {
									item.route = item.name;
							}
					}

					if (item.route_options) {
							item.route += "?" + $.map(item.route_options, function(value, key) {
									return encodeURIComponent(key) + "=" + encodeURIComponent(value)
							}).join('&')
					}

					if (item.type === "page" || item.type === "help" ||
							(item.doctype && frappe.model.can_read(item.doctype))) {
							item.shown = true;
					}
			});
	});
}

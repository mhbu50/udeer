 
frappe.pages['dash'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		single_column: true
	});
	
	
	// var modules = [{"name":"mod1", "ic":"ic1"},{"name":"mod2", "ic":"ic2"},{"name":"mod3", "ic":"ic3"}] ;
	var modules = frappe.get_desktop_icons(true);
	console.log("mudall",modules);
	// var user = [{"name":"محمد عبدالله", "image":"assets/udeer/images/default_user.png"}] ;
	var user = frappe.user;
	var side_menu_items = [{"content":"aaa", "url":"#1"},{"content":"bbb", "url":"#2"},{"content":"ccc", "url":"#3"}] ;
    
  
  
	console.log("mud0",modules[0])
	$("#body_div").html(frappe.render_template("dash"));
	$("#c-head").html(frappe.render_template("head_menu",{modules:modules,user:user}));
	$("#side_menu").html(frappe.render_template("side_menu",{side_menu_items:side_menu_items }));
	$("#page-content").html(frappe.render_template("content"));

	




	$('.img-circle').click({direction: 'Tools',data: {} }, RoutManager);

	$('.c-menue-item').click({direction: "mud" ,data: {} }, RoutManager);

	
	$('button').click({direction: "test",data: {} }, RoutManager);


	function RoutManager(event) {
    	switch(event.data.direction) {
		    case 'test':


		  //   	frappe.call({
				// 	method: "frappe.www.list.get_list",
				// 	args: {
				// 		doctype: "property",
				// 		txt: "",
				// 		filters: {
				// 			"name": "pro000003"},
				// 		limit_start: 0
						
				// 	},
				// 	callback: function(r) {
				// 	result=r;
				// 	console.log(result)
				// 	// $("#page-content").html(frappe.render_template("list",result));
					
				// 	},
				// 	freeze: true,
				// });
 				
 				// debugger;
 				$.ajax({
		    		url: "‫‪/",
		    		dataType: "json",
					data: {
						cmd:"frappe.desk.form.load.getdoctype",
						doctype:"property",
						with_parent:1
					},
					type: 'get',
					dataType: 'json',
					async: undefined,
					headers: { "X-Frappe-CSRF-Token": frappe.csrf_token },
					cache: false,
		    		success: function(result){

			        	console.log(result);
			        	$("#page-content").html(frappe.render_template("list",result));
			    	}
			    });
 				
					        

		        
		        
				
		        
		   
		        break;
		    case 'test2':
		        
		    	frappe.call({
					method: "frappe.website.router.get_page_context",
					args: {
						path: "/desk",
						
					},
					callback: function(r) {
					result=r;
					console.log(result)
					
					
					},
					freeze: true,
				});
		        
		        
				
		        
		   
		        break;    
		    case 'mud':
		        $("#page-content").html(frappe.render_template("test2"));
		        frappe.call({
					method: "frappe.desk.moduleview.get",
					args: {
						module: this.id
					},
					callback: function(r) {
						
						var m = {};
						m.data = r.message.data;
						$("#side_menu").html(frappe.render_template("side_menu2",m));

						

					},
					freeze: true,
				});
				icon = getIconByLabel(this.id,modules)
				$(document).ajaxStop(function () {
					$("#side_menu  a li").css("background-color", icon.color)
				});
				

		        
		        break;
		    default:
		        
		}
	}
	

	function getIconByLabel(label, modules) { 
		return modules.filter(function(obj) { 
			if(obj._label == label)
			 { 
			 	return obj } 
			 })[0] 
	}    
	
}

// doctype: "{{ doctype }}",
// 			txt: "{{ txt or '' }}",
// 			limit_start: next_start,
// 			pathname: location.pathname,
// 			is_web_form: "{{ is_web_form }}"
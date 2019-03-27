// Copyright (c) 2019, Ayushi Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sprint', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on('Sprint', 'onload', function(frm) {
     
    frappe.call({
        "method": "project_management.project_management_system.doctype.task.task.get_task_list_by_sprint",
        args: {
            "sprint":frm.doc.name
        },
        callback: function (r,rt) {
            console.log(r.message)
            frm.doc.project_task = []
			$.each(r.message|| [], function(i, d) {
			    var child = frm.add_child("project_task");
				frappe.model.set_value(child.doctype, child.name, "task_id", r.message[i].name);
				frappe.model.set_value(child.doctype, child.name, "task_name", r.message[i].task_name);
 				frappe.model.set_value(child.doctype, child.name, "task_status", r.message[i].status);
				frappe.model.set_value(child.doctype, child.name, "priority", r.message[i].priority);
				frappe.model.set_value(child.doctype, child.name, "estimated_start_date", r.message[i].estimated_start_date);
				frappe.model.set_value(child.doctype, child.name, "time", r.message[i].time);
				frappe.model.set_value(child.doctype, child.name, "estimated_end_date", r.message[i].estimated_end_date);
				frappe.model.set_value(child.doctype, child.name, "task_progress", r.message[i].task_progress);
				frappe.model.set_value(child.doctype, child.name, "details", r.message[i].details);
			});
			refresh_field("project_task");
        }
    })
});

cur_frm.get_field("project_task").grid.cannot_add_rows = true;


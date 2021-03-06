// Copyright (c) 2019, Ayushi Patel and contributors
// For license information, please see license.txt

cur_frm.get_field("sprints").grid.cannot_add_rows = true;

cur_frm.get_field("tasks").grid.cannot_add_rows = true;

frappe.ui.form.on('Project', 'onload', function(frm) {
     
    frappe.call({
        "method": "project_management.project_management_system.doctype.task.task.get_task_list_by_project",
        args: {
            "project":frm.doc.name
        },
        callback: function (r,rt) {
            console.log(r.message)
            frm.doc.tasks = []
			$.each(r.message|| [], function(i, d) {
				var child = frm.add_child("tasks");
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
			refresh_field("tasks");
        }
    })
            
    frappe.call({
        "method": "project_management.project_management_system.doctype.sprint.sprint.get_sprint_list_by_project",
        args: {
            "project":frm.doc.name
        },
        callback: function (r1,rt) {
            console.log(r1.message)
            frm.doc.sprints = []
			$.each(r1.message|| [], function(i, d) {
				 var child = frm.add_child("sprints");
				 frappe.model.set_value(child.doctype, child.name, "sprint_name", r1.message[i].name);
 				 frappe.model.set_value(child.doctype, child.name, "start_date", r1.message[i].start_date);
				 frappe.model.set_value(child.doctype, child.name, "end_date", r1.message[i].end_date);
				 frappe.model.set_value(child.doctype, child.name, "duration", r1.message[i].duration);
			});
			refresh_field("sprints");
        }
    })
            
});




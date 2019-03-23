// Copyright (c) 2019, Ayushi Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Task', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Task", "setup", function(frm) {
    cur_frm.set_query("task_dependent_on", function(frm) {
        return {
            "filters": [
                ["Task", "project", "=", cur_frm.doc.project],
                ["Task", "task_name", "!=", cur_frm.doc.task_name]
            ]
        };
    });
});



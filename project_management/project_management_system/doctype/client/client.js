// Copyright (c) 2019, Ayushi Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on('Client', {
    first_name: function(frm) {
        frm.doc.full_name = frm.doc.first_name +" " +frm.doc.last_name;
    },
    last_name: function(frm) {
        frm.doc.full_name = frm.doc.first_name +" " +frm.doc.last_name;
    }
    
});

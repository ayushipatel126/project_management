# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ayushi Patel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.nestedset import NestedSet

class Task(NestedSet):
	nsm_parent_field = 'parent_task'
	def validate(self):
		if not self.task_dependent_on == None and self.task_status.upper()=="IN PROGRESS":
			depedant_task=frappe.get_doc("Task",self.task_dependent_on)
			if not depedant_task.task_status == "Complete":
				frappe.throw("Task is dependent on another task. You have to complete it first.")
					

@frappe.whitelist()
def get_task_list_by_project(project):
	return frappe.get_list('Task', filters={'project': project}, fields=['*'])


@frappe.whitelist()
def get_task_list_by_sprint(sprint):
	return frappe.get_list('Task', filters={'sprint': sprint}, fields=['*'])





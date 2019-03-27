# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ayushi Patel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.nestedset import NestedSet

class Task(Document):
	#nsm_parent_field = 'parent_task'
	def validate(self):
		self.validate_weights()
		self.validate_task_dependency()
		self.project_completion_based_on_task()
					
	def project_completion_based_on_task(self):
		if not self.task_name: return
		#total = frappe.db.sql("""select count(task_name) from tabTask where project=%s""", self.name)[0][0]
		task_list = frappe.get_all('Task',filters={'project':self.project},fields=['*'])		
		project = frappe.get_doc('Project', self.project)
		if len(task_list) == 0 :
			project.project_completion_percentage = 0
		else:
			total_weight = 0
			completed_task_weight = 0
			for task in task_list:
				total_weight += task.task_progress
				if task.task_status == "Complete":
					completed_task_weight += task.task_progress
			if total_weight:
				project.project_completion_percentage = (completed_task_weight * 100)/ total_weight
			else:
				project.project_completion_percentage = 0
			project.save()
	
	def validate_task_dependency(self):
		if not self.task_dependent_on == None and self.task_status.upper()=="IN PROGRESS":
			depedant_task=frappe.get_doc("Task",self.task_dependent_on)
			if not depedant_task.task_status == "Complete":
				frappe.throw("Task is dependent on another task. You have to complete it first.")

	def validate_weights(self):
		task_list = frappe.get_all('Task',filters={'project':self.project},fields=['*'])		
		for task in task_list:
			if task.task_progress < 0:
				frappe.throw(_("Task weight cannot be negative"))

@frappe.whitelist()
def get_task_list_by_project(project):
	return frappe.get_list('Task', filters={'project': project}, fields=['*'])


@frappe.whitelist()
def get_task_list_by_sprint(sprint):
	return frappe.get_list('Task', filters={'sprint': sprint}, fields=['*'])





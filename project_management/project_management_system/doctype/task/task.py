# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ayushi Patel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Task(Document):
	pass



@frappe.whitelist()
def get_task_list_by_project(project):
	return frappe.get_list('Task', filters={'project': project}, fields=['*'])


@frappe.whitelist()
def get_task_list_by_sprint(sprint):
	return frappe.get_list('Task', filters={'sprint': sprint}, fields=['*'])





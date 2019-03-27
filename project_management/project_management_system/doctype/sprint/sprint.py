# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ayushi Patel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Sprint(Document):
	pass




@frappe.whitelist()
def get_sprint_list_by_project(project):
	return frappe.get_list('Sprint', filters={'project': project}, fields=['*'])

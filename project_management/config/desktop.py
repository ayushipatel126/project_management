# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Project Management System",
			"color": "#7578f6",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Project Management System")
		},
		{
			"module_name": "Project Management System",
			"icon": "octicon octicon-briefcase",
			"type": "module",
			"custom":1,
			"hidden":0,
			"_doctype":"Company",
			"force_show":1,
			"link": 'List/Company',
			"color": "#7578f6",
			"label": _("Company")
		},{
			"module_name": "Project Management System",
			"icon": "octicon octicon-organization",
			"type": "module",
			"custom":1,
			"hidden":0,
			"_doctype":"Sprint",
			"force_show":1,
			"color": "#7578f6",
			"link": 'List/Sprint',
			"label": _("Sprint")
		},{
			"module_name": "Project Management System",
			"color": "#7578f6",
			"icon": "octicon octicon-checklist",
			"type": "module",
			"custom":1,
			"hidden":0,
			"_doctype":"Task",
			"force_show":1,
			"link": 'List/Task',
			"label": _("Task")
		},{
			"module_name": "Project Management System",
			"color": "#7578f6",
			"icon": "octicon octicon-bug",
			"type": "module",
			"custom":1,
			"hidden":0,
			"_doctype":"Project Bug",
			"force_show":1,
			"link": 'List/Project Bug',
			"label": _("Project Bug")
		},{
			"module_name": "Project Management System",
			"color": "#7578f6",
			"icon": "octicon octicon-organization",
			"type": "module",
			"custom":1,
			"hidden":0,
			"_doctype":"Team",
			"force_show":1,
			"link": 'List/Team',
			"label": _("Team")
		},{
			"module_name": "Project Management System",
			"color": "#7578f6",
			"icon": "octicon octicon-calendar",
			"type": 'module',
			"custom":1,
			"hidden":0,
			"_doctype":"Timesheet",
			"force_show":1,
			"link": 'List/Timesheet',
			"label": _("Time Sheet")
		},
		{
			"module_name": 'Project Management System',
			"color": "#7578f6",
			"icon": "octicon octicon-broadcast",
			"type": 'module',
			"custom":1,
			"hidden":0,
			"_doctype":"Client",
			"force_show":1,
			"link": 'List/Client',
			'standard': 1,
			"label": _("Client")
		},{
			"module_name": "Project Management System",
			"color": "#7578f6",
			"icon": "octicon octicon-terminal",
			"type": 'module',
			"custom":1,
			"hidden":0,
			"_doctype":"Project",
			"force_show":1,
			"link": 'List/Project',
			"label": _("Project")
		}

	]

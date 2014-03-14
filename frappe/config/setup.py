from frappe import _
from frappe.widgets.moduleview import add_setup_section

data = [
	{
		"label": _("Users and Permissions"),
		"icon": "icon-group",
		"items": [
			{
				"type": "doctype",
				"name": "User",
				"description": _("System and Website Users")
			},
			{
				"type": "doctype",
				"name": "Role",
				"description": _("User Roles")
			},
			{
				"type": "page",
				"name": "permission-manager",
				"label": "Permission Manager",
				"icon": "icon-lock",
				"description": _("Set Permissions on Document Types and Roles")
			},
			{
				"type": "page",
				"name": "user-properties",
				"label": _("User Permission Restrictions"),
				"icon": "icon-user",
				"description": _("Set Defaults and Restrictions for Users")
			},
		]
	},
	{
		"label": _("Tools"),
		"icon": "icon-wrench",
		"items": [
			{
				"type": "page",
				"name": "data-import-tool",
				"label": _("Import / Export Data"),
				"icon": "icon-upload",
				"description": _("Import / Export Data from .csv files.")
			},
			{
				"type": "page",
				"name": "modules_setup",
				"label": _("Show / Hide Modules"),
				"icon": "icon-upload",
				"description": _("Show or hide modules globally.")
			},
			{
				"type": "doctype",
				"name": "Naming Series",
				"description": _("Set numbering series for transactions."),
				"hide_count": True
			},
			{
				"type": "doctype",
				"name": "Rename Tool",
				"description": _("Rename many items by uploading a .csv file."),
				"hide_count": True
			},
			{
				"type": "doctype",
				"name": "File Data",
				"description": _("Manage uploaded files.")
			}
		]
	},
	{
		"label": _("Workflow"),
		"icon": "icon-random",
		"items": [
			{
				"type": "doctype",
				"name": "Workflow",
				"description": _("Define workflows for forms.")
			},
			{
				"type": "doctype",
				"name": "Workflow State",
				"description": _("States for workflow (e.g. Draft, Approved, Cancelled).")
			},
			{
				"type": "doctype",
				"name": "Workflow Action",
				"description": _("Actions for workflow (e.g. Approve, Cancel).")
			},
		]
	},
	{
		"label": _("Email"),
		"icon": "icon-envelope",
		"items": [
			{
				"type": "doctype",
				"name": "Outgoing Email Settings",
				"description": _("Set outgoing mail server.")
			},
		]
	},
	{
		"label": _("Customize"),
		"icon": "icon-glass",
		"items": [
			{
				"type": "doctype",
				"name": "Customize Form",
				"description": _("Change field properties (hide, readonly, permission etc.)")
			},
			{
				"type": "doctype",
				"name": "Custom Field",
				"description": _("Add fields to forms.")
			},
			{
				"type": "doctype",
				"name": "Custom Script",
				"description": _("Add custom javascript to forms.")
			}
		]
	},
	{
		"label": _("System"),
		"icon": "icon-cog",
		"items": [
			{
				"type": "page",
				"name": "applications",
				"label": _("Application Installer"),
				"description": _("Install Applications."),
				"icon": "icon-download"
			},
			{
				"type": "doctype",
				"name": "Backup Manager",
				"label": _("Download Backup"),
				"onclick": "frappe.ui.toolbar.download_backup",
				"icon": "icon-download-alt",
				"description": _("Send download link of a recent backup to System Managers"),
				"hide_count": True
			},
			{
				"type": "doctype",
				"name": "Social Login Keys",
				"description": _("Enter keys to enable login via Facebook, Google, GitHub."),
			},
			{
				"type": "doctype",
				"name": "Backup Manager",
				"description": _("Manage cloud backups on Dropbox"),
				"hide_count": True
			},
			{
				"type": "doctype",
				"name": "Scheduler Log",
				"description": _("Log of error on automated events (scheduler).")
			},
		]
	}
]

def get_data():
	out = list(data)
	add_setup_section(out, "frappe", "website", _("Website"), "icon-globe")
	return out
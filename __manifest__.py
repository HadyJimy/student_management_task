# Copyright 2015 ABF OSIELL <https://osiell.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Student Management",
    "version": "16.0.0.0.1",
    "author": "Hady Gamal",
    "license": "AGPL-3",
    "depends": ["base","mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/root_menus.xml",
        "views/students_view.xml",
        "views/teachers_view.xml",
        "views/staff_view.xml",
        "views/course_view.xml",
        "views/unified_person_search.xml",
    ],
    "application": True,
    "installable": True,
}

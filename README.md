# student_management_task
student_management_task task at 7/10/2025
## What is included
- Models: Student, Teacher, Staff, Course
- Shared abstract model: base.person
- Views for list/form for each model
- Constraint: Course must have a Teacher
- Computed fields:
  - Student.age (from dob) — stored and depends on dob
  - Course.average_age (from students' ages)
- Overridden `create` in Student to validate age (18..60) and notify teacher by chatter
- Unified search wizard for searching names across Student, Teacher, Staff
- Unit tests using `odoo.tests.common.TransactionCase`
- Security: basic access rights (update as necessary)
- depand on pdf questions
- it mandatory to test -test-enable in the config
## Installation
1. Place folder `student_management` inside your Odoo addons path.
2. Update apps list and install.
3. To run tests:
   ```bash
   odoo-bin -c <config> --test-enable --stop-after-init -i student_management

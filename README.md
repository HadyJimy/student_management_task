# student_management_task
Structure
Models-Views-Security-Static-tests 

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
 How to install and test the module
- install it by make update app list then take the name of the addon and paste this in the search bar then activate it 
- it mandatory to test -test-enable in the config
  How you handle debugging, conflicts, and inheritance issues in large
Odoo systems.
i handle this by debug in the pycharm then trace where is the problem and prints too
## Installation
1. Place folder `student_management` inside your Odoo addons path.
2. Update apps list and install.
3. To run tests:
   ```bash
   odoo-bin -c <config> --test-enable --stop-after-init -i student_management
Link Vedio 
https://drive.google.com/file/d/1Rc_mCXl_7No3r8BLBbzRYem59TUteg8d/view?usp=drive_link

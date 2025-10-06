from odoo.tests.common import TransactionCase


class TestCourse(TransactionCase):

    # You Must Make In Config File Runner --test-enable to make test work
    def setUp(self,*args,**kwargs):
        super(TestCourse,self).setUp()

        self.course_01_rec=self.env['course.course'].create({
            'name':'TEST Course',
            'description':'DESSSSCRIPTION',
            'teacher_id':1,
            # 'staff_id':1,
        })
    # The name of the Function that i search with it in terminal
    def test_01_course(self):
        course_id=self.course_01_rec
        self.assertRecordValues(course_id,[{
            'name':'TEST Course',
            'description':'DESSSSCRIPTION',
            'teacher_id':1,
            # 'staff_id':1,
        }])
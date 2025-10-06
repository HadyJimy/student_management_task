from odoo.tests.common import TransactionCase
from datetime import date, timedelta

class TestStudent(TransactionCase):


    def setUp(self,*args,**kwargs):
        super(TestStudent,self).setUp()

        self.student_01_rec=self.env['student.student'].create({
            'name':'TEST PERSON STUDENT',
            'date_of_birth': date(2002, 4, 27),
        })
        self.student = self.env['student.student'].create({
            'name': 'Test Student',
            'date_of_birth': date.today() - timedelta(days=365*20),
        })
        self.course = self.env['course.course'].create({
            'name': 'AI Fundamentals',
            'description': 'Intro to AI',
            'teacher_id': 1,
        })

        id_1=self.env['student.student'].create({
            'name': 'Student 2',
            'date_of_birth': date.today() - timedelta(days=365 * 22),
        })
        id_2=self.env['student.student'].create({
            'name': 'Student 3',
            'date_of_birth': date.today() - timedelta(days=365 * 18),
        })
        self.course.student_ids = [(6, 0, [id_1.id, id_2.id])]
    def test_01_age_calculation(self):
        """Ensure student's age is computed correctly."""
        self.assertEqual(self.student.age, 20, "Age calculation is incorrect!")

    def test_01_student(self):
        student_id=self.student_01_rec
        self.assertRecordValues(student_id,[{
            'name': 'TEST PERSON STUDENT',
            'date_of_birth': date(2002, 4, 27),
            'age':23
        }])

    def test_03_average_age_computation(self):
        """Ensure average student age computation works correctly."""
        # Create two more students with known ages

        avg_age = self.course.average_age
        self.assertEqual(round(avg_age, 2), 20.0, "Average age computation is wrong!")

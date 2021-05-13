from django.core.management.base import BaseCommand
from django.contrib.auth.models import  User
from students.models import Student, Group


class Command(BaseCommand):
    help = "Prints to console number of student related objects in a database"

    models =(('student', Student), ('group', Group), ('user', User))

    def add_arguments(self, parser):
        parser.add_argument('models', nargs='+', type=str, help='<model_name model_name...>')


    # def handle(self, *args, **options):
    #     if 'student' in options['models']:
    #         self.stdout.write('Number of students in database: %d' % Student.objects.count())

    def handle(self, *args, **options):
        for name, model in self.models:

            if name in options['models']:
                self.stdout.write('Number of %ss in database: %d' % (name, model.objects.count()))
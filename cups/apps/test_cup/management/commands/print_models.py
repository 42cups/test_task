from django.core.management.base import NoArgsCommand,CommandError
from cups.apps.test_cup import models


# Create django command that prints all project models and the count of objects in every model
# Also:
# duplicate output to STDERR with prefix "error: "
# write bash script which execute your command and save output of stderr into file. File name should be current date with extension .dat
# x =[ i for i in  dir(models) if '__' not in i and i !='models']
class Command(NoArgsCommand):
    m_list =[]
    for i in dir(models):
        if '__' not in i and i !='models':
            m_list.append(i)
    args = 'Just run it'
    help = 'Print models and count models instanses'
    def handle(self, *args, **options):
        for model in self.m_list:
            self.stdout.write('There is -->{}'.format(model))
            try:
                inst = model.objects.all()
                self.stdout.write('It has {} instanses'.format(len(inst)))
            except Exception as e:
                raise CommandError('Ooops, error :{}'.format(e))

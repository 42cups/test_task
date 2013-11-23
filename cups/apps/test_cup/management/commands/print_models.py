from django.core.management.base import NoArgsCommand,CommandError
from django.contrib.contenttypes.models import ContentType

# Create django command that prints all project models and the count of objects in every model
# Also:
# duplicate output to STDERR with prefix "error: "
# write bash script which execute your command and save output of stderr into file. File name should be current date with extension .dat
# x =[ i for i in  dir(models) if '__' not in i and i !='models']
class Command(NoArgsCommand):
    m_list = ContentType.objects.filter(app_label='test_cup')
    args = 'Just run it'
    help = 'Print models and count models instanses'
    def handle(self, *args, **options):
        for model in self.m_list:
            base_class = model.model_class()
            self.stdout.write('There is -->{}'.format(base_class.__name__))
            try:
                inst = base_class.objects.all()
                if len(inst)>1:
                    self.stdout.write('It has {} instances'.format(len(inst)))
                else:
                    self.stdout.write('It has {} instance'.format(len(inst)))
            except Exception as e:
                raise CommandError('error :{}'.format(e))

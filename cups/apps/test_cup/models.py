from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    date_of_birth = models.DateField()
    email = models.EmailField()
    jabber = models.EmailField(blank=True)
    skype = models.CharField(max_length=20,blank=True)
    bio = models.TextField()
    contacts = models.TextField()
    other_contacts = models.TextField(blank=True)
    photo = models.ImageField(blank=True,upload_to='.',null=True,max_length=100, )


    def __unicode__(self):
        return '{} {}'.format(self.name,self.last_name)

class RequestDB(models.Model):
    date = models.DateTimeField()
    body = models.TextField()

    def __unicode__(self):
        return self.date.strftime("%a, %d %b %Y %H:%M:%S")


# Create signal processor that, for every model,
# creates the db entry about the object creation/editing/deletion


class LogStorage(models.Model):
    instance = models.CharField(max_length=100)
    event = models.CharField(max_length=20)
    time_stamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} {} at {}'.format(self.instance,self.event,self.time_stamp.strftime("%a, %d %b %Y %H:%M:%S"))



def get_models():
    m_list = ContentType.objects.filter(app_label='test_cup')
    base_class =[]
    for model in m_list:
            base_class.append(model.model_class())
    return base_class


@receiver(post_delete)
def callback_delete(sender, **kwargs):
        if sender in get_models() and sender!=LogStorage.__module__:
            LogStorage.objects.create(instance=sender.__name__,event='Delete')

@receiver(pre_save)
def callback_create(sender,instance, **kwargs):
    print LogStorage.__module__
    if sender in get_models() and sender.__name__!=LogStorage.__name__ and not instance.id:
        LogStorage.objects.create(instance=sender.__name__,event='Create')


@receiver(post_save)
def callback_change(sender,instance, **kwargs):
    if sender in get_models() and sender.__name__!=LogStorage.__name__ and instance.id:
        LogStorage.objects.create(instance=sender.__name__,event='Update')

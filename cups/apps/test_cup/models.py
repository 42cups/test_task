from django.db import models

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
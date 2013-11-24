from django.db import models

class Person(models.Model):

        name = models.CharField(max_length= 30)
        last_name = models.CharField(max_length= 30)
        bio = models.TextField()
        contacts = models.TextField()

        def __unicode__(self):
                return self.name

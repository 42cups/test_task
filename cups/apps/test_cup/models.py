from django.db import models
# from django.db.models.signals import post_delete, post_save, post_init
# from django.dispatch import receiver

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

	def __unicode__(self):
		return '{} {}'.format(self.name,self.last_name)
#
# class RequestDB(models.Model):
# 	date = models.DateTimeField()
# 	body = models.TextField()
#
# 	def __unicode__(self):
# 		return str(self.pk)
#
# @receiver(post_init,sender = Person)
# def callback_init(sender, **kwargs):
# 	print ('>>>>>>>>>>>>>>> Created! <<<<<<<<<<<<<<<<')
#
# @receiver(post_delete,sender = Person)
# def callback_delete(sender, **kwargs):
# 	print ('>>>>>>>>>>>>>>> Deleted! <<<<<<<<<<<<<<<<')
#
# @receiver(post_save,sender = Person)
# def callback_change(sender, **kwargs):
# 	print ('>>>>>>>>>>>>>>> Changed! <<<<<<<<<<<<<<<<')

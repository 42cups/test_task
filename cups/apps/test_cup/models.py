from django.db import models
# from django.db.models.signals import post_delete, post_save, post_init
# from django.dispatch import receiver

# Create your models here.
class Person(models.Model):

	name = models.CharField(max_length= 30)
	surname = models.CharField(max_length= 30)
	biography = models.TextField()
	contacts = models.TextField()

	def __unicode__(self):
		return self.name
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

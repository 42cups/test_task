from django.conf import settings

def settings_context(request):
	"""
	This function create logic for task context processor.

	"""
	set_dict={}
	dictlist=[]
	for s in dir(settings):
		if '__' not in s:
			set_dict[s]= getattr(settings, s)

	for key, value in set_dict.iteritems():
		temp = [key,value]
		dictlist.append(temp)
	return {'settings_context': dictlist,}
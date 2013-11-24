from django.utils import timezone
from models import RequestDB

class SaveRequestMiddleware(object):

    def process_request(self,request):
        current_date = timezone.now()
        current_request = request
        try :
            RequestDB.objects.create(date= current_date, body= current_request)
        except BufferError:
            pass




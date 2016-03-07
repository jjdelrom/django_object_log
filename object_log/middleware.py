from django.core.exceptions import ObjectDoesNotExist
from object_log.models import LogAction, LogItem
import json

class LogMiddleware(object):
    def process_request(self, request):


        try:
            action = LogAction.objects.get(name=request.path)
        except ObjectDoesNotExist:
            action = LogAction(name=request.path, 
                template=request.path)
            action.save()
        except Exception:
            action = None
             
        if action:              
            # Add log entry
            if not request.user.is_anonymous():

                if request.method == 'GET':
                    meta = request.GET
                elif request.method == 'POST':
                    meta = request.POST
                
                metadata = dict()    
                metadata['method'] = request.method
                metadata[request.method] = meta.dict()

                entry = LogItem(action=action, 
                    user=request.user, 
                    metadata=json.dumps(metadata))
                entry.save()
                
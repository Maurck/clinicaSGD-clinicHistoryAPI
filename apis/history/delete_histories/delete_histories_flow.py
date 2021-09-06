from models.history import History
from utils.utils import json_message

class DeleteHistoriesFlow:

    def __call__(self, request):

        histories = History.objects()

        if len(histories) == 0:
            return json_message("No existen historias")

        for history in histories:
            history.delete()

        return json_message("Historias borradas")

        

        
        

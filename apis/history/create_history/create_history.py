from .create_history_validator import CreateHistoryValidator
from .create_history_flow import CreateHistoryFlow


class CreateHistory:

    def __call__(self, request):

        create_history_validation = CreateHistoryValidator()
        create_history_validation_errors = create_history_validation(request)
        if create_history_validation_errors:
            return create_history_validation_errors

        create_history_flow = CreateHistoryFlow()
        return create_history_flow(request)

            

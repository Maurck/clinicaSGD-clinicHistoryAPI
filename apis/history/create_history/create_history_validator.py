from utils.utils import validate_parameters

create_history_body_schema = {}

class CreateHistoryValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.form, create_history_body_schema)
        return body_validation_errors
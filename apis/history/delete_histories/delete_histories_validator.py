from utils.utils import validate_parameters

delete_histories_query_schema = {
}

class DeleteHistoriesValidator:

    def __call__(self, request):
        query_validation_errors = validate_parameters(request.args, delete_histories_query_schema)
        return query_validation_errors
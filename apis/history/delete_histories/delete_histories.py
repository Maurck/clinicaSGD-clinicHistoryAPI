from .delete_histories_validator import DeleteHistoriesValidator
from .delete_histories_flow import DeleteHistoriesFlow


class DeleteHistories:

    def __call__(self, request):

        delete_histories_validation = DeleteHistoriesValidator()
        delete_histories_validation_errors = delete_histories_validation(request)
        if delete_histories_validation_errors:
            return delete_histories_validation_errors

        delete_histories_flow = DeleteHistoriesFlow()
        return delete_histories_flow(request)

            

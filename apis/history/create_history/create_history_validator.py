from utils.utils import validate_parameters

create_history_body_schema = {
    "patient_name": {
        "required": True,
        "nullable": False
    },
    "patient_dni": {
        "required": True,
        "nullable": False  
    },
    "patient_birth_date": {
        "required": True,
        "nullable": False  
    },
    "patient_sex": {
        "required": True,
        "nullable": False  
    },
    "medic_name": {
        "required": True,
        "nullable": False  
    },
    "diagnostic": {
        "required": True,
        "nullable": False  
    },
    "admision_date": {
        "required": True,
        "nullable": False  
    }
}

class CreateHistoryValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.form, create_history_body_schema)
        return body_validation_errors
from datetime import datetime
from models.history import History
from flask import jsonify
from utils.utils import get_age

class CreateHistoryFlow:

    def __call__(self, request):

        histories = History.objects()

        history_number = 1
        if len(histories) > 0:
            history_number = len(histories) + 1

        new_history = History(
            history_number=history_number,
            patient_name=request.form["patient_name"],
            patient_dni=request.form['patient_dni'],
            patient_birth_date=request.form['patient_birth_date'],
            patient_age=get_age(datetime.strptime(request.form['patient_birth_date'], '%Y-%m-%d')),
            patient_sex=request.form["patient_sex"],
            medic_name=request.form["medic_name"],
            diagnostic=request.form["diagnostic"],
            admision_date=request.form["admision_date"]
        )

        new_history.save()

        return jsonify({"msg":"Historia Guardada"})
        

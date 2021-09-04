from models.history import History
from flask import jsonify

class CreateHistoryFlow:

    def __call__(self, request):

        new_history = History(
            patient_number=request.form['patient_number'],
            patient_name=request.form["patient_name"],
            patient_dni=request.form['patient_dni'],
            patient_birth_date=request.form['patient_birth_date'],
            patient_age=request.form['patient_age'],
            patient_sex=request.form["patient_sex"],
            medic_name=request.form["medic_name"],
            diagnostic=request.form["diagnostic"],
            admision_date=request.form["admision_date"]
        )

        new_history.save()

        return jsonify({"msg":"Historia Guardada"})
        

'''
user.py: Modulo para definir las rutas relacionadas con la API User
'''

from flask import request
from apis.history.create_history.create_history import CreateHistory
from apis.history.get_histories.get_histories import GetHistories
from apis.history.delete_histories.delete_histories import DeleteHistories


def create_routes_history(app):

    @app.route('/history', methods=['POST'])
    def create_history():
        create_history = CreateHistory()
        return create_history(request)

    @app.route('/histories')
    def get_histories():
        get_histories = GetHistories()
        return get_histories(request)

    @app.route('/histories', methods=['DELETE'])
    def delete_histories():
        delete_histories = DeleteHistories()
        return delete_histories(request)


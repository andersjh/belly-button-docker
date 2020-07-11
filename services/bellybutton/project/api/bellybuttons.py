# services/bellybutton/project/api/bellybuttons.py


from sqlalchemy import exc
from flask import Blueprint, request, render_template
from flask_restful import Resource, Api
import os

from project.api.BellyButtonData import BellyButtonData


db_url = os.getenv('DATABASE_URL')
data = BellyButtonData(db_url)

bellybuttons_blueprint = Blueprint('bellybuttons', __name__, 
        template_folder='templates', 
        static_url_path='/api/static', 
        static_folder='static'
        )

api = Api(bellybuttons_blueprint)


@bellybuttons_blueprint.route('/', methods=['GET'])
def index():
    users = data.get_subject_ids()
    return render_template("index.html", user_ids=users)

@bellybuttons_blueprint.route('/bellybuttons/api/v1.0', methods=['GET'])
def show_apis():
    return render_template("api_1.0.html")

class BellybuttonPing(Resource):
    def get(self):
        return_object = {
            'status': 'success',
            'message': 'pong!'
        }
        return return_object, 200


class SubjectListIds(Resource):
    def get(self):
        response_object = data.get_subject_ids()
        return response_object, 200

class AllData(Resource):
    def get(self): 
        response_object = data.get_data_for_all()
        return response_object, 200          

class OneData(Resource):
    def get(self, subject_id):
        response_object = data.get_data_by_user(subject_id)
        return response_object, 200   

class SubjectList(Resource):
    def get(self):
        return data.get_subjects(), 200

class Subject(Resource):
    def get(self, subject_id):
        return data.get_subjects(subject_id), 200                  


api.add_resource(BellybuttonPing, '/bellybuttons/ping')
api.add_resource(SubjectListIds, '/bellybuttons/api/v1.0/ids')
api.add_resource(AllData, '/bellybuttons/api/v1.0/info')
api.add_resource(OneData, '/bellybuttons/api/v1.0/info/<subject_id>')
api.add_resource(SubjectList, '/bellybuttons/api/v1.0/subjects')
api.add_resource(Subject, '/bellybuttons/api/v1.0/subjects/<subject_id>')


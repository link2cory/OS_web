from flask import jsonify
from flask_restful import Resource, fields, marshal_with

from .post_parser import parse_args
from project.model import Activity as Model

activity_response_fields = {
    'name': fields.String,
    'time_start': fields.DateTime(),
    'time_end': fields.DateTime()
}

class Activity(Resource):
    def get(self):
        return jsonify(Model.objects)
    
    @marshal_with(activity_response_fields)
    def post(self):
        # parse the args and save them as a new document 
        activity = Model(**parse_args()).save()

        return activity, 201

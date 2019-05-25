#!/usr/bin/env python



import logging
from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from api.models import CompareWidget
from CustomLogging import DBLogHandler
from api import bcrypt, db, app

compare_blueprint = Blueprint('compare', __name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)
handler = DBLogHandler()
handler.setLevel(logging.WARN)
logger.addHandler(handler)

class CompareSalaryAPI(MethodView):
    """
    API for Compare Salary widget
    TODO: Replace stub with actual functionality
    """
    def get(self):
        return make_response(jsonify({
            'age': 35,
            'occupation': 70,
            'area': 42
        }), 200)

class CompareInAreaAPI(MethodView):
    """
    API for Compare in Area widget
    TODO: Replace stub with actual functionality
    """
    def get(self):
        return make_response(jsonify({
            'age': 27,
            'gender': 52
        }), 200)

compare_blueprint.add_url_rule(
    '/by_salary',
    view_func=CompareSalaryAPI.as_view('compare_salary_api'),
    methods=['GET']
)
compare_blueprint.add_url_rule(
    '/in_area',
    view_func=CompareInAreaAPI.as_view('compare_in_area_api'),
    methods=['GET']
)
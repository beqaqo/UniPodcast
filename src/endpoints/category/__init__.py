from flask_restx import fields
from flask_restx.reqparse import RequestParser

from src.ext import api


category_model = api.model('category', {
                'id': fields.Integer,
                'category': fields.String
            })

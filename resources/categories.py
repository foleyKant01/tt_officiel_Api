from flask_restful import Resource
import json
from helpers.categories import *
from flask import request


class CategoriesApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateCategories()
    
    def get(self, route):
        if route == "readall":
            return GetAllCategories()

        if route == "readsingle":
            return GetSingleCategories()
    
    def delete(self, route):
         if route == "delete":
            return DeleteCategories()
         
    def patch(self, route):
        if route == "update":
            return UpdateCategories()
        
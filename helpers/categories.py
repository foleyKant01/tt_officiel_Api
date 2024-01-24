from flask import request
import uuid
from config.db import db

from model.tt import Categories



def CreateCategories():
    
    response = {}

    try:
        ca_name = request.json.get('name')
        ca_uid = str(uuid.uuid4())

        new_categories = Categories()
        new_categories.ca_name = ca_name
        new_categories.ca_uid = ca_uid
        
        db.session.add(new_categories)
        db.session.commit()

        response['satus'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response


def UpdateCategories():
    response = {}

    try:

        update_categories = Categories.query.filter_by(ca_uid="efa34482-9325-48be-9cac-9875e7fc8991").first()
        
        if update_categories:
            update_categories.ca_name = request.json.get('name', update_categories.ca_name)
     
        db.session.add(update_categories)
        db.session.commit() 
        
        response['status'] = 'success'
        response['message'] = "the categories has been updated!"

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


def DeleteCategories():
    response = {}

    try:
        uid = request.json.get('ca_uid')

        deleteAdvertisement = Categories.query.filter_by(ca_uid=uid).first()

        if deleteAdvertisement:
            db.session.delete(deleteAdvertisement)
            db.session.commit()
            response['status'] = 'success'
        else:
            response['status'] = 'error'
            response['motif'] = 'utilisateur non trouvé'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response



def ReadAllCategories():
    response = {}
    
    try:
        all_categiries = Categories.query.all()

        categories_infos = []

        for categories in all_categiries:
            advertisement_info = {
                'ad_uid': categories.ca_uid,
                'name': categories.ca_name,              
            }
            categories_infos.append(advertisement_info)

        response['status'] = 'success'
        response ['users'] = categories_infos

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def ReadSingleCategories():
    response = {}

    try:
        categories_uid = request.json.get('ca_uid')


        single_categories = Categories.query.filter_by(ca_uid=categories_uid).first()

        categories_info = {
            'ad_uid': single_categories.ca_uid,
            'name': single_categories.ca_name,                
        }

        response['status'] = 'success'
        response['user'] = categories_info

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


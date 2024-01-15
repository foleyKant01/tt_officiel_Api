from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db
from model.tt import User
import bcrypt, jwt
from werkzeug.security import check_password_hash


# liste_users = []
   
def CreateUser():
    reponse = {}

    try:
        u_firstname = (request.json.get('firstname'))
        u_lastname = (request.json.get('lastname'))
        u_username = (request.json.get('username'))
        u_mobile = (request.json.get('mobile'))      
        u_address = (request.json.get('address'))
        u_email = (request.json.get('email'))
        u_password = (request.json.get('password'))
        u_city = (request.json.get('city'))
        u_uid = str(uuid.uuid4())

        hashed_password = bcrypt.hashpw(u_password.encode('utf-8'), bcrypt.gensalt())
        
        new_user = User()
        new_user.u_firstname = u_firstname
        new_user.u_lastname = u_lastname
        new_user.u_username = u_username
        new_user.u_mobile = u_mobile
        new_user.u_address = u_address
        new_user.u_email = u_email
        new_user.u_password = hashed_password
        new_user.u_city = u_city
        new_user.u_uid = u_uid
        
        db.session.add(new_user)
        db.session.commit()

        # nouvel_hotel =(reponse)
        # liste_users.append(nouvel_hotel)

        reponse['status'] = 'Succes'

    # except Exception as e:
    #     reponse['error_description'] = str(e)
    #     reponse['status'] = 'error'
    except:
        reponse['error'] = 'Incorrect data, recheck it'

    return reponse



def ReadAllUser():
    response = {}

    try:
        readAllUser = User.query.all()

        if readAllUser:
            user_informations = []

            for user in readAllUser:
                user_infos = {
                    'u_uid': user.u_uid,
                    'firstname': user.u_firstname,
                    'lastname': user.u_lastname,
                    'username': user.u_username,
                    'mobile': user.u_mobile,
                    'address': user.u_address,
                    'email': user.u_email,                    
                    'city': user.u_city, 
                }

                user_informations.append(user_infos)

            response['status'] = 'success'
            response ['users'] = user_informations
        else:
            response['status'] = 'erreur'
            response['motif'] = 'aucun'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response

def ReadSingleUser():
    response = {}

    try:
        uid = request.json.get('u_uid')

        readSingleUser = User.query.filter_by(u_uid = uid).first()

        if readSingleUser:
            user_infos = {
                'u_uid': readSingleUser.u_uid,
                'firstname': readSingleUser.u_firstname,
                'lastname': readSingleUser.u_lastname,
                'username': readSingleUser.u_username,
                'mobile': readSingleUser.u_mobile,
                'address': readSingleUser.u_address,
                'email': readSingleUser.u_email,                    
                'city': readSingleUser.u_city, 
            }

            response['status'] = 'success'
            response['user'] = user_infos
        else:
            response['status'] = 'erreur'
            response['motif'] = 'aucun'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response



def UpdateUser  ():
    reponse = {}

    try:
        updateuser = User.query.filter_by(u_uid = "b7f45e6f-aecd-4a61-9122-639b71839d74").first()

        if updateuser:
            updateuser.u_firstname = request.json.get('firstname', updateuser.u_firstname)
            updateuser.u_lastname = request.json.get('lastname', updateuser.u_lastname)
            updateuser.u_username = request.json.get('username', updateuser.u_username)            
            updateuser.u_mobile = request.json.get('mobile', updateuser.u_mobile)
            updateuser.u_address = request.json.get('address', updateuser.u_address)
            updateuser.u_email = request.json.get('email', updateuser.u_email)
            updateuser.u_password = request.json.get('password', updateuser.u_password)
            updateuser.u_city = request.json.get('city', updateuser.u_city)

            db.session.add(updateuser)
            db.session.commit()

            reponse['status'] = 'Succes'
        else:
            reponse['status'] = 'User not found'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def DeleteUser():
    response = {}

    try:
        uid = request.json.get('u_uid')

        deleteuser = User.query.filter_by(u_uid=uid).first()

        if deleteuser:
            db.session.delete(deleteuser)
            db.session.commit()
            response['status'] = 'success'
        else:
            response['status'] = 'error'
            response['motif'] = 'utilisateur non trouvé'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response



def LoginUser():
    response = {}
    responses = {}

    try:
        username = request.json.get('username')
        password = request.json.get('password')

        login_user = User.query.filter_by(u_username=username).first()

        if login_user and bcrypt.checkpw(password.encode('utf-8'), login_user.u_password.encode('utf-8')):
            expires = timedelta(hours=1)
            access_token = create_access_token(identity=username)

            response['status'] = 'success'
            response['message'] = 'Login successful'
            response['access_token'] = access_token

        else:
            response['status'] = 'error'
            response['message'] = 'Invalid username or password'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response

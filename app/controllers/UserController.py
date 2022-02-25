from flask import request, Blueprint
from marshmallow import ValidationError

from ..middlewares.AuthenticationMiddleware import Authentication
from ..middlewares.AccessControlMiddleware import AccessControl
from ..utils.CustomResponse import ErrorResponse
from ..services.UserService import UserService
from ..schemas.UserSchema import UserSchema
from ..errors.AppError import AppError

userRoutes = Blueprint('users', __name__)
userSchema = UserSchema()

@userRoutes.route('/', methods=['POST'])
@Authentication.required
@AccessControl.onlyAdmin
def create():
  body = request.get_json();  
  
  try:
    userSchema = UserSchema(only=["email", "fullname", "isAdmin", "password", "role", "orgId"])
    data = userSchema.load(body)
  except ValidationError as err:
    return ErrorResponse(AppError("Validation error", 400, err.messages))
  
  return UserService.createUser(data)

@userRoutes.route('/', methods=['GET'])
@Authentication.required
@AccessControl.onlyAdmin
def list():
  return UserService.list()

@userRoutes.route('/<int:userId>', methods=['GET'])
@Authentication.required
def get(userId):
  return UserService.getUser(userId)


from marshmallow import ValidationError
from flask import request, Blueprint

from ..middlewares.AuthenticationMiddleware import Authentication
from ..middlewares.AccessControlMiddleware import AccessControl
from ..utils.CustomResponse import ErrorResponse
from ..services.OrgService import OrgService
from ..schemas.OrgSchema import OrgSchema
from ..schemas.UserSchema import UserSchema
from ..errors.AppError import AppError

orgRoutes = Blueprint('orgs', __name__)
orgSchema = OrgSchema()

@orgRoutes.route('/', methods=['POST'])
@Authentication.required
@AccessControl.onlyAdmin
def create():
  body = request.get_json();  
  
  try:
    data = orgSchema.load(body)
  except ValidationError as err:
    return ErrorResponse(AppError("Validation error", 400, err.messages))
  
  return OrgService.create(data)

@orgRoutes.route('/', methods=['GET'])
@Authentication.required
@AccessControl.onlyAdmin
def list():
  return OrgService.list()

@orgRoutes.route('/<int:orgId>', methods=['GET'])
@Authentication.required
def get(orgId):
  return OrgService.get(orgId)

@orgRoutes.route('/<int:orgId>/users', methods=['POST'])
@Authentication.required
@AccessControl.onlyManager
@AccessControl.sameOrg
def createUser(orgId):
  body = request.get_json();  
  
  try:
    userSchema = UserSchema(only=["email", "fullname", "role", "password"])
    data = userSchema.load(body)
  except ValidationError as err:
    return ErrorResponse(AppError("Validation error", 400, err.messages))
  
  return OrgService.createUser(orgId, data)

@orgRoutes.route('/<int:orgId>/users', methods=['GET'])
@Authentication.required
@AccessControl.onlyManager
@AccessControl.sameOrg
def listUsers(orgId):
  return OrgService.listUsers(orgId)
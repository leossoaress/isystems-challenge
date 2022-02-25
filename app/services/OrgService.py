from ..utils.CustomResponse import CustomResponse, ErrorResponse
from ..models.OrgUserModel import OrgUserModel
from ..schemas.UserSchema import UserSchema
from ..schemas.OrgSchema import OrgSchema
from ..models.UserModel import UserModel
from ..models.OrgModel import OrgModel
from ..errors.AppError import AppError
  
class OrgService():

  @staticmethod  
  def create(data):
    org = OrgModel(data)
    org.save()
    
    orgSchema = OrgSchema(only=["id"]) 
    return CustomResponse(201, orgSchema.dump(org))
  
  @staticmethod
  def get(userId):
    org = OrgModel.getById(userId)
    if not org:
      return ErrorResponse(AppError(statusCode=404, msg="Org not found"))
    
    orgSchema = OrgSchema() 
    return CustomResponse(200, orgSchema.dump(org))
  
  @staticmethod
  def list():
    orgs = OrgModel.getAll()
    orgSchema = OrgSchema(many=True) 
    return CustomResponse(200, orgSchema.dump(orgs))
  
  @staticmethod
  def createUser(orgId, data):
    org = OrgModel.getById(orgId)
    if not org:
      return ErrorResponse(AppError(statusCode=404, msg="Org not found"))
    
    user = UserModel.getByEmail(data.get('email'))  
    if user:
      return ErrorResponse(AppError(statusCode=409, msg="Email already in use"))
    
    userSchema = UserSchema(only=["email", "fullname", "isAdmin", "password"]) 
    user = UserModel(userSchema.dump(data))
    user.save()
    
    orgUser = OrgUserModel({ 'userId': user.id, 'orgId': orgId, 'role': data.get('role')})
    orgUser.save()
    
    userSchema = UserSchema(only=["id"]) 
    return CustomResponse(200, userSchema.dump(user))
  
  @staticmethod
  def listUsers(orgId):
    org = OrgModel.getById(orgId)
    if not org:
      return ErrorResponse(AppError(statusCode=404, msg="Org not found"))
    
    users = org.users
    userSchema = UserSchema(only=["id", "email", "fullname", "isAdmin"],  many=True) 
    return CustomResponse(200, userSchema.dump(users))
from ..utils.CustomResponse import CustomResponse, ErrorResponse
from ..models.OrgUserModel import OrgUserModel
from ..schemas.UserSchema import UserSchema
from ..models.UserModel import UserModel
from ..models.OrgModel import OrgModel
from ..errors.AppError import AppError

class UserService():

  @staticmethod  
  def createUser(data):
    
    user = UserModel.getByEmail(data.get('email'))  
    if user:
      return ErrorResponse(AppError(statusCode=409, msg="Email already in use"))
    
    org = OrgModel.getById(data.get('orgId'))
    if not org:
      return ErrorResponse(AppError(statusCode=404, msg="Org not found"))
    
    userSchema = UserSchema(only=["email", "fullname", "isAdmin", "password"]) 
    user = UserModel(userSchema.dump(data))
    user.save()
    
    orgUser = OrgUserModel({ 'userId': user.id, 'orgId': data.get('orgId'), 'role': data.get('role')})
    orgUser.save()
    
    userSchema = UserSchema(only=["id"]) 
    return CustomResponse(200, userSchema.dump(user))
  
  @staticmethod
  def getUser(userId):
    
    user = UserModel.getById(userId)
    if not user:
      return ErrorResponse(AppError(statusCode=404, msg="User not found"))
    
    userSchema = UserSchema(only=["id", "email", "fullname", "isAdmin"]) 
    return CustomResponse(200, userSchema.dump(user))
  
  @staticmethod
  def list():
    users = UserModel.getAll()
    userSchema = UserSchema(only=["id", "email", "fullname", "isAdmin"],  many=True) 
    return CustomResponse(200, userSchema.dump(users))
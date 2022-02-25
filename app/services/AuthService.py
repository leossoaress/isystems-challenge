from urllib import response
from ..errors.AppError import AppError
from ..schemas.UserSchema import UserSchema
from ..models.UserModel import UserModel
from ..models.OrgUserModel import OrgUserModel
from ..utils.CustomResponse import CustomResponse, ErrorResponse
from ..utils.JwtToken import JwtToken


def login(email, password):
  
  user = UserModel.getByEmail(email)  
  if not user:
    return ErrorResponse(AppError(statusCode=404, msg="User not found"))
  
  if not user.checkHash(password):
    return ErrorResponse(AppError(statusCode=401, msg="Incorrect password"))
  
  role = "ADMIN" if user.isAdmin else user.orgUsers[0].role
  orgId = -1 if user.isAdmin else user.orgs[0].id
  
  token = JwtToken.generateToken(user.id, role, orgId)
  
  return CustomResponse(statusCode=200, data={'id': user.id, 'token': token})
  
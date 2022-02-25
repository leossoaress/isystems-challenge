from flask import request, Blueprint
from marshmallow import ValidationError

from ..utils.CustomResponse import ErrorResponse
from ..services.AuthService import login
from ..schemas.AuthSchema import AuthSchema
from ..errors.AppError import AppError

authRoutes = Blueprint('auth', __name__)
authSchema = AuthSchema()

@authRoutes.route('/', methods=['POST'])
def create():
  body = request.get_json();  
  
  try:
    data = authSchema.load(body)
  except ValidationError as err:
    return ErrorResponse(AppError("Validation error", 400, err.messages))
  
  return login(data.get('email'), data.get('password'))
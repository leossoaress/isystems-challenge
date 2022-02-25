from functools import wraps
from flask import json, request, Response, g

from ..models.UserModel import UserModel
from ..utils.JwtToken import JwtToken

class Authentication():
  
  def required(func):
    @wraps(func)
    def decorated_auth(*args, **kwargs):
      if 'Authorization' not in request.headers:
        return Response(
          mimetype="application/json",
          response=json.dumps({'error': 'Authentication token is not available, please login to get one'}),
          status=401
        )
      token = request.headers.get('authorization').split()[1]
      data = JwtToken.decodeToken(token)
      print(data)
      if 'error' in data:
        return Response(
          mimetype="application/json",
          response=json.dumps(data['error']),
          status=401
        )
        
      userId = data['payload']['sub']
      role = data['payload']['role']
      org = data['payload']['org']
      
      check_user = UserModel.getById(userId)
      if not check_user:
        return Response(
          mimetype="application/json",
          response=json.dumps({'error': 'user does not exist, invalid token'}),
          status=404
        )
      g.user = {'id': userId, 'role': role, 'org': org}
      return func(*args, **kwargs)
    return decorated_auth
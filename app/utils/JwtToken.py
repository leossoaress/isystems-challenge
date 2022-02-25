import jwt
import os
import datetime

class JwtToken():
  
  @staticmethod
  def generateToken(userId, role, orgId):
    try:
      payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'sub': userId,
        'org': orgId,
        'role': role
      }
      print(payload)
      return jwt.encode(payload, "secret", algorithm="HS256")
    except Exception as e:
      print(e)
      return None
    
  @staticmethod
  def decodeToken(token):
    try:
      print(token)
      payload = jwt.decode(token, "secret", algorithms=["HS256"])
      return {'payload': payload }
    except jwt.ExpiredSignatureError as e1:
      return {'error': { 'message': 'Token expired, please login again' }}
    except jwt.InvalidTokenError:
      return {'error': {'message': 'Invalid token, please try again with a new token'}}
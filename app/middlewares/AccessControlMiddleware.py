from functools import wraps
from flask import Response, json, g, request

class AccessControl():
  
  def onlyAdmin(func):
    @wraps(func)
    def decorated_auth(*args, **kwargs):
      print(g.user)
      if g.user['role'] != "ADMIN":
         return Response(
          mimetype="application/json",
          response=json.dumps({'error': 'Only admin can do this action'}),
          status=401
        )
      return func(*args, **kwargs)
    return decorated_auth
  
  def onlyManager(func):
    @wraps(func)
    def decorated_auth(*args, **kwargs):       
      if g.user['role'] != "MANAGER" and g.user['role'] != "ADMIN":
         return Response(
          mimetype="application/json",
          response=json.dumps({'error': 'Only manager or admin can do this action'}),
          status=401
        )
      return func(*args, **kwargs)
    return decorated_auth
  
  def sameOrg(func):
    @wraps(func)
    def decorated_auth(*args, **kwargs):       
      if g.user['org'] != request.view_args['orgId']:
         return Response(
          mimetype="application/json",
          response=json.dumps({'error': 'Only manager or admin can do this action'}),
          status=401
        )
      return func(*args, **kwargs)
    return decorated_auth
  
  def createUserToSameOrg(func):
    @wraps(func)
    def decorated_auth(*args, **kwargs):   
      if g.user['role'] == "ADMIN": 
        return func(*args, **kwargs)   
      if g.user['org'] != request.get_json()['orgId']:
         return Response(
          mimetype="application/json",
          response=json.dumps({'error': 'You only can create users in you organization'}),
          status=401
        )
      return func(*args, **kwargs)
    return decorated_auth
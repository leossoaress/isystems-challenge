from flask import Response, json
from ..errors import AppError

def CustomResponse(statusCode, data):
  return Response(
    mimetype="application/json",
    response=json.dumps(data),
    status=statusCode
  )
  
def ErrorResponse(appError):
  print(appError.statusCode)
  return Response(
    mimetype="application/json",
    response=json.dumps({ 'message': appError.msg, 'data': appError.data }),
    status=appError.statusCode
  )
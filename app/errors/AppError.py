class AppError():
  
  msg = "Internal Server Error"
  statusCode = 500
  data = {}
  
  def __init__(self, msg, statusCode, data=None):
    self.msg=msg
    self.statusCode=statusCode
    self.data=data
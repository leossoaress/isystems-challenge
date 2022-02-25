import datetime

from app.models import db, bcrypt

class UserModel(db.Model):
  __tablename__ = "user"

  id = db.Column(db.Integer, primary_key=True)
  fullname = db.Column(db.String(256), nullable=False)
  email = db.Column(db.String(256), nullable=False, unique=True)
  password = db.Column(db.String(1024), nullable=False)
  isAdmin = db.Column(db.Boolean, default=False)
  createdAt = db.Column(db.DateTime)
  updatedAt = db.Column(db.DateTime)
  orgUsers = db.relationship("OrgUserModel")
  orgs = db.relationship("OrgModel", secondary="orgUser")
  
  def __init__(self, data):
    self.fullname = data.get('fullname')
    self.email = data.get('email')
    self.password = self.generateHash(data.get('password'))
    self.isAdmin = data.get('isAdmin')
    self.createdAt = datetime.datetime.utcnow()
    self.updatedAt = datetime.datetime.utcnow()
    
  def generateHash(self, password):
    return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")
  
  def checkHash(self, password):
    return bcrypt.check_password_hash(self.password, password)
  
  def save(self):
    db.session.add(self)
    db.session.commit()
    
  @staticmethod
  def getById(id):
    return UserModel.query.get(id)
  
  @staticmethod
  def getByEmail(email):
    return UserModel.query.filter_by(email=email).first()
  
  @staticmethod
  def getAll():
    return UserModel.query.all()
  
    
  def __repr__(self):
      return "<User %r>" % self.email
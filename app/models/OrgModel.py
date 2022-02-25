import datetime

from app.models import db, bcrypt

class OrgModel(db.Model):
  __tablename__ = "org"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(256), nullable=False)
  createdAt = db.Column(db.DateTime)
  updatedAt = db.Column(db.DateTime)
  users = db.relationship("UserModel", secondary="orgUser")
  
  def __init__(self, data):
    self.name = data.get('name')
    self.createdAt = datetime.datetime.utcnow()
    self.updatedAt = datetime.datetime.utcnow()
      
  def save(self):
    db.session.add(self)
    db.session.commit()
    
  @staticmethod
  def getById(id):
    return OrgModel.query.get(id)
  
  @staticmethod
  def getAll():
    return OrgModel.query.all()
  
  def __repr__(self):
      return "<Org %r>" % self.name
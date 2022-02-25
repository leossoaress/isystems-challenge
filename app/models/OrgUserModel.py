import datetime

from app.models import db, bcrypt

class OrgUserModel(db.Model):
  __tablename__ = "orgUser"

  orgId = db.Column(db.Integer, db.ForeignKey('org.id'), primary_key=True)
  userId = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
  role = db.Column(db.String(256), nullable=False)
  createdAt = db.Column(db.DateTime)
  updatedAt = db.Column(db.DateTime)
  org = db.relationship("OrgModel")
  user = db.relationship("UserModel")
  
  def __init__(self, data):
    self.orgId = data.get('orgId')
    self.userId = data.get('userId')
    self.role = data.get('role')
    self.createdAt = datetime.datetime.utcnow()
    self.updatedAt = datetime.datetime.utcnow()
      
  def save(self):
    db.session.add(self)
    db.session.commit()
    
  @staticmethod
  def getByIds(orgId, userId):
    return OrgUserModel.query.filter_by(orgId=orgId, userId=userId).first()
  
  @staticmethod
  def getAll():
    return OrgUserModel.query.all()
  
  def __repr__(self):
      return "<OrgUser %r %r>" % self.orgId % self.userId
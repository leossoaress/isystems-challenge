from marshmallow import Schema, fields, validates_schema, ValidationError

class UserSchema(Schema):
  id = fields.Int(dump_only=True)
  fullname = fields.Str(required=True)
  email = fields.Email(required=True)
  password = fields.Str(required=True)
  isAdmin = fields.Boolean(required=False)
  orgId = fields.Int()
  role = fields.Str()
  createdAt = fields.DateTime(dump_only=True)
  updatedAt = fields.DateTime(dump_only=True)
  
  # @validates_schema
  # def validate_age(self, data, **kwargs):
  #   if (not data['orgId'] or not data['role']) and data['isAdmin'] != True:  
  #     raise ValidationError("You need to set orgId and role when isAdmin is not True")
from marshmallow import Schema, fields

class OrgUserSchema(Schema):
  orgId = fields.Int(dump_only=True)
  userId = fields.Int(dump_only=True)
  role = fields.Str(required=True)
  createdAt = fields.DateTime(dump_only=True)
  updatedAt = fields.DateTime(dump_only=True)
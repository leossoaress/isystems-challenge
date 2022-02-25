from marshmallow import Schema, fields

class OrgSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  createdAt = fields.DateTime(dump_only=True)
  updatedAt = fields.DateTime(dump_only=True)
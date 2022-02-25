from flask_socketio import SocketIO, ConnectionRefusedError, emit
from flask import request

from ..models.UserModel import UserModel
from ..utils.JwtToken import JwtToken

socketio = SocketIO()

sockets = {}
clients = {}

@socketio.on('connect')
def connect(auth):
  data = JwtToken.decodeToken(auth)
  if 'error' in data:
    raise ConnectionRefusedError('Authentication failed')
  
  userId = data['payload']['sub']
  clients[userId] = request.sid
  sockets[request.sid] = userId
  print('Client connect')

@socketio.on('disconnect')
def disconnect():
  del clients[sockets[request.sid]] 
  del sockets[request.sid]
  print('Client disconnected')

@socketio.on('chat')
def forwardMessage(json):
  print('received json: ' + str(json))
  dest = json.get('dest')
  if dest in clients:
    emit('chat', {'message': json.get('message')}, room=clients[dest])
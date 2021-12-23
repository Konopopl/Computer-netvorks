import grpc
import message_pb2
import message_pb2_grpc
import random
import time

def generate_messages():
  print("generating messages")
  messages = [str(i) for i in range(10)]
  for i in range(10):
    message = messages[random.randint(0, len(messages) - 1)]
    print("send message %s" % message)
    yield message_pb2.Message(message = message)

with grpc.insecure_channel('localhost:8080/python-server/') as channel:
  stub = message_pb2_grpc.ServiceStub(channel)
  #while(True):
  response = stub.Channel(generate_messages())
    #for response in responses:
  for r in response:
    print(r)
    

import grpc
import message_pb2
import message_pb2_grpc
import random
import time
from concurrent import futures

class Servicer:
    def __init__(self):
        self.messages = []
        self.count = 0
        self.sum = 0
        self.sumsq = 0
    def Channel(self, request_iterator, context):
        print("started")
        for request in request_iterator:
            print("message received: %s" % request.message)
            message = int(request.message)
            self.messages.append(message)
            self.sum += message
            self.sumsq += message ** 2
            self.count += 1
        ans = "mean is %f, std is %f" % (self.sum/self.count, (self.sumsq/self.count - (self.sum/self.count)**2)**0.5)
        yield message_pb2.SumMessage(sum = self.count, message = ans)
    def Request(self, request, context):
        self.count += 1
        return message_pb2.SumMessage(sum = self.count, message = request.message)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
message_pb2_grpc.add_ServiceServicer_to_server(Servicer(), server)
server.add_insecure_port('[::]:9090')
server.start()
server.wait_for_termination()

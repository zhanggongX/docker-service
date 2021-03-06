from message.api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class MessageServiceHandler:
    def send(self, mobile, message):
        print("sendMobileMessage")
        return True

    def sendEmail(self, email, message):
        print("sendEmailMessage")
        return True

if __name__ == '__main__':
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket("localhost", "9090")
    tfactory = TTransport.TFramedTransportFactory()
    pfacotry = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfacotry)
    print("python thrift server start")
    server.serve()
    print("python thrift server exit")
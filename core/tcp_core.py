# coding:utf-8
from socketserver import BaseRequestHandler, TCPServer
import socket
import threading
import time

client_socket = []


class SeverHandler(BaseRequestHandler):
    def setup(self):
        ip = self.client_address[0].strip()  # 获取客户端的ip
        port = self.client_address[1]  # 获取客户端的port
        print(ip + ":" + str(port) + " is connect!")
        client_socket.append(self.request)  # 保存套接字socket

    def handle(self):
        print('Got connection from', self.client_address, end=' ')
        while True:
            msg = self.request.recv(8192)
            print("[message]", end=' ')
            print(msg)
            if not msg:
                break
            self.request.send("receive success".encode('utf-8'))

    def finish(self):
        print("client is disconnect!")
        client_socket.remove(self.request)


class tcp_server(threading.Thread):
    def __init__(self, port):
        super().__init__()
        self.serv = None
        self.port = port

    def run(self):
        self.serv = TCPServer(
            ('', self.port), SeverHandler, bind_and_activate=False)
        self.serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                    True)
        # Bind and activate
        self.serv.server_bind()
        self.serv.server_activate()
        self.serv.serve_forever()

    def send_data(self, data):
        '''
            Args:
                data: bytes data
        '''
        if self.is_alive():
            for client in client_socket:
                client.sendall(data)


if __name__ == '__main__':
    ser = tcp_server(20000)
    ser.start()
    print("listening")
    time.sleep(10)
    print("sending")
    ser.send_data("test sending".encode('utf-8'))
    time.sleep(5)
    print("shuting")
    ser.shutdown()

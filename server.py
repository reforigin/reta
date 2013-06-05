#!/usr/bin/python
#coding=utf-8

import tornado.web
import tornado.ioloop

class Handlers(tornado.web.RequestHandler):
    def Error(self, message=''):
        if message:
            self.write(message)
        else:
            self.write('Something went wrong -_-')

class IndexHandler(Handlers):
    def get(self):
        self.Error()
        #self.write("Hey. Hello, reta :)")

class Server(object):
    def Init(self):
        self.application = tornado.web.Application([
            ('/', IndexHandler),
        ])

    def Listen(self, port):
        self.application.listen(int(port))
        tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    server = Server()
    server.Init()
    server.Listen(80)


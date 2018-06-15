#!bin/python
import time
import cherrypy
import os

class Root(object):
    """ root of web application """
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, delay=60):
        """ base API - Delay """
        t = time.time()
        time.sleep(float(delay))
        response = { "start_time": t, "delay":delay }
        return response 

if __name__ == '__main__':
    _port = int(os.getenv('PORT', 8080))
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': _port,})
    cherrypy.quickstart(Root(), '/',)

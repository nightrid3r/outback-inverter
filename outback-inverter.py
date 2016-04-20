#!/usr/bin/python
""" Node Server for Polyglot 
      by Einstein.42(James Milne)
      milne.james@gmail.com"""

from polyglot.nodeserver_api import SimpleNodeServer, PolyglotConnector
from inverter_types import ModbusController

VERSION = "0.1.1"


class OutbackNodeServer(SimpleNodeServer):
    controller = []
    mbnodes = []

    def setup(self):
        manifest = self.config.get('manifest',{})
        self.controller = OutbackController(self,'obcontroller','Outback Controller', True, manifest)
        self.poly.logger.info("FROM Poly ISYVER: " + self.poly.isyver)
        self.controller._discover()
        self.update_config()
        
    def poll(self):
        pass

    def long_poll(self):
        pass
        
def main():
    # Setup connection, node server, and nodes
    poly = PolyglotConnector()
    # Override shortpoll and longpoll timers to 5/30, once per second is excessive in this nodeserver 
    nserver = OutbackNodeServer(poly, 5, 30)
    poly.connect()
    poly.wait_for_config()
    poly.logger.info("Modbus Interface version " + VERSION + " created. Initiating setup.")
    nserver.setup()
    poly.logger.info("Setup completed. Running Server.")
    nserver.run()
    
if __name__ == "__main__":
    main()
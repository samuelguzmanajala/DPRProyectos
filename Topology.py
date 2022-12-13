from mininet.topo import Topo
import sys

class Topology:
    def __init__(self, *args, **params):
        print('hola')
        super().__init__(*args, **params)
        
        Topo.__init__( self )
    
        
        fo = sys.argv[1]
        Ts = self.addSwitch('Ts', dpid = '0000000100002022')

        if fo<1 or fo >255:
            print('rango incorrecto, debe estar entre 1 y 255')
        else:
            for i in range(1, fo+1):
                switches = self.addSwitch('s' + str(i))
                self.addLink(switches, Ts, 1, i)

                for j in range(1, fo+1):
                    hosts = self.addHost('h_s'+ str(i) + 'n' + str(j), ip = '10.0.' + str(i)+ '.' + str(j) + '/16')
                    self.addLink(hosts, switches, 1, j+1)
topos = {'topology': (lambda:Topology())}

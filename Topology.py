from mininet.topo import Topo
import sys
class Topology( Topo ):
    def __init__(self):
        Topo.__init__( self )
        fo = input('cuantos switchs?')
        if fo<1 or fo >255: #Lanzamos una excepcion si el valor fo es incorrecto
            raise AttributeError
        print("se crearan", fo, "switches y", fo*fo, "hosts")
        parentSwitch = self.addSwitch('Ts', dpid = '0000000000002022')
        for i in range(1, fo+1):
            switches = self.addSwitch('s' + str(i))
            self.addLink(switches, parentSwitch, 1, i)
            for j in range(1, fo+1):
                hosts = self.addHost('host_'+ str(i) + '_' + str(j), ip = '10.0.' + str(i)+ '.' + str(j) + '/16')
                self.addLink(hosts, switches, 1, j+1)
topos = {'topology': (lambda:Topology())}

from mininet.topo import Topo
from mininet.node import OVSSwitch


class Lab1Topo(Topo):
    def __init__(self, n=4):
        Topo.__init__(self)
        switches = []
        hosts = []
        for i in range(n):
            # Añadir switch con capacidad de STP
            swx = self.addSwitch(f"s{i+1}", cls=OVSSwitch, stp=1,
                                 failMode="standalone")
            # Añadir host y su enlace al switch
            hx = self.addHost(f"h{i+1}")
            self.addLink(swx, hx)
            # Añadir enlaces con los demás switches
            for sw in switches:
                self.addLink(swx, sw)
            switches.append(swx)
            hosts.append(hx)


topos = {
    "lab1": Lab1Topo,
}

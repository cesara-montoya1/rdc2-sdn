# Parte de este código es tomada del curso de SDN realizado por el profesor
# Nick Feamster

from pox.core import core
import pox.openflow.discovery
import pox.openflow.spanning_tree
import pox.openflow.libopenflow_01 as of
from pox.lib.addresses import EthAddr
from pox.lib.util import dpidToStr
import os
import csv


# Adicione las clases y métodos que considere
def read_firewall_policies(file_path):
    try:
        with open(file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = []
            for row in reader:
                data.append((EthAddr(row.get("mac_0")),
                             EthAddr(row.get("mac_1"))))
            return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []


log = core.getLogger()

# Cree variables globales acá
POLICIES_FILE = f"{os.environ['HOME']}/pox/pox/misc/firewall-policies.csv"
FIREWALL_POLICIES = read_firewall_policies(POLICIES_FILE)


class Firewall:
    def __init__(self):
        core.openflow.addListeners(self)
        log.debug("Inicializando el firewall...")

    # Evento de switch conectándose al controlador
    def _handle_ConnectionUp(self, event):
        dpid = event.dpid
        log.debug(f"Instalando el firewall en {dpidToStr(dpid)}")

        for dl_src, dl_dst in FIREWALL_POLICIES:
            # Crear mensaje OpenFlow para modificar la tabla de flujos
            msg = of.ofp_flow_mod()
            # Crear regla, como no tiene acción por defecto descarta
            msg.match = of.ofp_match(dl_src=dl_src, dl_dst=dl_dst)
            # Enviar mensaje OpenFlow hacia el switch
            event.connection.send(msg)

        log.debug(f"Reglas instaladas en {dpidToStr(dpid)}")


def launch():
    pox.openflow.discovery.launch()
    pox.openflow.spanning_tree.launch()
    core.registerNew(Firewall)

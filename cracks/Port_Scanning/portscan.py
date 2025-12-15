from ..base import Crack
from scapy.all import sniff, TCP, UDP

class PortScanCrack(Crack):
  store = {}

  def defend(self, defendip):
    self.store = {}
    packets = sniff(count=2000)

    for packet in packets:
        src_ip = packet[defendip].src

        isTCP = packet.haslayer(TCP)
        isUDP = packet.haslayer(UDP)

        if (not (isTCP and isUDP)):
          continue
        
        port = packet[TCP].dport if isTCP else packet[UDP].dport
        
        if not self.store[src_ip]:
          self.store[src_ip] = {}
        else:
          self.store[src_ip][port] = True
    
    return sorted([k for k,v in self.store.items() if len(v) >= 2000])
    
from collections import defaultdict
from time import time
from scapy.layers.inet import IP, TCP
from cracks.base import Crack

class PortScanCrack(Crack):
    WINDOW = 10
    PORT_THRESHOLD = 20

    def __init__(self):
        super().__init__("Port Scan")
        self.history = defaultdict(list)

    def on_packet(self, pkt, context):
        if not (pkt.haslayer(IP) and pkt.haslayer(TCP)):
            return []

        src = pkt[IP].src
        dport = pkt[TCP].dport
        now = time()

        self.history[src].append((now, dport))
        self.history[src] = [
            (t, p) for t, p in self.history[src]
            if now - t <= self.WINDOW
        ]

        ports = {p for _, p in self.history[src]}

        if len(ports) >= self.PORT_THRESHOLD:
            scanned_ports = sorted(ports)
            self.history[src] = []

            return [(
                "Port Scan",
                src,
                f"Scanned ports: {scanned_ports}"
            )]

        return []

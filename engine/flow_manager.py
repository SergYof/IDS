# engine/flow_manager.py
from time import time
from scapy.layers.inet import IP, TCP, UDP
from engine.flow import Flow
from scapy.layers.inet6 import IPv6

FLOW_TIMEOUT = 60  # seconds


class FlowManager:
    def __init__(self):
        self.flows = {}



    def flow_key(self, pkt):
        # IPv4 TCP
        if pkt.haslayer(IP) and pkt.haslayer(TCP):
            return (
                pkt[IP].src,
                pkt[TCP].sport,
                pkt[IP].dst,
                pkt[TCP].dport,
                "TCP"
            )

        # IPv4 UDP
        if pkt.haslayer(IP) and pkt.haslayer(UDP):
            return (
                pkt[IP].src,
                pkt[UDP].sport,
                pkt[IP].dst,
                pkt[UDP].dport,
                "UDP"
            )

        # IPv6 TCP (optional but recommended)
        if pkt.haslayer(IPv6) and pkt.haslayer(TCP):
            return (
                pkt[IPv6].src,
                pkt[TCP].sport,
                pkt[IPv6].dst,
                pkt[TCP].dport,
                "TCP6"
            )

        return None

    def get_flow(self, pkt):
        key = self.flow_key(pkt)
        if not key:
            return None

        flow = self.flows.get(key)
        if not flow:
            flow = Flow(key)
            self.flows[key] = flow

        flow.touch()
        return flow

    def expire_flows(self):
        now = time()
        expired = [
            k for k, f in self.flows.items()
            if now - f.last_seen > FLOW_TIMEOUT
        ]

        for k in expired:
            del self.flows[k]

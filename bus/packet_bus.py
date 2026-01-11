# bus/packet_bus.py
from collections import deque

class PacketBus:
    def __init__(self):
        self.queue = deque()

    def publish(self, pkt, suspicious=False):
        self.queue.append((pkt, suspicious))

    def get_all(self):
        items = list(self.queue)
        self.queue.clear()
        return items

PACKET_BUS = PacketBus()
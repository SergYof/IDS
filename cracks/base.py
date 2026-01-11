# cracks/base.py
class Crack:
    def __init__(self, name):
        print(f"[!] {name.upper()} STARTED")
        self.name = name

    def on_packet(self, pkt, flow):
        return []

    def on_flow(self, flow):
        return []

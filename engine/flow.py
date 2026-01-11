# engine/flow.py
from time import time

class Flow:
    def __init__(self, key):
        self.key = key
        self.created = time()
        self.last_seen = time()

        # best-effort stream buffer (TCP)
        self.buffer = b""

        # arbitrary per-flow state
        self.meta = {}

    def touch(self):
        self.last_seen = time()

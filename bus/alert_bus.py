# bus/alert_bus.py
from collections import deque

class AlertBus:
    def __init__(self):
        self.queue = deque()

    def publish(self, alert):
        self.queue.append(alert)

    def get_all(self):
        alerts = list(self.queue)
        self.queue.clear()
        return alerts

ALERT_BUS = AlertBus()
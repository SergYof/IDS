from manager import Manager
from cracks.portscan import PortScanCrack
from cracks.arpspoof import ARPSpoofCrack
from cracks.dnsspoof import DNSSpoofCrack
from gui import start_gui
from threading import Thread


IFACE = "\\Device\\NPF_{F1E0C994-3AF0-4DDB-A078-DD369AC3F0E4}"

def main():
    cracks = [
        PortScanCrack(),
        ARPSpoofCrack(),
        DNSSpoofCrack()
    ]

    gui_thread = Thread(target=start_gui, daemon=True)
    gui_thread.start()

    Manager(cracks).start(IFACE)

if __name__ == "__main__":
    main()

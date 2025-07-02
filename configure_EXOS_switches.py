from netmiko import ConnectHandler
from datetime import datetime
from all_devices import extreme_exos_SW1, extreme_exos_SW2, extreme_exos_SW3, extreme_exos_IGW
import os

class EXOSDeviceManager:
    def __init__(self, device_dict):
        self.device = device_dict
        self.connection = None
        self.name = None

    def connect(self):
        self.connection = ConnectHandler(**self.device)
        self.name = self.connection.find_prompt()[2:5]

    def configure_bgp(self):
        config_file = f'./Configurations/iBGP_{self.name}.txt'
        print(f"Configuring BGP for {self.name}")
        self._send_config(config_file)

    def configure_loopback(self):
        config_file = f'./Configurations/Loopback_{self.name}.txt'
        print(f"Configuring Loopback for {self.name}")
        self._send_config(config_file)

    def _send_config(self, config_file):
        try:
            if os.path.exists(config_file):
                self.connection.send_config_from_file(config_file=config_file)
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(f"Error: Config file {config_file} not found.")

def main():
    starttime = datetime.now()
    devices = [extreme_exos_SW1, extreme_exos_SW2, extreme_exos_SW3, extreme_exos_IGW]

    for device in devices:
        manager = EXOSDeviceManager(device)
        manager.connect()
        manager.configure_bgp()
        manager.configure_loopback()

    print(f"Time Elapsed = {datetime.now() - starttime}")

if __name__ == "__main__":
    main()

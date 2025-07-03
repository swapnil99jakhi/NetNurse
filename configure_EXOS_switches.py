from netmiko import ConnectHandler
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from device_configs import device_configs
from all_devices import extreme_exos_SW1, extreme_exos_SW2, extreme_exos_SW3, extreme_exos_IGW

class EXOSDeviceManager:
    def __init__(self, device_dict, template_data):
        self.device = device_dict
        self.template_data = template_data
        self.connection = None
        self.name = None
        self.env = Environment(loader=FileSystemLoader('./Config_templates'))

    def connect(self):
        self.connection = ConnectHandler(**self.device)
        self.name = self.connection.find_prompt()[2:5]

    def configure_bgp(self):
        print(f"Configuring BGP for {self.name}")
        self._render_and_send('BGP_template.j2')

    def configure_loopback(self):
        print(f"Configuring Loopback for {self.name}")
        self._render_and_send('Loopback_template.j2')

    def _render_and_send(self, template_name):
        try:
            template = self.env.get_template(template_name)
            config = template.render(self.template_data)
            commands = config.strip().splitlines()
            self.connection.send_config_set(commands)
        except Exception as e:
            print(f"Error rendering or sending config: {e}")

def main():
    starttime = datetime.now()
    devices = {
        'SW1': extreme_exos_SW1,
        'SW2': extreme_exos_SW2,
        'SW3': extreme_exos_SW3,
        'IGW': extreme_exos_IGW
    }

    for name, device in devices.items():
        if name in device_configs:
            manager = EXOSDeviceManager(device, device_configs[name])
            manager.connect()
            manager.configure_bgp()
            manager.configure_loopback()
        else:
            print(f"No config found for {name}")

    print(f"Time Elapsed = {datetime.now() - starttime}")

if __name__ == "__main__":
    main()

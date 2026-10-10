from pypresence import Presence
from time import sleep
from utils import (
    get_system_stats , 
    get_distro , 
    get_os_name,
    get_info ,
)

class DiscordRPC:
    
    def __init__(self):
        self.client_id = "1318260477817786511" 
        self.rpc = Presence(self.client_id)
    
    def connect(self):
        try:
            self.rpc.connect()
            print("✅ Connected to Discord RPC!")
        except Exception as e:
            print(f"❌ Error connecting to Discord RPC: {e}")

    def update_presence(self):
        os_name = get_os_name()
        battery_percent, cpu_usage, memory_usage, uptime_str , power_plugged= get_system_stats()
        distro = get_distro()
        window = get_info("activewindow")
        try:
            self.rpc.update(
                    state=f"</> OS: {os_name} | 💻 CPU: {cpu_usage}{" | 🐧 Distro: {}".format(distro) if distro else ""}",
                details=f"⚡ Battery: {battery_percent}\n | 🖥 Memory: {memory_usage} | 👾 App: {str(window.get("class")).capitalize()}",
                large_image="arch",
                large_text=f"Uptime : {uptime_str} | Charging : {"Off" if power_plugged == False else "On"}",
                small_image="neovim",
                small_text="Neovim",
                
            )
            print("✅ Presence updated!")
        except Exception as e:
            print(f"❌ Error updating presence: {e}")

if __name__ == "__main__":
    presence = DiscordRPC()
    presence.connect()

    while True:
        presence.update_presence()
        sleep(10) 

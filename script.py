###--- IMPORTS ---###
import subprocess


###--- FUNCTIONS ---###
def disable_wifi_service():
    subprocess.run(
        ["sudo", "networksetup", "-setnetworkserviceenabled", "Wi-Fi", "off"])


def enable_wifi_service():
    subprocess.run(
        ["sudo", "networksetup", "-setnetworkserviceenabled", "Wi-Fi", "on"])


###--- DRIVER CODE ---###
if __name__ == "__main__":
    disable_wifi_service()
    # enable_wifi_service()

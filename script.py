###--- IMPORTS ---###
import subprocess


###--- FUNCTIONS ---###
def disable_wifi_service():
    subprocess.run(
        ["sudo", "networksetup", "-setnetworkserviceenabled", "Wi-Fi", "off"])


def enable_wifi_service():
    subprocess.run(
        ["sudo", "networksetup", "-setnetworkserviceenabled", "Wi-Fi", "on"])


def turn_airplane_mode_off():
    '''
     AirPort (Wi-Fi) off 
    '''
    subprocess.run(
        ["sudo", "networksetup", "-setairportpower", "airport", "off"])


def turn_airplane_mode_on():
    '''
     AirPort (Wi-Fi) on
    '''
    subprocess.run(
        ["sudo", "networksetup", "-setairportpower", "airport", "on"])


def disable_wifi_and_ethernet():
    subprocess.run(["sudo", "networksetup", "-setv6off", "Wi-Fi"])


def enable_wifi_and_ethernet():
    subprocess.run(["sudo", "networksetup", "-setv6automatic", "Wi-Fi"])


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # disable_wifi_service()
    # enable_wifi_service()
    # turn_airplane_mode_off()
    # turn_airplane_mode_on()
    # disable_wifi_and_ethernet()
    enable_wifi_and_ethernet()

import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "---interface", dest="interfacePars", help="Interface 2 change mac address" )

newmac=input("New MAC: --> ")
interface=input("Interface: --> ")


print("[+] Changing MAC address for " + interface + " to" + newmac)
print("-> shooting down " + interface)
subprocess.call("sudo ifconfig " + interface + " down", shell=True)
print("-> changing mac to " + newmac)
subprocess.call("sudo ifconfig " + interface + " hw ether " + newmac, shell=True)
print("-> powering up " + interface)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)
print("result: ")
subprocess.call("sudo ifconfig " + interface, shell=True)
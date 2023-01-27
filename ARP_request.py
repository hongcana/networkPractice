# # for Windows and Linux:
# import os

# def send_arp_request():
#     os.system("arp -a")

# send_arp_request()


# for MacOS:
import subprocess

def send_arp_request():
    output = subprocess.run(["arp", "-a"], capture_output=True, text=True)
    print(output.stdout)

send_arp_request()
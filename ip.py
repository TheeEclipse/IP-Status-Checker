import requests
from termcolor import colored
import time

# Print the ASCII art to the console
# Print the ASCII art to the console
ascii_banner = r"""
._____________  _________ .__                   __    
|   \______   \ \_   ___ \|  |__   ____   ____ |  | __
|   ||     ___/ /    \  \/|  |  \_/ __ \_/ ___\|  |/ /
|   ||    |     \     \___|   Y  \  ___/\  \___|    < 
|___||____|      \______  /___|  /\___  >\___  >__|_ \
                        \/     \/     \/     \/     \/ 1.1.0"""
print(colored(ascii_banner.strip(), "cyan"))
print(colored("Author: Thee_Eclipse\n", "yellow"))
print(colored("https://twitter.com/Thee_Eclipse\n", "yellow"))
print(colored("Usage Guide", "green"))
print(colored("Enter starting IP e.g: 21.90.220.0 and ending IP e.g: 21.90.220.255 or within the ASN IP ranges.", "yellow"))
print(colored("More details on ASN and IP ranges: https://ipinfo.io/", "blue"))
print("-----------------------------------------------------")
print("\n")

# Prompt the user to enter the range of IP addresses to scan
start_ip = input(colored("Enter the starting IP address: ", "magenta"))
end_ip = input(colored("Enter the ending IP address: ", "magenta"))

for i in range(int(start_ip.split(".")[3]), int(end_ip.split(".")[3])+1):
    ip_address = ".".join(start_ip.split(".")[:3]) + "." + str(i)
    url = "http://" + ip_address

    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Print the IP address in orange if status code is 200
            print(colored(ip_address, "yellow"), "is up and running with status code 200 OK")
        else:
            print(ip_address, "is down")
    except:
        pass

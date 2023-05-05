# IP-Status-Checker
This is a simple IP status checker tool that allows you to check the status of an IP range or ASN. The tool can be used to quickly identify any unreachable or unresponsive IP addresses within a range.
# Features
* Check the status of an IP range or ASN
* Quickly identify unreachable or unresponsive IP addresses
* Easy-to-use command line interface
* Can work with other tools to fetch and scan IP status codes
# Getting Started
  # Prerequisites
* Python 3.x
* requests module (can be installed using ```pip install requests```)
# Installation
* Clone the repository: ```git clone https://github.com/TheeEclipse/IP-Status-Checker```
* Navigate to the project directory: ```cd IP-Status-Checker```
>>Or just get the python file: and run it
# Usage
* Open a command prompt or terminal window and navigate to the project directory.
* Run the tool using the following command:
```python3 ip.py```

You will be prompted to enter:

```Enter the starting IP address:``` eg:  1.90.246.0

```Enter the ending IP address:``` eg: 1.90.246.25
# Dont know a target or  ASN IP range?
Use: https://ipinfo.io/
# Output
The tool will output the following information for each IP address:

* IP address
* Status (reachable or unreachable)

Here all unreachable IP's are listed as ```{ip} is down``` and you can edit that to meet your needs

All reachable IP's are listes as: ```{IP} is up and running with status code 200 OK```
# Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request.

# Hint
Manual testing is always recommended for all tools!!


# findit---Network-Scanner-and-Port-Closer
The findit tool will scan the specified network for open ports and close any that it finds.

# Introduction
findit is a network scanner tool designed to detect open ports on a specified network and close them. This tool is divided into two parts: a Python script for scanning `scanner.py` and another for closing the detected open ports `closer.py`. The tool is designed to be used on Kali Linux.

## Features
- Scan a target IP address for open ports within a specified range.
- Generate a report of open ports.
- Close the detected open ports using iptables.

# Requirements
- Python 3.x
- Kali Linux or any other Linux distribution with iptables installed.
- Elevated privileges `sudo` to modify firewall settings.

# Installation
1. Clone the repository (or download the scripts):
   ```
   git clone https://github.com/muhammad1596/findit.git
)
   ```
   ```
   cd findit
   ```
2. Ensure the scripts are executable:
   ```
   chmod +x findit.sh
   ```

# Usage

1. Run the Tool:
  Execute the bash script to run the scanner and closer scripts sequentially:
  ```
  sudo ./findit.sh
  ```

2. Follow the Prompts:
  - Enter the target IP address.
  - Specify the start and end ports for the scan.

3. Output:
  - The scanner will display and save the open ports in `open_ports.txt`.
  - The closer script will read from `open_ports.txt` and close the detected open ports.

## Notes
  - Ensure you run the findit.sh script with sudo to allow the closing of ports.
  - The tool modifies iptables rules, so make sure to review the changes to avoid blocking necessary traffic.

import os

# Function to close a given port using iptables
def close_port(port):
    os.system(f"sudo iptables -A INPUT -p tcp --dport {port} -j DROP")
    os.system(f"sudo iptables -A OUTPUT -p tcp --sport {port} -j DROP")
    print(f"Port {port} closed.")

if __name__ == "__main__":
    try:
        with open("open_ports.txt", "r") as file:
            open_ports = [int(line.strip()) for line in file]
        
        if open_ports:
            print("Closing open ports...")
            for port in open_ports:
                close_port(port)
            print("All open ports closed.")
        else:
            print("No open ports to close.")
    except FileNotFoundError:
        print("open_ports.txt not found. Please run the scanner first.")

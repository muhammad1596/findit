import socket
from datetime import datetime

# Function to scan ports on a given host
def scan_ports(host, start_port, end_port):
    open_ports = []
    print(f"Starting scan on host: {host}")
    
    # Scan each port in the specified range
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    start_time = datetime.now()
    open_ports = scan_ports(target, start_port, end_port)
    end_time = datetime.now()
    
    total_time = end_time - start_time
    print(f"Scanning completed in: {total_time}")
    
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
        
        with open("open_ports.txt", "w") as file:
            for port in open_ports:
                file.write(f"{port}\n")
    else:
        print("No open ports found")

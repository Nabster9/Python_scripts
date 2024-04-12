import socket
import subprocess
import sys
from datetime import datetime
import argparse

def scan(ip):
    remoteServerIP = socket.gethostbyname(ip)
    # Print banner
    print("_" * 60)
    print("Please wait scanning", remoteServerIP)
    print("_" * 60)

    # Check the date and time when the scan started
    start_time = datetime.now()

    # Using the range function specify ports.
    # Also, we will do error handling
    try:
        for port in range(1, 65536):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:    
        print("Hostname could not be resolved")
        sys.exit()

    except socket.error:
        print("Could not connect to the server")
        sys.exit()

    # Check time again
    end_time = datetime.now()

    # Calculate the difference time
    print('Scan Completed in : ', end_time - start_time)

def main():
    parser = argparse.ArgumentParser(description='Port scan')
    parser.add_argument('ip', metavar='ip', type=str, help='IP Address')
    args = parser.parse_args()
    remoteServerIP = args.ip
    
    # Clear the screen
    subprocess.call('clear', shell=True)

    scan(remoteServerIP)

if __name__ == "__main__":
    main()

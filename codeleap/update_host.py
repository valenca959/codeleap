import os
import sys

def modify_hosts(domain, ip):
    """Modify the /etc/hosts file on Linux/macOS systems."""
    hosts_path = "/etc/hosts"
    entry = f"{ip} {domain}\n"

    try:
        if os.geteuid() != 0:
            print("This script needs to be run as root.")
            sys.exit(1)

        with open(hosts_path, "r") as hosts_file:
            lines = hosts_file.readlines()

        for line in lines:
            if domain in line:
                print(f"The domain {domain} is already configured in /etc/hosts.")
                return

        with open(hosts_path, "a") as hosts_file:
            hosts_file.write(entry)

        print(f"The domain {domain} has been added to the /etc/hosts file with IP {ip}.")

    except Exception as e:
        print(f"Error modifying the /etc/hosts file: {e}")

def modify_hosts_windows(domain, ip):
    """Modify the hosts file on Windows systems."""
    hosts_path = r"C:\\Windows\\System32\\drivers\\etc\\hosts"
    entry = f"{ip} {domain}\n"

    try:
        if not os.access(hosts_path, os.W_OK):
            print("This script needs to be run as administrator.")
            return

        with open(hosts_path, "r") as hosts_file:
            lines = hosts_file.readlines()

        for line in lines:
            if domain in line:
                print(f"The domain {domain} is already configured in the hosts file.")
                return

        with open(hosts_path, "a") as hosts_file:
            hosts_file.write(entry)

        print(f"The domain {domain} has been added to the hosts file with IP {ip}.")

    except Exception as e:
        print(f"Error modifying the hosts file: {e}")

if __name__ == "__main__":
    domain = "dev.codeleap.co.uk"
    ip = "127.0.0.1"

    if os.name == "nt":
        modify_hosts_windows(domain, ip)
    else:
        modify_hosts(domain, ip)

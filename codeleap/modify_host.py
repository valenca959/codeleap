import os
import sys

def modify_hosts(domain, ip):
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
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
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


def remove_hosts_entry(domain, ip):
    hosts_path = "/etc/hosts"
    entry = f"{ip} {domain}\n"

    try:
        if os.geteuid() != 0:
            print("This script needs to be run as root.")
            sys.exit(1)

        with open(hosts_path, "r") as hosts_file:
            lines = hosts_file.readlines()

        with open(hosts_path, "w") as hosts_file:
            for line in lines:
                if line != entry:
                    hosts_file.write(line)

        print(f"The entry for domain {domain} has been removed from the /etc/hosts file.")

    except Exception as e:
        print(f"Error modifying the /etc/hosts file: {e}")


def remove_hosts_entry_windows(domain, ip):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    entry = f"{ip} {domain}\n"

    try:
        if not os.access(hosts_path, os.W_OK):
            print("This script needs to be run as administrator.")
            return

        with open(hosts_path, "r") as hosts_file:
            lines = hosts_file.readlines()

        with open(hosts_path, "w") as hosts_file:
            for line in lines:
                if line != entry:
                    hosts_file.write(line)

        print(f"The entry for domain {domain} has been removed from the hosts file.")

    except Exception as e:
        print(f"Error modifying the hosts file: {e}")


if __name__ == "__main__":
    domain = "dev.codeleap.co.uk"
    ip = "127.0.0.1"

    if sys.platform != "win32":
        action = input("Choose action (add/remove): ").strip().lower()
        if action == "add":
            modify_hosts(domain, ip)
        elif action == "remove":
            remove_hosts_entry(domain, ip)
        else:
            print("Invalid action. Choose 'add' or 'remove'.")
    else:
        action = input("Choose action (add/remove): ").strip().lower()
        if action == "add":
            modify_hosts_windows(domain, ip)
        elif action == "remove":
            remove_hosts_entry_windows(domain, ip)
        else:
            print("Invalid action. Choose 'add' or 'remove'.")
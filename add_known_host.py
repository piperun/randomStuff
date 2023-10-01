import paramiko
import argparse
import socket
import os
from pathlib import Path


class Known_hosts():
    def __init__(self, ip_adress, port, userauth):
        self.ip_adress = ip_adress
        self.port = port
        self.userauth = userauth
        self.hostkey = self.get_remotehostkey()
        self.ssh = paramiko.SSHClient()
        self.host_file = self.get_known_hosts()

    def ssh_connect(self):
        self.ssh.get_host_keys().add(self.ip_adress, "ssh-rsa", self.hostkey)
        self.ssh.connect(self.ip_adress, port=self.port,
                         username=self.userauth["username"], password=self.userauth["password"], pkey=self.userauth["privkey"])
           
    def create_known_hosts(self):
        if not Path(self.host_file).is_file():
            Path(self.host_file).mkdir(parents=True ,exist_ok=True)
    

    def get_remotehostkey(self):
        sock = socket.socket()
        sock.connect((self.ip_adress, self.port))
        transport = paramiko.transport.Transport(sock)
        transport.start_client()
        k = transport.get_remote_server_key()
        return k

    def get_known_hosts(self) -> str:
        home = str(Path.home())
        cwd = os.path.dirname(__file__)
        known_hosts_locations = {
            "user":str(Path(home + "/.ssh/known_hosts")),
            "default":str(Path(cwd + "/known_hosts"))
        }
        known_hosts = known_hosts_locations["user"] if Path(home + "/.ssh/known_hosts").is_file() else known_hosts_locations["default"]

        return known_hosts

    def save_hostskey(self):
        self.ssh_connect()
        self.ssh.load_host_keys(self.host_file)
        self.ssh.save_host_keys(self.host_file)

def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [add] [IP]...",
        description="Adds hosts key to known_hosts.",
    )
    parser.add_argument("add", nargs=2)

    return parser

def main():
    #parser = init_parser()
    #args = parser.parse_args()
    userauth = {
        "username":"flynn",
        "password":"operetek",
        "privkey":None
    }
    known_hosts = Known_hosts("192.168.1.240", 22, userauth)
    known_hosts.save_hostskey()


if __name__ == "__main__":
    main()    
    

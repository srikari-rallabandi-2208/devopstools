import paramiko
import threading
# Define the SSH server class
class SSHServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        # Add your authentication logic here
        if username == "myuser" and password == "mypassword":
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_exec_request(self, channel, command):
        # Add your command execution logic here
        # For example, you can execute the command using `subprocess` module
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            channel.send(output)
            channel.send_exit_status(0)
        except subprocess.CalledProcessError as e:
            channel.send(e.output)
            channel.send_exit_status(e.returncode)

    def get_allowed_auths(self, username):
        return "password"

# Start the SSH server
def start_ssh_server():
    passphrase = "mypassword"  # Set your passphrase here
    host_key = paramiko.RSAKey(filename='./keys/host_rsa.key', password=passphrase)

    server = SSHServer()

    # Create an SSH transport
    transport = paramiko.Transport(('0.0.0.0', 22))
    transport.add_server_key(host_key)
    transport.set_subsystem_handler("sftp", paramiko.SFTPServer, SFTPServer)

    # Start the SSH server
    transport.start_server(server=server)

    # Accept connections
    while True:
        channel = transport.accept(20)
        if channel is None:
            continue
        server.event.wait(10)
        if not server.event.is_set():
            channel.close()
            continue
        server.event.clear()
        server.check_channel_request(channel)
        server.event.set()

# Main entry point
if __name__ == "__main__":
    start_ssh_server()

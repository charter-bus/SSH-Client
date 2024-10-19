import paramiko
# ssh_command will form a connection to an SSH server and relay standard output & error feedback to our console
# The paramiko module supports key authentication, as well as username/password authentication.
# Key authentication is preferred for security reasons.

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    default_host = '0.0.0.0'
    default_port = 2222
    default_username= 'root'
    default_password = 'password'

    import getpass
    # Prompt the user for the username, password, host, and port for the target machine.
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter server IP: ') or default_host
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)


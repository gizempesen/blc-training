import subprocess

def ip():
    global ip
    ip = open("/root/kubespray-2.17.1/ip.txt", "r", encoding="utf-8")
    IPS = ip.read()
    print(IPS)
    #subprocess.run(["declare -a IPS=(" + IPS + ")" ])

ip()

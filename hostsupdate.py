import os
from shutil import copyfile

if(not os.path.exists("/etc/hosts.bak")):
    copyfile("/etc/hosts", "/etc/hosts.bak")

t = os.popen("cat /etc/hosts.bak", 'r', 2)
oldhosts = "## WARNING ##\n" + \
    "# YOU ARE USING GITHUBHOSTS AUTO UPDATER, IF YOU WANT TO CHANGE THIS FILE, PLEASE GO TO \"/etc/hosts.bak\"\n\n" + t.read()

t = os.popen(
    "curl https://cdn.jsdelivr.net/gh/521xueweihan/GitHub520@main/hosts", 'r', 2)
newhosts = oldhosts+t.read()

with open("/etc/hosts", 'w') as f:
    f.write(newhosts)

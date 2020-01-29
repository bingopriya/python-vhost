from jinja2 import Environment, FileSystemLoader
import os
import subprocess
import sys

def check_username ( name ):
    '''
    If user exists it will return true
    '''
    
    readpasswd=open("/etc/passwd","r")
    for i in readpasswd:
        user=i.split(":")[0]
        if(user ==  name):
            return True
    return False


Username = raw_input("Enter your username :")
if check_username(Username)==True:
    print("Username already exists")
    sys.exit()
else:
    print("Username available")
Website_Name = raw_input("Enter your Website name :")
Website_Location =raw_input("Enter your Website locaton :")
doc ="/var/www/html/"+Username
subprocess.call(["useradd","-d",doc,Username])
#subprocess.call(["mkdir",doc])
subprocess.call(["chown","{}:{}".format(Username,Username),doc])
subprocess.call(["cp","-r","{}".format(Website_Location),doc])
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('test.com.conf')

filename = "/etc/httpd/sites-available/{}.conf".format(Website_Name)
with open(filename, 'w') as fh:
    fh.write(template.render(
        Website_Name = Website_Name,
        doc = doc,
        
    ))
enable ="/etc/httpd/sites-enabled/{}.conf".format(Website_Name)
subprocess.call(["ln","-s",filename,enable])
subprocess.call(["chown", "-R","apache:apache","/var/www/html"])
subprocess.call(["systemctl","restart","httpd"])
import subprocess
Username = input("Enter your username :")
Website_Name = input("Enter your Website name :")
Website_Location =input("Enter your Website Location :")
subprocess.run(["useradd",Username])

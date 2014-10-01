'wgTerm'

import os

class AppInfo():
    version = "1.0.0.0"

class Configuration():

    init_onstartup = False
    update_using_git = False
    wget_no_cert = False

app = AppInfo()

config = Configuration()

def init():

    print("wgTerm v" + app.version + "\n\n")
    term()

def term():

    term_input = input("$>")
    if term_input == "": term()
    elif term_input == "exit": exit()
    elif term_input == "st -about": About()
    elif term_input == "st -update": Updates()
    else:
        os.system("wget " + term_input)
        term()

def About():

    print("wgTerm v" + app.version + "\n")
    print("This software is Free Software.\n")
    print("License: https://gnu.org/licenses/gpl.txt")
    print("Project site: https://deavmi.github.io/wgTerm")
    print("Source code: https://github.com/deavmi/wgTerm\n")
    term()

def Updates():

    print("wgTerm v" + app.version + "\n")
    if config.update_using_git == True:
        print("Getting updates...")
        print("Fetching files... [0%]")
        os.system("git clone https://github.com/deavmi/wgTerm.git")
        print("Fetching files... [100%]")
        print("Update completed!")
    else:
        if config.wget_no_cert == True: flag = " --no-check-certificate"
         else: flag = ""
        print("Getting updates...")
        print("Fetching file [1 of 4]")
        os.system("wget https://raw.githubusercontent.com/deavmi/wgTerm/master/term.py" + flag)
        print("Fetching file [2 of 4]")
        os.system("wget https://raw.githubusercontent.com/deavmi/wgTerm/master/LICENSE" + flag)
        print("Fetching file [3 of 4]")
        os.system("wget https://raw.githubusercontent.com/deavmi/wgTerm/master/CREDITS.md" + flag)
        print("Fetching file [4 of 4]")
        os.system("wget https://raw.githubusercontent.com/deavmi/wgTerm/master/README.md" + flag)
        print("Update completed!")
    term()

def read_config():

    if config.init_onstartup == True: init()
    else: term()

'Reads the configuration'
read_config()
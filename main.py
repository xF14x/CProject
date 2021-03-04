# programming by suliman almohawis \ twitter : F14Commander Inatagram : f14.commander

# =-=-=-=-=-=-=-=-= import the liberes

from os import system, chdir
from sys import argv

# =-=-=-=-=-=-=-=-=

Pythonlocaton_txt = open('Data/PythonLocaton.txt')
PythonFileLocaton = Pythonlocaton_txt.read()

JavaFilelocaton_txt = open('Data/JavaLocaton.txt')
JavaFilelcaton = JavaFilelocaton_txt.read()

ShellFilelocaton_txt = open('Data/ShellLocaton.txt')
ShellFileLocaton = ShellFilelocaton_txt.read()

CFileLocaton_txt = open('Data/C-Locaton.txt')
CFileLocaton = CFileLocaton_txt.read()

# =-=-=-=-=-=-=-=

if argv[1] == "help":
    print(f''' 
Java & C & Shell & Python
''')
    exit()
else: pass

def MakeTheaProject(lang, ProjectName):
    if lang == "python" and ProjectName == str:

        print("Creating the project...")
        system(f'mkdir {PythonFileLocaton}{ProjectName} && git init {PythonFileLocaton}{ProjectName}')
        print("")
        print(f'Project Locaton is {PythonFileLocaton}{ProjectName}')
    elif lang == "java" and ProjectName == str:

        print("Creating the project...")
        system(f'mkdir {PythonFileLocaton}{ProjectName} && git init {PythonFileLocaton}{ProjectName}')
        print("")
        print(f'Project Locaton is {PythonFileLocaton}{ProjectName}')
    elif lang == "shell" and ProjectName == str:

        print("Creating the project...")
        system(f'mkdir {PythonFileLocaton}{ProjectName} && git init {PythonFileLocaton}{ProjectName}')
        print("")
        print(f'Project Locaton is {PythonFileLocaton}{ProjectName}')
    elif lang == "C" and ProjectName == str :

        print("Creating the project...")
        system(f'mkdir {PythonFileLocaton}{ProjectName} && git init {PythonFileLocaton}{ProjectName}')
        print("")
        print(f'Project Locaton is {PythonFileLocaton}{ProjectName}')
    else:
        print("Error")
        
MakeTheaProject(argv[1], argv[2])

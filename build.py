import subprocess

subprocess.run(["pyinstaller", "main.py", "--onefile", "--windowed", "--add-data", "src:src", "-i", "./src/img/logo.ico"])
import subprocess

subprocess.run(["pyinstaller", "serenify.py", "--onefile", "--windowed", "--add-data", "src:src", "-i", "./src/img/logo.ico"])
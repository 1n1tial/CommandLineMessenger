import subprocess

subprocess.run(["powershell.exe", "Get-Date"],  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, check=True)

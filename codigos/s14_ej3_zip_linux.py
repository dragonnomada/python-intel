import subprocess

command = 'zip backup.zip s4_*.py'

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = process.communicate()

print("stdout:", stdout)
print("stderr:", stderr)

for line in stdout.decode('utf-8').split("\n"):
    print(line)
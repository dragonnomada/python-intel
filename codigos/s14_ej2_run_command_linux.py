import subprocess

command = ['date', '+"%A %B (%d %m)"', '-u']

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = process.communicate()

print("stdout:", stdout)
print("stderr:", stderr)

for line in stdout.decode('utf-8').split("\n"):
    print(line)
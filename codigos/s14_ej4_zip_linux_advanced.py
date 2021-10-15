import re
import subprocess

command = 'zip backup.zip s4_*.py'

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = process.communicate()

print("stdout:", stdout)
print("stderr:", stderr)

s = 0
n = 0
for line in stdout.decode('utf-8').split("\n"):
    p = 0
    for capture in re.finditer(r"deflated\s+(\d+.?\d*)%", line):
        p = float(capture.group(1))
    print(line, p)
    s += p
    n += 1

print("TOTAL ZIP FILES: {} | DEFLATED AVG: {:.1f}%".format(n, s / n))
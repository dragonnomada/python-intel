import subprocess

def create_folder(name):
    command = 'mkdir -p {}'.format(name)

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    if len(stderr) > 0:
        return stderr.decode('utf-8').split("\n")

    return []

def create_file(name, content):
    command = 'echo "{}" > {}'.format(content, name)

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    if len(stderr) > 0:
        return stderr.decode('utf-8').split("\n")

    return []

def date_when(description, args = ""):
    command = 'date -d "{}" +"%Y:%m:%d:%H:%M:%S:%z" {}'.format(description, args)

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    date = [int(part) for part in stdout.decode('utf-8').split("\n")[0].split(":")]

    [year, month, day, hours, minutes, seconds, utc] = date

    doc = {
        "year": year,
        "month": month,
        "day": day,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "utc": utc,
    }

    return doc

def list_files(ftype = "*"):
    command = 'ls {}'.format(ftype)

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    return stdout.decode('utf-8').split("\n")

def copy_file(source, target):
    command = 'cp {} {}'.format(source, target)

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    return stdout.decode('utf-8').split("\n")
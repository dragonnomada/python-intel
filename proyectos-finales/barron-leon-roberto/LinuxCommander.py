##Libreria que usas subproces para hacer llamadas de Linux
import subprocess

def create_folder(name):
    command = 'mkdir {}'.format(name)

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

#   Return a list with all the files listed in the provided path
#   Path:  PAth to be listed. Default Value = ""
#   ftype input options for the ls command. Default value
def list_files(path="", ftype = "",EnableLogs=True):
    command = 'ls {} {}'.format(path,ftype)

    if(EnableLogs):
        print (command)

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()
    #print (stdout)

    return stdout.decode('utf-8').split("\n")

def copy_file(source, target):
    command = 'cp {} {}'.format(source, target)

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    return stdout.decode('utf-8').split("\n")


#   Unzip a file
#   Path:       filename or path to zip
#   options:    zip options to set as input in the command. default is overwritting the old folder if exist
#   EnableLogs: Enable the display output in the console True as default
def unzip_file(path,options="-o",EnableLogs=True):

    command = 'unzip '+options+" "+path

    if(EnableLogs):
        print (command)

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    if(EnableLogs):
        print("stdout:", stdout)
        print("stderr:", stderr)

    if(EnableLogs):
        for line in stdout.decode('utf-8').split("\n"):
            print(line)

#Send the generic command to Linux console
def generic_command(comand_input=""):

    subprocess.Popen("ls", cwd="/")#

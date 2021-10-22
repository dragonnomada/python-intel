
from os import chdir
import LinuxCommander
import random

class Reporte:

    #### Global Vaiables
    Dev_dict = {}           #Git Developer Master Dictionary Structure to keep all the commit info
    RequiredCommits=0       #Global field of number of commits requested by the used
    RequiredDate= "Today"   #Date limit used for the commit. Format yyyy/mm/dd

    EnableTraces= False
    numberOftest=0
    numberOfErrors=0
    numberOfCodeCommits=0

    ErrorList={}       #Dictionary used to kept track of errors identified in files

    def getGitLogInfo(self,log):
        f = open(log, "r")

        commit_number=0             #Variable to track the number of commits we read from the file
        current_commit_number = 1   #Variable to keep track of the number of commits saved in the master dict

        for line in f:  #Moving trough the log file line by line

            if (len(line.split()) == 0):    #Ignoring empty lines
                continue

            #If there is content then we start filtering
            #Getting the respective field according to the line content in the log
            if (line.startswith("commit")):
                if (commit_number==current_commit_number):     #We found a new commit save old values in the master dict and start a new record
                    self.Dev_dict[current_commit_number]={"commit_id": commit_id, "author":author,"mail":mail, "date":date, "comment":comment }
                    current_commit_number= current_commit_number+1

                commit_number=commit_number+1   #We found a new commit
                temp_fields=line.split()        #We split the Fields
                commit_id=temp_fields[1]        #Extracting the commitid

            elif(line.startswith("Author")):
                temp_fields=line.split()        #We split the Fields
                author=line[8:line.find("<")-1] #Extracting the author name
                mail=line[line.find("<")+1:-2]  #Extracting the email from the line
            elif(line.startswith("Date")):
                date=line[8:-1                  ]#Extracting the date
            else:
                #Any other comment should be a comment or requires a new field
                comment=line.strip().rstrip()   #trimming special characters
        f.close()

    #Print all commits in the master dict
    def showcommits(self):
        for x in self.Dev_dict:
            print(x,self.Dev_dict[x])

    def ReadReport(self):
        LinuxCommander.create_folder("LogResults")

    #Return a list of namefiles that includes the filetype in the name
    #Loglist:   Listof files obtaned from LinuxCommander.list_files
    #Filetype:  type of file that want to extract from the LogList
    def file_filter(self,Loglist, filetype="log"):

        listfiles =[]
        for filename in Loglist:
            if (filetype in filename):
                listfiles.append(filename)
        return listfiles

    def create_file(self,Name="NoName.txt",DefaultInputText=[]):
        f = open(Name, "w")
        for Line in DefaultInputText:
             f.write(Line+"\n")
        f.close()

    def check_errors(self,LogList="LogList.txt"):

        FileList = open(LogList, "r")   #The file including all the logs filenames
        ErrorFoundFlag= False           #Flag to keep track if an error was found in the logs
        ErrorList={}
        ErrorList["ErrorFlagInfo"]={"ErrorFoundFlag":ErrorFoundFlag}

        self.logger("Verifiying errors in files")

        for FileName in FileList:   #Opening file by file to check for errors in the File List

            self.logger("Verifiying errors in {}".format(FileName))
            file = open(".\\Logs\\"+FileName.strip(),"r")   #opening a particular file
            LineNumber=0
            self.numberOftest=self.numberOftest+1

            for Line in file:           #Check Line by line if there is an ERROR message

                LineNumber=LineNumber+1
                if "ERROR:" in Line:
                    self.logger("Error Found in {} in line {} with code ->{} ".format(FileName, LineNumber, Line))
                    ErrorList[FileName]={"LineNumber":LineNumber,"Line":Line.strip()}
                    ErrorFoundFlag= True

            file.close
            LineNumber=0
        FileList.close()
        ErrorList["ErrorFlagInfo"]={"ErrorFoundFlag":ErrorFoundFlag}
        return ErrorList

    def logger(self,message=""):
        if self.EnableTraces:
            print(message)

    def parseLogs(self,options="-o", TraceEnabled=False):

        print ("Unzipping the Logs")
        LinuxCommander.unzip_file("Logs.zip",options,TraceEnabled) #Unzip the logs folder. It overwritte old content if exist
        print ("  Logs decompressed.\nGetting the file names from the logs ")
        listfiles=self.file_filter(LinuxCommander.list_files(".\\Logs\\","*.log", EnableLogs=False),".log")
        self.create_file(Name="LogList.txt",DefaultInputText=listfiles)
        print("  LogList file created.\n  Checking for errors")
        self.ErrorList=self.check_errors("LogList.txt")
        if (self.ErrorList["ErrorFlagInfo"]["ErrorFoundFlag"] == True):
            print("Errors Detected in logs->> Error LogList file created ")
            print (self.ErrorList)
        else:
            print("No Errors detected in Logs")

    def createHTMLReport(self):
        print("Creating the LogReport folder")
        LinuxCommander.create_folder("LogReport")
        print("Creating the error report")
        self.createErrorReport()
        print("Creating the developer list")
        self.createGitLogReport()
        print("Data generated correctly. Creating Main Page")
        self.createMainLogReport()
        print("Report created successfully")

    def createErrorReport(self):

        Template = open(".\\Inputs\\Template.HTML", "r")   #The file including all the logs filenames
        ErrorReport= open(".\\LogReport\\ErrorReports.HTML", "w")   #The file including all the logs filenames


        for Line in Template:
            if "<th>ContentTitle</th>" in Line:
                ErrorReport.write("			<th>Error Report</th>")
            elif "<td>Content</td>" in Line:
                ErrorReport.write("			<td>\n			    <table>\n")
                ErrorReport.write("			        <th>Module</th><th>Line</th><th>Error Code</th> \n")
                for Error in self.ErrorList:                 #Writting the rest of Error Content
                    self.numberOfErrors=self.numberOfErrors+1
                    if "ErrorFlagInfo" not in Error:         # skipping the ErrorFlag Content
                        ErrorReport.write("			        <tr>\n			            <td> {}</td> \n".format(Error.strip()))
                        for LineNumber in self.ErrorList[Error]:
                            ErrorReport.write("			            <td>{}</td>\n".format(self.ErrorList[Error][LineNumber]))
                        ErrorReport.write("			        </tr> \n")
                ErrorReport.write("			   </table>\n			</td>\n")
            else:
                ErrorReport.write(Line)
        Template.close()
        ErrorReport.close()

    def createGitLogReport(self):

        Template = open(".\\Inputs\\Template.HTML", "r")   #The file including all the logs filenames
        CommitReport= open(".\\LogReport\\CommitReport.HTML", "w")   #The file including all the logs filenames

        for Line in Template:
            if "<th>ContentTitle</th>" in Line:
                CommitReport.write("			<th> Commit Report Info</th>")
            elif "<td>Content</td>" in Line:
                CommitReport.write("			<td>\n			    <table>\n")
                CommitReport.write("			        <th>Commit No.</th><th>commit_id</th><th>author</th><th>mail</th><th>date</th><th>comment</th> \n")
                for Commit in self.Dev_dict:                 #Writting the rest of Error Content
                    CommitReport.write("			        <tr>\n			            <td> {}</td> \n".format(Commit))
                    for CommitInfo in self.Dev_dict[Commit]:
                            CommitReport.write("			            <td>{}</td>\n".format(self.Dev_dict[Commit][CommitInfo]))
                            if "author" in CommitInfo:
                                if "Generic Autobuilder" not in self.Dev_dict[Commit][CommitInfo]:
                                    #print(self.Dev_dict[Commit][CommitInfo])
                                    self.numberOfCodeCommits=self.numberOfCodeCommits+1
            else:
                CommitReport.write(Line)
        Template.close()
        CommitReport.close()

    def createMainLogReport(self):
        Template = open(".\\Inputs\\Template.HTML", "r")   #The file including all the logs filenames
        MainReport= open(".\\LogReport\\Main.HTML", "w")   #The file including all the logs filenames

        for Line in Template:
                    if "<th>ContentTitle</th>" in Line:
                        MainReport.write("			<th>Abstract Info</th>\n")
                    elif "<td>Content</td>" in Line:
                        MainReport.write("<td>")
                        MainReport.write("<OL>")
                        MainReport.write("<LI> Number of performed test: {}\n".format(self.numberOftest))
                        MainReport.write("<LI> Number of identified Errors: {}\n".format(self.numberOfErrors))
                        MainReport.write("<LI> Number of commited code files: {}\n".format(self.numberOfCodeCommits))
                        MainReport.write("</OL>")
                        MainReport.write("</td>")
                    else:
                        MainReport.write(Line)
        Template.close()
        MainReport.close()

#Not relevant for module. Created to generate Dummy Logs for testint the module
    def createDummyLogs(self):
        Filenames = open(".\\Inputs\\LogList.txt", "r")

        for FileName in Filenames:
            tempfile = open(".\\Logs\\"+FileName.strip(), "w")
            Lines=random.randint(1, 300)
            for line in range(0, Lines):
                Error=random.randint(1,1000)
                if Error < 2:
                    dummyvalue=random.randint(1,200)
                    tempfile.write("ERROR: Automated Test Failure!! Failed on SED:{} Expected Value:{} Obtained:{}.\n".format(line,random.randint(1,200),dummyvalue,dummyvalue+random.randint(1,10)))
                else:
                    tempfile.write("Automated Test: Corrent Value\n")
            tempfile.close()
        Filenames.close()

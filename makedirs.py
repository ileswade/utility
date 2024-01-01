from os import listdir
import dateparser
from datetime import datetime
from os.path import isfile, join

import os

def parse(inbound):
    isSubmissionFile=False
    filename, submittedFileExtension = os.path.splitext(inbound)
    segments = filename.lower().strip().split(' - ', 3)
    isSubmissionFile = (len(segments)==4)
    if isSubmissionFile: 
        fileCode, studentName, sumbissionDate, submittedFileName = segments
        if (studentName[0]=="."): studentName = studentName[1:].strip()  ##  Remove ". " in student name if present
        sumbissionDate = sumbissionDate[:-5]+":"+sumbissionDate[-5:]    ## Add a colon between hours and minutes
        x = dateparser.parse(sumbissionDate)
        submissionDateString = x.strftime("%y%m%d%H%M")
        newFolder = studentName + "("+submissionDateString+")"
        newFile = submittedFileName+submittedFileExtension
        return newFolder, newFile, submittedFileExtension
    else:
        return None, None, None
    
## Get Files
my_path = os.path.dirname(os.path.realpath(__file__))
files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

for file in files:
    folder, newfile, extension = parse(file)
    if folder:
        print (f"{folder}@{newfile}@{extension}@{file}")
        ## Make folder if it doesnt exist
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        ## Move the file to the new folder
        old = os.getcwd()+"/"+file
        new = os.getcwd()+"/"+folder+"/"+newfile
        os.rename(old, new)


        ## Unzip it if it is a zip file?

        ## remove it once unzipped
    else:
        print (f"NOT SUBMISSION@{file}")





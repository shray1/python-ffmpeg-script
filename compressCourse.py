import os
import sys
from videoCompress import executeCompression , copyFile

if(len(sys.argv)!=2):
	print(". . . Kindly give the path to the folder. :) " )
	exit()

logFile = open("logCompressCourse" , "w")

cmdargs = str(sys.argv)
pathToFolder = os.path.expanduser(sys.argv[1])
if not (pathToFolder.endswith("/")):
	pathToFolder = pathToFolder + "/"

print(". . . Path to folder is : " , pathToFolder)
logFile.write(". . . Path to folder is : " + pathToFolder)

listOfFolders = []
for file in os.listdir(pathToFolder):
	if os.path.isdir(pathToFolder + file):
		listOfFolders.append(pathToFolder + file + "/")

listOfFolders.sort()
foldersProcessed = set(['Lecture 8 - SegmentTree - 1'])

print ("List of Folders to process = ", listOfFolders)
print ("List of Folders already processed : " , foldersProcessed)


for folder in listOfFolders:
	baseFolder  = folder.split("/")
	baseFolder = baseFolder[len(baseFolder)-2]
	if baseFolder not in foldersProcessed:
		foldersProcessed.add(baseFolder)
		baseFolder = baseFolder.replace(" ", "_")
		outputdir = os.path.expanduser("~/Desktop/ML-CodingNinjas/"+baseFolder)
		if not (os.path.exists(outputdir)):
			os.mkdir(outputdir)
		if not (outputdir.endswith("/")):
			outputdir = outputdir + "/"
		
		print("Output director made is :  " , outputdir)
		print(". . . Processing Folder : " , folder)
		logFile.write("Output director made is :  " + outputdir)
		logFile.write(". . . Processing Folder : " +  folder)

		filesToProcess = []
		for file in os.listdir(folder):
			if(file.endswith(".mp4")):
				filesToProcess.append(file)
		filesToProcess.sort()
		#print(filesToProcess)
		executeCompression(filesToProcess , folder , outputdir, logFile)

print("DONE :) :D ")




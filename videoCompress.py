import os
import sys
#import tqdm


def copyFile(inputdir, outputdir , file ):
	child = os.system("cp " + "\"" + inputdir + file + "\"" +  "  \"" + outputdir+file + "\"" )
	if child == 0:
		return True
	return False

def executeCompression(filesToProcess , inputdir , outputdir , logFile=None):
	for file in filesToProcess:
		try: 
			moveForward = 1
			outputFile = file.replace(" ", "_")
			print (outputdir + outputFile )
			if not (os.path.exists(outputdir+file)):
				print("\n. . . Copying file")
				logFile.write("\n. . . Copying file")
				if(copyFile(inputdir, outputdir , file)):
					print ("\n. . . File copied : " , file)
					logFile.write("\n. . . File copied : " + file)					
				else:
					moveForward = 0;
			if (moveForward == 1):
				print("\n . . . Issuing Processing")
				logFile.write("\n . . . Issuing Processing")
				logFile.flush()
				exitStatus = os.system("/usr/local/bin/ffmpeg -i " + "\"" + outputdir + file + "\"" + " -vcodec h264 -acodec mp2 " +  " \"" +outputdir +  outputFile  + "\"")
				
				print ("\n. . . Processing Done. ")
				logFile.write("\n . . . Processing Done.")
				logFile.flush()
				
				os.system("rm -rf  " + "\"" +  outputdir + file +  "\"")
				print("\n. . . Input File Deleted")
				logFile.write("\n . . . Input file deleted.")
				logFile.flush()
				
				if logFile:
					if exitStatus == 0:
						logFile.write("\nFinised doing file " + outputFile + "\n")
						logFile.flush()
						print("\nFinised with file " + outputFile + "\n" , flush=True)
					else : 
						logFile.write("\nERROR :: EXIST STATUS = " + str(exitStatus) +  "for. file :" + file + "\n")
						logFile.flush()
						print("\nERROR :: EXIST STATUS = ", str(exitStatus) , "for. file :" , file , "\n",flush=True)
			else:
				print ("\nERROR : RETURN STATUS NOT 0 for Copying file : ", file)
				logFile.write("\nERROR : RETURN STATUS NOT 0 for Copying file : " + file)
				logFile.flush()

		except Exception as e:
			print("\nERROR : SOME ERROR OCCURED FOR FILE " , file)
			print("type error: " + str(e))
			logFile.write("\nERROR : SOME ERROR OCCURED FOR FILE : " + file)
			logFile.write("type error: " + str(e))
			logFile.flush()
	return


#executeCompression(filesToProcess , logFile)

#ffmpeg -i input.mp4 -vcodec h264 -acodec mp2 output.mp4

#https://stackoverflow.com/questions/8500047/how-to-inherit-stdin-and-stdout-in-python-by-using-os-execv

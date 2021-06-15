import os
import time
import psutil
from sys import *
import schedule
import yagmail


def ProcessDisplay(FolderName="Process"):

	
	Data=[]

	if not os.path.exists(FolderName):
		os.mkdir(FolderName)		
		
	File_Path= os.path.join(FolderName,"ProcessList%s.log"%time.ctime())
	File_Path=(File_Path.replace(" ","").replace(":",""))

	fd=open(File_Path,"w")
		

	for proc in psutil.process_iter():
		value=proc.as_dict(attrs=["pid","name","username"])
		Data.append(value)
		
	for element in Data:
		fd.write("%s\n"%element)

	yag_smtp_connection = yagmail.SMTP( user="adityapardeshi0078@gmail.com", password="***********", host='smtp.gmail.com')

	yag_smtp_connection.send(
    		to="adityapardeshi0078@gmail.com",
    		subject="Current Processes Running Activities",
    		contents="Your list of currently executing processes are attached in the textfile in the attachment", 
    		attachments=File_Path,
	)

def main():
	
	print("----Periodic Process Logger Script----")
	print("Script Title:"+argv[0])
	
	
	if((argv[1]=="-u") or (argv[1]=="-U")):				
		print("Usage: Application_Name Schedule_Time Directory_Name")
		exit()

	
	if((argv[1]=="-h") or (argv[1]=="-H")):				
		print("Help: It is Used to create log file of running processes")
		exit()


	schedule.every(int(argv[1])).minutes.do(ProcessDisplay)

	while True:
		schedule.run_pending()
		time.sleep(1)
	
	
	
if __name__=="__main__":
	main()
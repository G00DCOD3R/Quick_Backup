import shutil, sys
from datetime import datetime

USER_NAME = 'USER_NAME' # specify user who does backup, you can leave it empty but it can cause some problems
destination_path = '/example/path/my_backups/' # specify path where folder with backup will be stored (with '/' at the end)
BACKUP_NAME = ''

#   If you leave this empty, then BACKUP_NAME 
#   becomes "Backup-dd-mm-yyyy", or other format you specify in set_name()
#   otherwise, script won't change it

def path_conv(path):
	
	#   removing white characters from the end
	#   and converting '~' to /home/USER_NAME
	#   path starts with '/'
	
	if len(path) == 0:
		return False
	last = len(path)
	while last > 0 and path[last - 1] == " ":
		last -= 1
	if last == 0:
		return False
	path = path[0:last:1]
	if path[0] == '~':
		path = '/home/' + str(USER_NAME) + path[1:len(path):1]
	if path[0] != '/':
		path = '/' + path

	return path
	

def make_backup(path):
	path = path_conv(path)
	if not path:
		return
	#   print(path, destination_path + path[6 + len(USER_NAME):len(path):1])
	print("Copying: {}".format(path))
	shutil.copytree(path, destination_path + path[6 + len(USER_NAME):len(path):1])
	
	
def set_name():
	Now = datetime.now()
	global BACKUP_NAME
	BACKUP_NAME = "Backup-" + Now.strftime("%d-%m-%Y")
	
	#   other options: (you can add your own)
	#   BACKUP_NAME = "Backup-" + Now.strftime("%d-%m-%Y-%H:%M")
	#   BACKUP_NAME = "Backup-" + Now.strftime("%d-%B-%Y")
	#   BACKUP_NAME = "Backup-" + Now.strftime("%d-%b-%Y")

def main():
	
	if not BACKUP_NAME:
		set_name()
	global destination_path
	destination_path = destination_path + BACKUP_NAME
	
	print("do you want to create a backup in this \n{}\ndirectory? [y/n]".format(destination_path))
	my_option = input()
	if my_option[0] != 'y' and my_option[0] != 'Y':
		print("Aborted")
		return
	
	if len(sys.argv) == 1:
		raise Error("no input file")
	data = open(sys.argv[1], 'r').read()
	files_to_backup = data.splitlines()
	
	for paths in files_to_backup:
		make_backup(paths)
	
	shutil.copy2(str(sys.argv[1]), destination_path + "/BackupInfo.ignore")
	#   Additional info for restoration

if __name__ == "__main__":
	
	main()

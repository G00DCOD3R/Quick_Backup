import shutil, sys
 
#   ***WARNING***
#   This script can remove some directories if they occur at destination 
#   But every time it will ask you for permission
#   I recommend to remove useless files manually 

USER_NAME = 'USER_NAME'
source_path = '/example/path/my_backups/backup_folder_name' # specify folder with backup files (without '/' at the end)

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
	
def restore(path):
	path = path_conv(path)
	if not path:
		return
	print("Copying: {}".format(path), end = " ")
	try:
		shutil.copytree(source_path + path[6 + len(USER_NAME):len(path):1], path)
		print("Done")
	except FileExistsError:
		print("\nSuch directory already exists!\nDo you want to REMOVE it? (this operation cannot be undone) [y/n]")
		my_option = input()
		if my_option[0] != 'y' and my_option[0] != 'Y':
			print("Skipped")
			return
		shutil.rmtree(path)
		shutil.copytree(source_path + path[6 + len(USER_NAME):len(path):1], path)

def main():
	data = open(source_path + '/BackupInfo.ignore', 'r').read()
	files_to_restore = data.splitlines()
	
	for paths in files_to_restore:
		restore(paths)

if __name__ == "__main__":
	
	main()

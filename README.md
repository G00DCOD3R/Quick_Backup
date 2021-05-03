# Quick_Backup
quick and simple script for making backups 

# usage 
- specify user name and source / destination path in backup.py and restore.py
- prepare file with links to direstories you want to backup, each in new line. e.g.
```
~/one
~/two
~/three
```
- pass this file as argument in backup.py:
``` python3 backup.py input_file```
- restoring with this script only works when backup was made with it too :)
``` python3 restore.py ```

Script can be run at any directory, but I found it convienient to keep it with backup files

It's not that hard to modify for your purposes

Sometimes errors may occur, because I didn't test it much

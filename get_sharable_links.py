import dropbox
import csv
import os

dbx = dropbox.Dropbox('*********************************') #dropbox api secret
for foldername in ["/Dir 1", "/Dir 2"] :
	filesList = []
	print "creating links for folder " + foldername
	files = dbx.files_list_folder('/'+foldername)
	filesList.extend(files.entries)
	print len(files.entries)

	while(files.has_more == True):
		files = dbx.files_list_folder_continue(files.cursor)
		filesList.extend(files.entries)
		print len(files.entries)
	
	csvfile = open('Files/' + foldername + '.csv',"a+")
	os.chmod(csvfile.name, 0777)
	for file in filesList:
		filename = file.name + ','
		link_data = dbx.sharing_create_shared_link(file.path_lower)
		filename += link_data.url + '\n'
		csvfile.write(filename)
		print file.name
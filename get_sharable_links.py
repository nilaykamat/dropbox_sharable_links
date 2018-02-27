import dropbox
import csv
import os


def create_links(foldername, csvfile) :
	filesList = []
	print "creating links for folder " + foldername
	files = dbx.files_list_folder('/'+foldername)
	filesList.extend(files.entries)
	print len(files.entries)

	while(files.has_more == True):
		files = dbx.files_list_folder_continue(files.cursor)
		filesList.extend(files.entries)
		print len(files.entries)
	
	for file in filesList:
		if (isinstance(file, dropbox.files.FileMetadata)):
			filename = file.name + ','
			link_data = dbx.sharing_create_shared_link(file.path_lower)
			filename += link_data.url + '\n'
			csvfile.write(filename)
			print file.name
		else: 
			create_links(foldername+'/'+file.name, csvfile)


dbx = dropbox.Dropbox('*********************************') #dropbox api secret
global filesList
for foldername in ["/Dir 1", "/Dir 2"] :
	filesList = []
	csvfile = open('Files/' + foldername + '.csv',"a+")
	os.chmod(csvfile.name, 0777)
	print "creating links for folder " + foldername
	create_links(foldername, csvfile)
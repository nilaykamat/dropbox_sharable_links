import dropbox

dbx = dropbox.Dropbox('*********************************') #dropbox api secret
for foldername in ["/Dir 1", "/Dir 2"] :
	print "creating links for folder " + foldername
	files = dbx.files_list_folder(foldername)
	for file in files.entries:
		filename = file.name + ', '
		link_data = dbx.sharing_create_shared_link(file.path_lower)
		filename += link_data.url
		print filename

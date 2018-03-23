import dropbox
import csv
import os
import random
import string
from threading import Thread

def create_links(foldername, csvfile) :
    filesList = []
    print("creating links for folder " + foldername)
    try : 
        files = dbx.files_list_folder('/'+foldername)
        filesList.extend(files.entries)
        print(len(files.entries))

        while(files.has_more == True) :
            files = dbx.files_list_folder_continue(files.cursor)
            filesList.extend(files.entries)
            print(len(files.entries))

        for file in filesList :
            if (isinstance(file, dropbox.files.FileMetadata)) :
                filename = file.name + ',' + file.path_lower + '\n'
                # link_data = dbx.sharing_create_shared_link(file.path_lower)
                # filename += link_data.url + '\n'
                csvfile.write(filename)
                print(file.name)
            else :
                create_links(foldername+'/'+file.name, csvfile)
    except :
        print "Exception Happened"
        print foldername

def start(api_key, folders) :
    global dbx
    global filesList
    dbx = dropbox.Dropbox(api_key) #dropbox api secret

    directory = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    os.makedirs('Files/'+ directory)

    for foldername in folders :
        filesList = []
        nameOfFile = foldername.split('/')
        csvfile = open('Files/' + directory + '/' + nameOfFile[-1] + '.csv',"a+")
        os.chmod(csvfile.name, 0777)
        t = Thread(target=create_links, args=(foldername, csvfile))
        t.start()
    
    return {"status":True, "message":"Successfully queued for generating links", "token":directory}
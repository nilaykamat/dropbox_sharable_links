import dropbox
import csv
import os
import json
from time import gmtime, strftime
import random
import string
import urllib
from threading import Thread
from tinydb import TinyDB, Query

global BASE_URL
BASE_URL = os.path.dirname(os.path.realpath(__file__)) 

def create_links(foldername, csvfile) :
    filesList = []
    print("creating links for folder " + foldername)
    files = dbx.files_list_folder('/'+foldername)
    filesList.extend(files.entries)
    print(len(files.entries))
    
    while(files.has_more == True) :
        files = dbx.files_list_folder_continue(files.cursor)
        filesList.extend(files.entries)
        print(len(files.entries))

    for file in filesList :
        if (isinstance(file, dropbox.files.FileMetadata)) :
            filename = file.name + ',' + file.path_lower + ','
            link_data = dbx.sharing_create_shared_link(file.path_lower)
            filename += link_data.url + '\n'
            csvfile.write(filename)
            print(file.name)
        else :
            create_links(foldername+'/'+file.name, csvfile)


def thread_lifecycle(foldername, csvfile, token) :
    # pre execution code
    # Link creation execution
    try :
        create_links(foldername, csvfile)
	update_end_time(foldername, token, 2)
    except : 
        update_end_time(foldername, token, 1)


def start(api_key, folders) :
    global dbx
    global filesList

    dbx = dropbox.Dropbox(api_key) #dropbox api secret

    directory = generate_random_token()
    os.makedirs(BASE_URL + '/Files/'+ directory)
    
    for foldername in folders :
	foldername = urllib.unquote(foldername)
        nameOfFile = get_file_name(foldername)
        
        filePath = BASE_URL + '/Files/' + directory + '/' + nameOfFile + '.csv'
        csvfile = create_csv(filePath)
        
        listElem = {
		'token' : directory,
	        'file_path' : filePath,
        	'folder_name' : foldername,
	        'start_time' : strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        	'end_time' : False,
		'status' : 0
        }
    	save_collection_to_db(listElem)

        t = Thread(target=thread_lifecycle, args=(foldername, csvfile, directory))
        t.start()
    
    return {"status":True, "message":"Successfully queued for generating links", "token":directory}

def save_collection_to_db(collection) :
    db = TinyDB(BASE_URL + '/Database/db.json')
    db.insert(collection)

def update_end_time(foldername, token, status) :
    db = TinyDB(BASE_URL + '/Database/db.json')
    Token = Query()
    db.update({'end_time': strftime("%Y-%m-%d %H:%M:%S", gmtime()), 'status': status}, (Token.token==token) & (Token.folder_name==foldername))

def get_token_status(token) :
    db = TinyDB(BASE_URL + '/Database/db.json')
    Token = Query()
    return db.search(Token.token==token)

def get_file_name(foldername) :
	nameOfFile = foldername.split('/')
	return nameOfFile[-1]

def create_csv(filePath) :
	csvfile = open(filePath, "a+")
	os.chmod(csvfile.name, 0777)
	csvfile.write('File Name, File Path, Sharable Link \n')
	return csvfile

def generate_random_token() :
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))



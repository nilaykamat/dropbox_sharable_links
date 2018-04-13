from tinydb import TinyDB, Query
import get_sharable_links
import json
import sys
import os

global BASE_URL
BASE_URL = os.path.dirname(os.path.realpath(__file__))

def update_status() :
    db = TinyDB(BASE_URL + '/Database/db.json')

    for collection in db.all() :
        if collection['end_time'] != False :
            get_sharable_links.update_end_time(collection['folder_name'], collection['token'], 2)

def get_status() :
    db = TinyDB('./Database/db.json')
    print db.all()


function = globals()[sys.argv[1]]
function()

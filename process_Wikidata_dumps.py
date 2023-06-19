# This scipt process the xml dumps. We use threading to read the files in parallel. The function extraction2 reads the xml dump and 
# extractes the pages for items talk pages and proeprty talk pages (namespace 1 and 121 respectively). The script creates a csv file for every page.

import xml.etree.ElementTree as etree
from bz2 import BZ2File
import pandas as pd
import json
import codecs
import csv
import os
import re
import logging
import threading
import concurrent.futures
import tracemalloc


def extraction2(file_name):
    prefix = '{http://www.mediawiki.org/xml/export-0.10/}'
    p_title = prefix + 'title'
    p_ns = prefix + 'ns'
    p_id = prefix + 'id'
    p_timestamp = prefix + 'timestamp'
    p_page = prefix + 'page'
    p_revision = prefix + 'revision'
    p_username = prefix + 'username'
    p_ip = prefix + 'ip'
    p_text = prefix + 'text'
    
    
    p_list = []

    c_page = None
    c_revision = None
    c_username = None
    c_timestamp = None
    c_title = None
    c_ns = None
    c_text = None
    c_ip = None
    revisions = []
    user_edits_timestamps={}
    

    
    # We keep a stack of 'breadcrumbs', i.e. all open elements to this point
    path = []
    with BZ2File(str(PATH_read)+str(file_name)) as xml_file:

        # open the file to save discussions' text
        hfile = codecs.open(str(PATH_save)+str(file_name[:-4])+'_DiscussionPage.csv', 'w', encoding='utf-8')
        hfilecsv = csv.writer(hfile)
        hfilecsv.writerow(['page_title','namespace', 'text'])

        # displaying the memory
        print(tracemalloc.get_traced_memory())

        for event, elem in etree.iterparse(xml_file, events=('start','end')):
            if event == 'start':
                path.append(elem.tag)
            elif event == 'end':
                if elem.tag in p_list: # Printing all elements we are interested in in p_list
                    # print(path)
                    # print(elem.tag, elem.text)
                    continue
                # page info
                if elem.tag == p_title and p_page in path: # store the page title
                    c_title = elem.text
                if elem.tag == p_ns and p_page in path: # store the page namespace
                    c_ns = elem.text
                    # print(c_ns)
                #revision info
                if elem.tag == p_id and p_revision in path: # Store revision ids
                    c_revision = elem.text
                if elem.tag == p_timestamp: # Store revision timestamp, always after revision id
                    c_timestamp = elem.text
                if elem.tag == p_ip: # store editor's name
                    c_ip = elem.text                  
                if elem.tag == p_username: # store editor's name
                    c_username = elem.text
                if elem.tag == p_text: # store revision text
                    c_text = elem.text
                    # store usernames in revisions with the timestamp 
                    if c_username is None and c_ip:# check if c_username is None and istead the re is c_ip
                        c_username = c_ip
                    if c_username is None and c_ip is None:
                        c_username = 'username_and_ip_are_None'
                    
                    if c_username in user_edits_timestamps.keys(): # check if the username exist in the dictionary
                        user_edits_timestamps[c_username].append(c_timestamp) # if username exists store the timestamp of the revision
                    else: user_edits_timestamps[c_username]=[c_timestamp] # if username does not exist add it as key and store the timestamp
                    
                    if c_ns in ['1','121']: # list of the discussion page namespaces                  
                        revisions.append((c_revision, c_timestamp, c_username, c_text))#store revisions
                
                if elem.tag == p_page: # End of a page, get most recent revision text 
                    if c_ns in ['1','121']: # list of the discussion page namespaces                  
                        revisions_sorted = sorted(revisions, key=lambda tup: tup[1], reverse=True) # Order list of tuples by second field (timestamp), descending order
                        hfilecsv.writerow([c_title,c_ns,revisions_sorted[0][3]])
  
                    revisions = []

                path.pop()
        

    
#===========================
#threading process


ENCODING = "utf-8"

PATH_read='Dumps/'
PATH_save='Discussion_files/'
start_file=0
end_file=1


if not os.path.exists(PATH_save):
        os.mkdir(PATH_save)


def thread_function(name):
    logging.info("Thread %s: starting", name)
    extraction2(name)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        executor.map(thread_function, [f'dump_{i}.bz2' for i in range(start_file,end_file)])

    
# This scripts download the dump files from Wikidata dumps. The dumps have data from the begining since Novemer 2021.
#extra files for this script - 1. wikidata_urls_Nov_2021.txt
#output - Folder: dumps_xml_Nov2021


import urllib.request
import os
import bz2


# path to save files
PATH='Dumps/'


#create  folder to save the dumps
if not os.path.exists(PATH):
   os.mkdir(PATH)


#read the urls form the txt file   
file1 = open('dump_urls.txt', 'r')
Lines = file1.readlines()
# print(Lines[1443])


n=0 # number to name the dumps
for i in Lines:
   link=i[:-1]
   print('start: '+str(n)+'----'+str(link))
   urllib.request.urlretrieve(link, str(PATH)+'dump_'+str(n)+'.bz2')
   print("finished: "+str(n)+'----'+str(link))
   n +=1


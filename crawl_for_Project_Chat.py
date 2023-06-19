# This script use web crawl to extract discussion from Project Chat communication page in Wikidata. 
# It reads a list of urls with the archive files for Project Chat and extract discussions. It saves one file for each discussion.

import bs4 as bs
import urllib.request
import codecs
import csv
import re

ENCODING = "utf-8"


#open and read the csv to take the list with urls
#=============== change the csv file====================
with open('project_chat_urls.csv', newline='') as csvfile:
    csv_urls = csv.reader(csvfile, delimiter=' ', quotechar='|')
    header=next(csv_urls)
    for row in csv_urls:
    #row=next(csv_urls)
    #print(row)
        url=', '.join(row)

        subject='subject'
        thread='thread'
        #start the process to get the discussions
        #creat the csv
        name_file=re.sub(r'[^\w\s]', '', url[39:])
        print(name_file)
        #======================change the saved folder===================================
        FILENAME_ARTICLES = 'Project_chat/'+str(name_file)+'.csv'
        hfile = codecs.open(FILENAME_ARTICLES, 'w', ENCODING)
        hfilecsv = csv.writer(hfile)
        #hfilecsv.writerow(['subject', 'thread'])

        #start with the html
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source,'html.parser')
        #take the body part of the html. Is the one with the urls I am looking
        body_urls=soup.find('div', class_='mw-parser-output')

        children=body_urls.findChildren(recursive=False)
        #print(children[3])
        #subject=children.find_all(class_='mw-headline').get('id')

        num=0
        for beg in children:
            num += 1
            if (beg.has_attr('class') and beg['class'][0] == 'ext-discussiontools-init-section') or beg.name=='h3' or beg.name=='h2':
                    break

        for child in children[num-1:]:
            if (child.has_attr('class') and child['class'][0] == 'ext-discussiontools-init-section') or child.name=='h3' or child.name=='h2':
                hfilecsv.writerow([subject, thread])
                subject=child.find(class_='mw-headline').get('id')
                thread=''
            else:
                thread=thread+" "+child.get_text()
        hfilecsv.writerow([subject, thread])
        # try:
        #     element = 'div'
        #     assert element in ['div','h2','ul','p']
        #     ...

        # except AssertionError as e:
        #     print(element)
        #     raise e



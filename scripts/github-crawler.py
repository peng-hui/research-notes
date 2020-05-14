#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib2
import re, time, os
from multiprocessing import Process, Lock


def geturl(searchurl, filename):
    try:
        html_page = urllib2.urlopen(searchurl)
    except urllib2.HTTPError as e:
        if e.code == 429:
            time.sleep(5)
            geturl(searchurl,filename)
            return 
        else:
            pass
            return
    soup = BeautifulSoup(html_page, "html.parser")
    repo_list =  soup.findAll('a', attrs={'class': 'v-align-middle'})
    f = open(filename, 'a+')
    for repo in repo_list:
        url = 'https://github.com' + repo['href']
        f.write(url + '\n')
        print(url)
    f.close()

def getpageurl(url, pagenum, urldir):
    turl = url + '&p=' + str(pagenum)
    geturl(turl, os.path.join(urldir, str(pagenum) + '.txt'))
    return

def download(url, dstdir):
    command = 'git clone ' + url.rstrip('\n') + ' %s '% dstdir 
    print(command)
    os.system(command)

if __name__ == '__main__':
    url = 'https://github.com/search?l=PHP&o=desc&q=php&s=stars&type=Repositories'

    '''
    numofprocess = 1
    startpage = {0: 10, 1: 20, 2: 70, 3: 80}
    process = {}
    for num in range(numofprocess):
        process[num] = Process(target=crawlpage, args=(url, startpage[num], startpage[num] + 10 ))
        process[num].start()

    for num in range(numofprocess):
        process[num].join()
    '''


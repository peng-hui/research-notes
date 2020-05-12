#!/usr/bin/python3
import os, sys

filepaths = ['ACE', 'ACE-SEN', 'BDF', 'BDF-SEN']
dstpath = 'dst'

def move(src, dst):
    command = 'mv %s %s ' % (src, dst)
    #print(command)
    os.system(command)

def copy(src, dst):
    command = 'cp -rf %s %s ' % (src, dst)
    #print(command)
    os.system(command)

def mkdir(path):
    command = 'mkdir %s' % path
    #print(command)
    os.system(command)

def parse(path, dstpath):
    #countdir = 0
    #countfile = 0
    files = os.listdir(path)
    for f in files:
        if not f.endswith('.txt'): # hopefully the homework is not in .txt format :)
            sid = f.split('_')[1]
            f = f.replace(' ', '\ ').replace('(', '\(').replace(')', '\)')
            name = ''.join(f.split('_')[1:]).replace('\ ', '')
            dirpath = os.path.join(dstpath, sid)
            if not os.path.exists(dirpath):
                mkdir(dirpath)
                #countdir += 1
            copy(os.path.join(path, f), os.path.join(dirpath, name))
            #countfile += 1
    # print('countdir = %d countfiles = %d' %(countdir, countfile))

def select(path, dstpath, nt):
    fp = open(nt)
    sids = [i.rstrip() for i in fp.readlines()]
    fp.close()
    # count = 1 #row id in the table
    for sid in sids:
        srcpath = os.path.join(path, sid)
        count += 1
        if os.path.exists(srcpath):
            copy(srcpath, os.path.join(dstpath, str(count).zfill(3)))
        else:
            print('not found %s' %sid) 
    return

if __name__ == "__main__":
    if not os.path.exists(dstpath):
        mkdir(dstpath)
    for path in filepaths:
        parse(path, dstpath)
    #select(dstpath, 'mine', 'list.txt')



import os
import time
import shutil
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT
import logging

import kmlistfi

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui

import random



def _runCLargs(cmd,showCMD=True):
    '''
    executes command passed in. Vulnerable to attacks

    '''
    print(cmd)
    p = Popen(cmd , stdout = PIPE, stderr = STDOUT, shell = True)
    s = ''
    for line in p.stdout:
        #logging.info(line)
        print(line.decode("utf-8").rstrip())
        s+= line.decode("utf-8")
    
    return s

def _bodge_vanity_pagesave(url, save_id):
    

    br = webdriver.Firefox()
    br.get(url)

    time.sleep(5 + (0.5-random.random())*4)
    html = br.page_source


    # open 'Save as...' to save html and assets
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite(save_id)
    pyautogui.hotkey('enter')
    time.sleep(2 + (0.5-random.random())*1.5)

    br.quit()


    return

def _transfer_from_downloads_to_temp(save_id):


    # Migrate pages to from /home/ME/Downloads/ to temp/
    fls = kmlistfi.les('/home/keith/Downloads/')
    arxiv_fls = [x for x in fls if save_id in x]
    
    if len(arxiv_fls) == 0:
        return

    
    #os.path.dirname
    build_dirs = list(set([os.path.dirname(x).split('Downloads')[-1] for x in arxiv_fls]))

    folders_to_remove = []
    for a_dir in build_dirs:
        new_dir = 'temp'+a_dir
        #print(new_dir)
        if not os.path.isdir(new_dir):
            os.mkdir(new_dir)
            folders_to_remove.append('/home/keith/Downloads'+a_dir)

    for srcFile in arxiv_fls:
        dstFile = 'temp/'+ srcFile.split('Downloads/')[-1]
        #print(srcFile)
        #print(dstFile)
        shutil.move(srcFile, dstFile)
        
    # Finish by removing empty folder
    #print(folders_to_remove)
    for fld in folders_to_remove:
        os.rmdir(fld+'/')

    return
    


def main_arxiv_vanity_bodge(arxiv_source_url):

    '''
    A highly inadvisable solution to getting arxiv papers to my kindle
    but it is also simple, and can be itteratively improved, so it's 
    the solution that is currently being used


    Input: arxiv url
        |
        v
    Identify if url in arxiv pdf, or earlier in the site hierarchy
            Sample:
                https://arxiv.org/abs/1909.02128
                https://arxiv.org/pdf/1909.02128.pdf
                https://arxiv.org/format/1909.02128

        |
        v
    Make request to arxiv vanity, passing in arxiv page
            Sample:
                https://www.arxiv-vanity.com/papers/
                https://www.arxiv-vanity.com/papers/1909.02128/
                

        |
        v
    save resulting webpage as html
            Autogui bodge: this opens up a selenium browser instance which 
            saves in the default downloads folder location.

            If the arxiv vanity webpage needs to render, this messes up, 
            there are two solutions: using selenium, I can use a combination
            of waitforelement + some timeout condition, however I intend to 
            move away from arxiv vanity as a whole, so the next solution is 
            where I'll put my effort--Rather than using arxiv-vanity site 
            proper, navigate to arxiv.org/format/..., download `other format`
            and run the render engine arxiv vanity uses--latexML+engrafo
        |
        v
    Convert html files to epub (in hopes it maintains equations)
            This and the following steps are handled by `ebook-convert`,
            a function by Calibre ebook management library. 
        |
        v
    Convert epub to mobi
        |
        v
    return mobi path

    '''

    # Identify if url in arxiv pdf, or earlier in the site hierarchy
    raw_source = arxiv_source_url

    if '.pdf' in raw_source:
        parent_node = raw_source.strip('.pdf')
    else:
        parent_node = raw_source

    arxiv_id = parent_node.split('/')[-1]

    
    
    # Make request to arxiv vanity, passing in arxiv page
    arxiv_vanity_url = "https://www.arxiv-vanity.com/papers/" + arxiv_id

    # save resulting webpage as html
    _bodge_vanity_pagesave(arxiv_vanity_url, arxiv_id)

    # Transfer file to temp 
    _transfer_from_downloads_to_temp(arxiv_id)


    # convert to epub
    epub_title = '_'.join(arxiv_id.split('.')) + '.epub'
    print(epub_title)
    temp_path = os.path.abspath('temp')
    full_epub = temp_path + '/' + epub_title


    cmd = 'ebook-convert temp/' + arxiv_id + '.html ' + full_epub
    _runCLargs(cmd)

    # Convert to mobi
    mobi_title = '_'.join(arxiv_id.split('.')) + '.mobi'
    print(mobi_title)
    temp_path = os.path.abspath('temp')
    full_mobi = temp_path + '/' + mobi_title

    
    cmd = 'ebook-convert ' + full_epub + ' ' + full_mobi
    _runCLargs(cmd)

    return full_mobi




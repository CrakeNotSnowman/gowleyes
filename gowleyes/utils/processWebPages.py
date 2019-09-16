


import logging
import os



def joinAndMakeDir(parent, child):
    newDir = os.path.join(parent, child)
    if not os.path.exists(newDir):
        os.makedirs(newDir)
        logging.info("Making new directory: " + newDir)
    return newDir


def docFromURL(url):
    '''
    Classify URL, Then go to url and act accordingly

    For Arxive.org:
        See if URL is of a pdf, abstract, or 
    '''

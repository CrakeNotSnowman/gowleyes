


import argparse, textwrap
import logging
import os

from utils import docsToEReader
from utils import sendToEreader
from utils import processWebPages





def joinAndMakeDir(parent, child):
    newDir = os.path.join(parent, child)
    if not os.path.exists(newDir):
        os.makedirs(newDir)
        logging.info("Making new directory: " + newDir)
    return newDir

def interface():
    args = argparse.ArgumentParser(
        prog='main.py', 
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='A Document converter to prep and send files to my ereader',
        epilog=textwrap.dedent('''\
            Program currently does not take input.
        '''))
    args.add_argument('-q', '--quiet-mode', type=bool, default=False,\
                      help='[True/False] An input that is not currently used')
    args = args.parse_args()
    return args


def alskd():
    '''
    '''
    from utils import docsToEReader
    sourceTex_Filepath = "tests/test_format_src/tex/Basic_Tex/Simple_And_Plain/SimpleAndPlain.tex"
    output_Directory = "temp/"
    x = docsToEReader.latexSourceToHTML_htlatex(sourceTex_Filepath, output_Directory)
    #print(x)
    assert x >0

if __name__ == "__main__":
    #args = interface()
    #alskd()
    pass
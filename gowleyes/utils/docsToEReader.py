


import os
import time
import shutil
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT
import logging

import kmlistfi
import kmmessage
from utils import arxiv_vanity_bodge


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

_progLoc = ""
_progName = "ebook-convert"
_cmdPrefix = os.path.join(_progLoc, _progName)

'''
def minimap(fasta_filename, fastq1_filename, fastq2_filename, 
        outfile = "outfile.sam", read_length = "sr",
        thread_count=1, R="'@RG\\tID:K12\\tSM:K12'",
        outputToSAM=True,
        returnString=False, justBuildCMD=False):
    fasta = os.path.abspath(fasta_filename)
    fastq1 = os.path.abspath(fastq1_filename)
    fastq2 = os.path.abspath(fastq2_filename)
    thread_count = str(thread_count)

    conditionals = ""
    if outputToSAM:
        conditionals += " -a "

    cmd = _cmdPrefix  + ' -t ' + thread_count + ' -ax ' + read_length + \
        ' -R ' + R +  ' ' + conditionals + ' ' + \
        fasta + ' ' + fastq1 + ' ' + fastq2 + ' > ' + outfile

    if justBuildCMD:
        return cmd
    s = runprogs._runCLargs(cmd)
    if returnString:
        return s
    return
'''


def _runCLargsAndLog(cmd):
    '''
    executes command passed in. Vulnerable to attacks

    '''
    p = Popen(cmd , stdout = PIPE, stderr = STDOUT, shell = True)
    for line in p.stdout:
        logging.info(line)
    return




def compressFilesZip(file_list, output_filename):
    return


def sendToKindle(mobi_path):
    full_path = os.path.abspath(mobi_path)
    kmmessage.message_Send_Full_Email([''], 'convert.', '', [full_path])
    return

def HTMLtoMobi():

    _progLoc = ""
    _progName = "ebook-convert"
    _cmdPrefix = os.path.join(_progLoc, _progName)
    return


def HTMLtoEpub(htmlFilePath):

    _progLoc = ""
    _progName = "ebook-convert"
    _cmdPrefix = os.path.join(_progLoc, _progName)
    return


    

def latexSourceToHTML_htlatex(sourceTex_Filepath, output_Directory, template_Path=None):
    '''
    Convert Latex Document to HTML 

    Parameters
    ----------
    sourceTex_Filepath : str
        F
    Returns
    -------
    Other Parameters
    ----------------
    Raises
    ------
    See Also
    --------
    Notes
    -----
    Bodge: because htlatex does not have a specified output directory,
        this program polls the files in the `sourceTex_Filepath`, runs
        `htlatex`, and polls the files in the same location again. 

        Then 
    References
    ----------
    Examples
    --------

    '''
    print(sourceTex_Filepath, output_Directory)
    assert(os.path.isdir(output_Directory))
    output_Directory = os.path.abspath(output_Directory)
    method = 1

    if method == 1:
        #htlatex
        if template_Path:
            assert(os.path.isfile(template_Path))




        src_path = os.path.abspath( os.getcwd())
        
        src_dir = os.path.abspath(os.getcwd())
        original_fls = kmlistfi.les(src_dir)

        _progLoc = ""
        _progName = "htlatex"
        _cmdPrefix = os.path.join(_progLoc, _progName)
        cmd = _cmdPrefix +' ' + sourceTex_Filepath
        if template_Path:
            cmd_tail = ' "' + template_Path + ' , charset=utf-8" " -cunihtf -utf8"'
            cmd+= cmd_tail
        logging.debug(cmd)
        _runCLargs(cmd)

        #time.sleep(0.03)
        built_fls = kmlistfi.les(src_dir)
        new_fls = [x for x in built_fls if x not in original_fls]
        #print("*"*30)
        for fl in new_fls:
            flName = fl.split(src_dir)[-1][1:]
            srcFile = fl
            dstFile = os.path.abspath(os.path.join(output_Directory, flName))
            logging.debug(srcFile + '->\n\t' + dstFile)
            shutil.move(srcFile, dstFile)

    elif method == 2:
        #latexml
        pass


        
    return len(kmlistfi.les(output_Directory))




def latexSourceToHTML_latexml(sourceTex_Filepath, output_Directory, template_Path=None):
    '''
    Convert Latex Document to HTML 

    Parameters
    ----------
    sourceTex_Filepath : str
        F
    Returns
    -------
    Other Parameters
    ----------------
    Raises
    ------
    See Also
    --------
    Notes
    -----
    Bodge: because htlatex does not have a specified output directory,
        this program polls the files in the `sourceTex_Filepath`, runs
        `htlatex`, and polls the files in the same location again. 

        Then 
    References
    ----------
    Examples
    --------

    '''
    print(sourceTex_Filepath, output_Directory)
    assert(os.path.isdir(output_Directory))
    output_Directory = os.path.abspath(output_Directory)
    method = 1

    if method == 1:
        #htlatex
        if template_Path:
            assert(os.path.isfile(template_Path))




        src_path = os.path.abspath( os.getcwd())
        
        src_dir = os.path.abspath(os.getcwd())
        original_fls = kmlistfi.les(src_dir)

        _progLoc = ""
        _progName = "latexml"
        _cmdPrefix = os.path.join(_progLoc, _progName)
        cmd = _cmdPrefix +' ' + sourceTex_Filepath
        if template_Path:
            cmd_tail = ' "' + template_Path + ' , charset=utf-8" " -cunihtf -utf8"'
            cmd+= cmd_tail
        logging.debug(cmd)
        _runCLargs(cmd)

        #time.sleep(0.03)
        built_fls = kmlistfi.les(src_dir)
        new_fls = [x for x in built_fls if x not in original_fls]
        #print("*"*30)
        for fl in new_fls:
            flName = fl.split(src_dir)[-1][1:]
            srcFile = fl
            dstFile = os.path.abspath(os.path.join(output_Directory, flName))
            logging.debug(srcFile + '->\n\t' + dstFile)
            shutil.move(srcFile, dstFile)
    return len(kmlistfi.les(output_Directory))

def run_arxiv_vanity_bodge(arxiv_url):
    '''
    This is the only section of the code that actually functions

    Which isn't the nicest thing in the world, but it's a baseline, 
    we can improve from here
    '''
    mobi_path = arxiv_vanity_bodge.main_arxiv_vanity_bodge(arxiv_url)
    sendToKindle(mobi_path)
    return


def sampleNumpyDefDocstring():
    """
    A one-line summary that does not use variable names or the
    function name.
    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.
    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    long_var_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.
    Returns
    -------
    type
        Explanation of anonymous return value of type ``type``.
    describe : type
        Explanation of return value named `describe`.
    out : type
        Explanation of `out`.
    Other Parameters
    ----------------
    only_seldom_used_keywords : type
        Explanation
    common_parameters_listed_above : type
        Explanation
    Raises
    ------
    BadException
        Because you shouldn't have done that.
    See Also
    --------
    otherfunc : relationship (optional)
    newfunc : Relationship (optional), which could be fairly long, in which
              case the line wraps here.
    thirdfunc, fourthfunc, fifthfunc
    Notes
    -----
    Notes about the implementation algorithm (if needed).
    This can have multiple paragraphs.
    You may include some math:
    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}
    And even use a greek symbol like :math:`omega` inline.
    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.
    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.
    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.
    >>> a = [1, 2, 3]
    >>> print [x + 3 for x in a]
    [4, 5, 6]
    >>> print "a\n\nb"
    a
    b
    """


    """
    Parameters
    ----------
    Returns
    -------
    Other Parameters
    ----------------
    Raises
    ------
    See Also
    --------
    Notes
    -----
    References
    ----------
    Examples
    --------
    """
    return



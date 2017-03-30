"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Author : James Arambam
Date   : 08 Feb 2017
Description :
Input : 
Output : 


How to use :

$python push.py "message"

or

$python push.py


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

# ================================ priImports ================================ #

import sys
import os
import platform
from pprint import pprint
import time

# ================================ secImports ================================ #

o = platform.system()
if o == "Linux":
    d = platform.dist()
    if d[0] == "debian":
        sys.path.append("/media/james/Storage/PyCharmProjects/auxLib")
    if d[0] == "centos":
        sys.path.append("/home/ajsingh/PycharmProjects/auxLib")
if o == "Darwin":
    sys.path.append("/Users/james/PycharmProjects/auxLib")

import auxLib as ax

print "# ============================ START ============================ #"

# ============================================================================ #

# --------------------- Variables ------------------------------ #

ppath = os.getcwd() + "/"  # Project Path Location


# -------------------------------------------------------------- #

def main():

    s = str(time.strftime("%d/%m/%Y"))
    tmp = s.split("/")
    tmp[2] = tmp[2][2:4]
    version = reduce(lambda v1, v2 : v1+""+v2, tmp)
    version = "v"+version
    try:
        msg = sys.argv[1]

    except:
        msg = ""
        os.system("cd "+ppath)
    os.system("cd "+ppath +" && "+"git add .")
    os.system("cd "+ppath +" && "+'git commit -m "'+version+' - '+msg+'"')
    os.system("cd "+ppath +" && "+'git push')


# =============================================================================== #

if __name__ == '__main__':
    main()
    print "# ============================  END  ============================ #"


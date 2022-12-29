#!/usr/bin/env python

################################################################################
#
#  File:
#        resume_generator.py
#
#  Author:
#        Anushya Balakrishnan <anushya816@gmail.com>
#
#  Description:
#        Creates a sample cover letter and resume in latex.
#
#  Copyright notice:
#        Copyright (C) 2022 Anushya Balakrishnan
#
#  Licence:
#
#        This file is free code: you can redistribute it and/or modify it under
#        the terms of the GNU Lesser General Public License version 2.1 as
#        published by the Free Software Foundation.
#
#        This package is distributed in the hope that it will be useful, but
#        WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#        Lesser General Public License for more details.
#
#        You should have received a copy of the GNU Lesser General Public
#        License along with the NetFPGA source package.  If not, see
#        http://www.gnu.org/licenses/.
#
#


import os, sys, getopt, getpass

class CoreGen(object):
    def __init__(self):
        self.name = "resume" 
        self.version = "_v1_00_a"
        self.path = "."
        self.userlogic = "user_logic"
        self.author = getpass.getuser()

    def getOpt(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], 
                                       "h", ["help", "name=", "path=",
                                            "author=","userlogic=", "begin="])
        except getopt.GetoptError:
            print (sys.argv[0] +": invalid option\nUsage:")
            self.showHelp()
            sys.exit(1)
        for opt,arg in opts:
            if opt in ("-h", "--help"):
                self.showHelp()
                sys.exit(0)
            elif opt == "--name":
                self.name = arg
            elif opt == "--path":
                self.path = arg
            elif opt == "--author":
                self.author = arg
            elif opt == "--userlogic":
                self.userlogic = arg
            elif opt == "--begin":
                self.begin = arg
        print("passed values:")
        print("self.name is : "+self.name) 
        print("self.version is : "+self.version)
        print("self.path is : "+self.path)
        print("self.author is : "+self.author)
        print("self.userlogic is : "+self.userlogic)

    def showHelp(self):
        print("resume_generator.py [--help --name <company name> --path <dest path> --author <author name> --userlogic <user_logic name>]")

    def createFileHeader(self,filename,desc="Some pcore file",fsuffix=".tex"):
        return  "################################################################################\n\
#\n\
#  File:\n\
#        " + filename + fsuffix + " \n\
#\n\
#  Author:\n\
#        " + self.author + "\n\
#\n\
#  Description:\n\
#        " + desc + "\n\
#\n\
#  Copyright notice:\n\
#        Copyright (C) 2022 Anushya Balakrishanan \n\
#\n\
#  Licence:\n\
#        This file is free code: you can redistribute it and/or modify it under\n\
#        the terms of the GNU Lesser General Public License version 2.1 as\n\
#        published by the Free Software Foundation.\n\
#\n\
#        This package is distributed in the hope that it will be useful, but\n\
#        WITHOUT ANY WARRANTY; without even the implied warranty of\n\
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU\n\
#        Lesser General Public License for more details.\n\
#\n\
#        You should have received a copy of the GNU Lesser General Public\n\
#        License along with the NetFPGA source package.  If not, see\n\
#        http://www.gnu.org/licenses/.\n\
#\n\
#\n\
"
    def createLatexHeader(self,filename,desc="Some pcore file",fsuffix=".tex"):
        return  "%###############################################################################\n\
%\n\
%\n\
%  File:\n\
%        " + filename + fsuffix + " \n\
%\n\
%  Author:\n\
%        " + self.author + "\n\
%\n\
%  Description:\n\
%        " + desc + "\n\
%\n\
%  Copyright notice:\n\
%        Copyright (C) 2022 Anushya Balakrishnan \n\
%\n\
%  Licence:\n\
%        This file is free code: you can redistribute it and/or modify it under\n\
%        the terms of the GNU Lesser General Public License version 2.1 as\n\
%        published by the Free Software Foundation.\n\
%\n\
%        This package is distributed in the hope that it will be useful, but\n\
%        WITHOUT ANY WARRANTY; without even the implied warranty of\n\
%        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU\n\
%        Lesser General Public License for more details.\n\
%\n\
%        You should have received a copy of the GNU Lesser General Public\n\
%        License along with the NetFPGA source package.  If not, see\n\
%        http://www.gnu.org/licenses/.\n\
%\n\
%\n\
"

    def makeDirectories(self):
        # Create Pcore directory
        self.fullCorePath = self.path + '/' + self.name + self.version
        if not os.path.exists(self.fullCorePath): 
            os.makedirs(self.fullCorePath)

        # Create data directory
        self.dataCorePath = self.fullCorePath + '/cover_letter'
        if not os.path.exists(self.dataCorePath): 
            os.makedirs(self.dataCorePath)

	# Create hdl/verilog path
        self.verilogCorePath = self.fullCorePath + '/resume'
        if not os.path.exists(self.verilogCorePath): 
            os.makedirs(self.verilogCorePath)

    def createCoverLetter(self):
        with open(self.dataCorePath + "/" + self.name + 
                  "_cover_letter.tex","w") as f:
            f.write(self.createLatexHeader(filename=self.name+"_cover_letter",
                                          desc=self.name+"'s  Cover letter File",
                                          fsuffix=".tex") +

"\documentclass{article} \n\
  \\begin {document}\n\
  %Hi World! \n\
  Hi !! This is " + self.author.upper() + "'s cover letter for " + self.name.upper() + " company. \n\
\end{document}\n\
")

    def createResumeLetter(self):
        with open(self.verilogCorePath + "/" + self.name + 
                  "_resume_letter.tex","w") as f:
            f.write(self.createLatexHeader(filename=self.name+"_resume_letter",
                                          desc=self.name+"'s  CV/Resume File",
                                          fsuffix=".tex") +

"\documentclass{article} \n\
  \\begin {document}\n\
  %Hi World! \n\
  Hi !! This is " + self.author.upper() + "'s CV/Resume for " + self.name.upper() + " company. \n\
\end{document}\n\
")


    def createPcore(self):
        self.makeDirectories()
        self.createCoverLetter()
        self.createResumeLetter()

def main():
    core = CoreGen()
    try:
        core.getOpt()
    except getopt.GetoptError:
        core.showHelp()
        sys.exit(1)
    print ("Pcore name: "+ core.name + "\n\
User Logic Name:" + core.userlogic + "\n\
Path:" + core.path + "\n\
Author:" + core.author)
    core.createPcore()

if __name__ == '__main__':
    main()


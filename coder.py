class Coder():
    def __init__(self, session):
        import logging
        logging.basicConfig(level=logging.INFO)
        logging.info("session: " + session + " starting")

        self.session = session
        self.userList = []
        self.fileList = []
        self.compiledList = []
        self.allOutputList = []
        self.succesOutputList = []

    def setParameters(self, path, userFileName, rootFileName,
                      userFileListSave, userListSave, compiledSave,
                      fileOutputName, allOutputSave, succesOutputSave):
        self.path = path
        self.userFileName = userFileName
        self.rootFileName = rootFileName
        self.userFileListSave = userFileListSave
        self.userListSave = userListSave
        self.compiledSave = compiledSave
        self.fileOutputName = fileOutputName
        self.allOutputSave = allOutputSave
        self.succesOutputSave = succesOutputSave

    def run(self):
        """ Code starting """
        import logging

        logging.info("user list creating")
        self.user_lister()
        logging.info("user list created")

        logging.info("user file list creating")
        self.file_lister()
        logging.info("user file list created")

        logging.info("codes compiling")
        self.code_compiler()
        logging.info("all codes compiled")

        logging.info("output files checking")
        self.code_control()
        logging.info("all output files checked")

    def user_lister(self):
        """ List directories in path """
        import os, logging
        logging.info("walking directories in " + self.path)

        for dirname, dirnames, filenames in os.walk(self.path):
            for subdirname in dirnames:
                self.userList.append(os.path.join(self.path, subdirname))

        self.save_file(self.userList, self.userFileListSave)

    def file_lister(self):
        """ List files which name equal fileName"""
        import os
        for user in self.userList:
            for dirname, dirnames, filenames in os.walk(user):
                for filename in filenames:
                    if(self.userFileName == filename):
                        self.fileList.append(os.path.join(user, filename))

        self.save_file(self.fileList, self.userFileListSave)

    def code_compiler(self):
        """ Compile c source codes in fileList """
        import logging, commands
        for fileName in self.fileList:
            compiledName =  str(fileName).rstrip(".c")
            compile_error = commands.getstatusoutput("gcc " + fileName +
                                                     " -o " + compiledName)
            if(compile_error[0]):
                logging.info("compile error: " + fileName)
                logging.info(compile_error[1])
            else:
                logging.info("succesfully compile: " + fileName)
                self.compiledList.append(compiledName)
                runner_error = commands.getoutput(compiledName)
                logging.info("runned file output: " + runner_error)

        self.save_file(self.compiledList, self.compiledSave)

    def code_control(self):
        """ Control diff rootFileName with outputList """
        import logging, os
        for user in self.userList:
            userFile = os.path.join(user, self.fileOutputName)
            self.allOutputList.append(userFile)
            if self.is_same(userFile, self.rootFileName):
                self.succesOutputList.append(userFile)

        self.save_file(self.allOutputList, self.allOutputSave)
        self.save_file(self.succesOutputList, self.succesOutputSave)

    def save_file(self, fileList, fileName):
        """ Save fileList as fileName in json """
        import json, logging
        with open(fileName,'wb') as fp:
            logging.info("file saving as " + fileName)
            json.dump(fileList, fp, indent=2)

    def is_same(self, user_file, target_file):
        import filecmp, logging
        try:
            return filecmp.cmp(user_file, target_file)
        except:
            logging.warning("output file error: " + user_file)
            logging.info("passing")

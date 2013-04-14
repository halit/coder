class Coder():
    def __init__(self, session):
        import logging
        logging.basicConfig(level=logging.INFO)
        logging.info("session: " + session + " starting")

        self.session = session
        self.userList = []
        self.fileList = []
        self.compiledList = []

    def setParameters(self, path, userFileName, rootFileName,
                      userFileListSave, userListSave, compiledSave):
        self.path = path
        self.userFileName = userFileName
        self.rootFileName = rootFileName
        self.userFileListSave = userFileListSave
        self.userListSave = userListSave
        self.compiledSave = compiledSave

    def run(self):
        """ Code starting """
        import logging

        logging.info("user list creating")
        self.user_lister(self.path, self.userListSave)
        logging.info("user list created")

        logging.info("user file list creating")
        self.file_lister(self.userFileListSave)
        logging.info("user file list created")

        logging.info("codes compiling")
        self.code_compiler()
        logging.info("all codes compiled")

    def user_lister(self, path, fileName):
        """ List directories in path """
        import os, logging
        logging.info("walking directories in " + path)

        for dirname, dirnames, filenames in os.walk(path):
            for subdirname in dirnames:
                self.userList.append(os.path.join(path, subdirname))

        self.save_file(self.userList, fileName)

    def file_lister(self, fileName):
        """ List files which name equal fileName"""
        import os
        for user in self.userList:
            for dirname, dirnames, filenames in os.walk(user):
                for filename in filenames:
                    if(self.userFileName == filename):
                        self.fileList.append(os.path.join(user, filename))

        self.save_file(self.fileList, fileName)

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

    def code_control(self, rootFileName, outputList):
        """ Control diff rootFileName with outputList """
        pass
    def save_file(self, fileList, fileName):
        """ Save fileList as fileName in json """
        import json, logging
        with open(fileName,'wb') as fp:
            logging.info("file saving as " + fileName)
            json.dump(fileList, fp, indent=2)
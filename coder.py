class Coder():
    def __init__(self, path, userFileName, rootFileName):
        import logging
        logging.basicConfig(level=logging.INFO)

        self.path = path
        self.userFileName = userFileName
        self.rootFileName = rootFileName
        self.userList = []
        self.fileList = []
        self.userFileListSave = "/home/halit/coder/test/userFileList.json"
        self.userListSave = "/home/halit/coder/test/userList.json"

    def run(self):
        import logging

        logging.info("user list creating")
        self.user_lister(self.path, self.userListSave)

        logging.info("user file list creating")
        self.file_lister(self.userListSave, self.userFileListSave)

    def user_lister(self, path, fileName):
        """ List directories in path """
        import os, logging
        logging.info("walking directories in " + path)

        for dirname, dirnames, filenames in os.walk(path):
            for subdirname in dirnames:
                self.userList.append(os.path.join(path, subdirname))

        self.save_file(self.userList, fileName)

    def file_lister(self, userList, fileName):
        """ List files which name equal fileName"""
        import json, os
        with open(userList, 'rb') as fp:
            user_list = json.load(fp)

        for user in user_list:
            for dirname, dirnames, filenames in os.walk(user):
                for filename in filenames:
                    if(self.userFileName == filename):
                        self.fileList.append(os.path.join(user, filename))

        self.save_file(self.fileList, fileName)

    def code_compiler(self, fileList):
        """ Compile c source codes in fileList """
        pass
    def code_control(self, rootFileName, outputList):
        """ Control diff rootFileName with outputList """
        pass
    def save_file(self, fileList, fileName):
        """ Save fileList as fileName in json """
        import json, logging
        with open(fileName,'wb') as fp:
            logging.info("file saving as " + fileName)
            json.dump(fileList, fp, indent=2)
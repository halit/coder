import coder

if __name__ == "__main__":

    path             = "/home/halit/coder/test"
    userFileName     = "matris.c"
    rootFileName     = "/home/halit/output.txt"
    userFileListSave = "/home/halit/coder/test/userFileList.json"
    userListSave     = "/home/halit/coder/test/userList.json"

    coder = coder.Coder("1")
    coder.setParameters(path=path, userFileName=userFileName, rootFileName=rootFileName)
    coder.setParameters(userFileListSave=userFileListSave, userListSave=userListSave)
    coder.run()
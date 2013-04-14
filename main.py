import coder, time, os

if "__main__" == __name__:

    path = "/home/halit/coder/test"
    userFileName = "matris.c"
    rootFileName = "/home/halit/output.txt"

    session = str(time.time()).split(".")[0] + str(time.time()).split(".")[1]
    sessionDir = os.path.join(os.path.join(path,"sessions"), session)

    try:
        os.mkdir(os.path.join(path,"sessions"))
    except:
        pass

    os.mkdir(sessionDir)
    userFileListSave = os.path.join(sessionDir, "userFileList.json")
    userListSave = os.path.join(sessionDir, "userList.json")
    compiledSave = os.path.join(sessionDir, "compiled.json")

    coder = coder.Coder(session)
    coder.setParameters(path=path, userFileName=userFileName, rootFileName=rootFileName,
                        userFileListSave=userFileListSave, userListSave=userListSave,
                        compiledSave=compiledSave)
    coder.run()
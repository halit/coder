import coder, time, os

if "__main__" == __name__:

    path = "/home/halit/coder/test"
    sessions = "/home/halit/coder"
    userFileName = "matris.c"
    rootFileName = "/home/halit/coder/output.txt"
    fileOutputName = "output.txt"

    session = str(time.time()).split(".")[0] + str(time.time()).split(".")[1]
    sessionDir = os.path.join(os.path.join(sessions, "sessions"), session)

    try:
        os.mkdir(os.path.join(sessions,"sessions"))
    except:
        pass

    os.mkdir(sessionDir)
    userFileListSave = os.path.join(sessionDir, "userFileList.json")
    userListSave = os.path.join(sessionDir, "userList.json")
    compiledSave = os.path.join(sessionDir, "compiled.json")
    allOutputSave = os.path.join(sessionDir, "allOutput.json")
    succesOutputSave = os.path.join(sessionDir, "succesOutput.json")

    coder = coder.Coder(session)
    coder.setParameters(path=path, userFileName=userFileName, rootFileName=rootFileName,
                        userFileListSave=userFileListSave, userListSave=userListSave,
                        compiledSave=compiledSave, fileOutputName=fileOutputName,
                        allOutputSave=allOutputSave, succesOutputSave=succesOutputSave)

    coder.run()
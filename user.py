if "__main__" == __name__:
    import parsefile
    functionFile = "test.c"
    endOf = "#end#"

    opener = parsefile.Opener(functionFile)
    parser = parsefile.Parser(opener.open(),endOf)
    list = parser.run()

    print list[1]


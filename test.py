import parsefile

string = """

int foo(int x, int y){
    int sum;
    sum = x+y;
    return sum;
}
#end#

void bar(){
    printf("foobar");
}
#end#
"""

parser = parsefile.Parser(string,"#end#")
list = parser.run()

print list[0]
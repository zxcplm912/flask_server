from flask_script import Manager,Command,Option
from test_col_diamon import app
manager=Manager(app)

class World(Command):
    'print World lala string'
    option_list=(
        Option('--name','-n',dest='hearttalk',default='see next century'),
    )
    def run(self,hearttalk):
        print 'world lala %s'%hearttalk

@manager.command
def hello(truth='sss'):
    'print hello jj string'
    print "hello jj %s"%truth

@manager.option('-n','--name',help='your namx',default='xiaoming')
#@manager.option('-a','--age',help='your age',default=18)
@manager.option('-a','--age',help='your age')
def printname(name,age):
    'print nihao <name> [age]'
    if age is None:
        print "nihao",name
    else:
        print "nihao %s age is %d"%(name,int(age))

@manager.command
def printbool(booler=False):
    'print nihao xxx'
    print "nihao",'yes' if booler else 'no'
if __name__ == "__main__":
    #manager.add_command('world2',World())
    manager.run({'world2':World()})

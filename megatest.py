from MEGA import *
main = mega2('test')
ffile = ['File_Fake',['test','lines','three','exist?']]
main.adddata(ffile)
print(main.peek())

#!/usr/bin/python
from Tkinter import *
import tkFont
import subprocess as sub
import sys

cmd=[]
verbose=False
def changeverbose():
    global verbose
    verbose=not verbose
    if not lastcmd[0]=='/usr/bin/strings':
        newtext(lastcmd,verbose)
def newtext(cmd,verbose):
    global lastcmd
    lastcmd=cmd[:]
    cmd2=cmd[:]
    if verbose:
        cmd2.insert(1,'-v')
    p = sub.Popen(cmd2,stdout=sub.PIPE,stderr=sub.PIPE)
    output, errors = p.communicate()
    text['state']=NORMAL
    text.delete(1.0,END)
    text.insert(END, output)
    text['state']=DISABLED
    root.title(cmd2)

cmd+=sys.argv[1:]
cmdbase=cmd[1:]
if len(cmdbase)>1 and cmdbase[1]=='-v':
    cmdbase=cmdbase[1:]
    verbose=True
cmdhd=['/usr/bin/hd']+cmdbase
cmdstrings=['/usr/bin/strings']+cmdbase
cmdstringsel=['/usr/bin/strings','-el']+cmdbase
cmdcat=['/bin/cat']+cmdbase

root = Tk()
root.geometry('1224x968+200+50')
text = Text(root)
font = tkFont.Font(font='mono',size=10)
font['size']=10
yscrollbar=Scrollbar(root, orient=VERTICAL, command=text.yview)
text.configure(
    background='black',
    foreground='orange2',
    font=font,
    wrap='none',
    yscrollcommand=yscrollbar.set,
    )
text.pack(side=LEFT, fill=BOTH, expand = YES)
yscrollbar.pack(side=RIGHT, fill=Y)
newtext(cmd,verbose)
root.bind('<Escape>',lambda y: sys.exit(0))
root.bind('q',lambda y: sys.exit(0))
root.bind('Q',lambda y: sys.exit(0))
root.bind('<Next>',  lambda y:text.yview_scroll(1,'pages'))
root.bind('<Prior>', lambda y:text.yview_scroll(-1,'pages'))
root.bind('<Up>',    lambda y:text.yview_scroll(-1,'units'))
root.bind('<Down>',  lambda y:text.yview_scroll(1,'units'))
root.bind('<Left>',  lambda y:text.xview_scroll(-1,'pages'))
root.bind('<Right>', lambda y:text.xview_scroll(1,'pages'))
root.bind('w', lambda y: 
          text.configure(wrap=['char','none'][(text['wrap']=='char')]))
root.bind('s',lambda y: newtext(cmdstrings,False))
root.bind('S',lambda y: newtext(cmdstringsel,False))
root.bind('h',lambda y: newtext(cmdhd,verbose))
root.bind('c',lambda y: newtext(cmdcat,verbose))
root.bind('v',lambda y: changeverbose())
root.mainloop()

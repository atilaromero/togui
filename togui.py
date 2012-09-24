#!/usr/bin/python
from Tkinter import *
import tkFont
import subprocess as sub
import sys

cmd=[]
cmd+=sys.argv[1:]
p = sub.Popen(cmd,stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()

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
yscrollbar.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT, fill=BOTH, expand = YES)
text.insert(END, output)
text['state']=DISABLED
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
root.mainloop()

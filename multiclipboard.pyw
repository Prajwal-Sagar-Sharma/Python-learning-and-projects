import shelve,pyperclip,sys
import pprint
mcb=shelve.open('mcb')
# to do : save clipboard content
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcb[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcb.keys())))
    elif sys.argv[1] in mcb:
        pyperclip.copy(mcb[sys.argv[1]])
        

# list keyboard and load content

mcb.close()

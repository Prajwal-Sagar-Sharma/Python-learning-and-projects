import send2trash
testfile=open('test.txt','a')
testfile.write('\nhi')
testfile.close()
send2trash.send2trash('test.txt')
# this help you to send the deleted file to recycle bin 
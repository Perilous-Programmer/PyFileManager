import os
import cgi
form = cgi.FieldStorage()
filee = ''
try:
    filee=form['file'].value
except:
    pass
try:
    path=form['path'].value+'/'
except:
    path = '/'
#
#
#

#
#
#
if ('.' in filee):
    # HTTP Header
    print 'Content-Type:application/octet-stream;'
    print 'Content-Disposition: attachment; filename="'+filee+'";'
    print
    # file open
    fo = open(path+filee, "rb")
    print fo.read()
    # Close opend file
    fo.close()

else:
    print "Content-Type: text/html"
    print
    print '<p>Current Drive:'+path+'<br /><a href="index.py?path=c:" >C:</a><br /><a href="index.py?path=d:" >D:</a><br /></p><p>'
    for x in os.listdir(path):
        if ('.' not in x):
            print '<a href="index.py?path='+path+x+'" >'+x+'</a><br />'
        else:
            print '<a href="index.py?path='+path+'&file='+x+'" >'+x+'</a><br />'
    print '</p>'
#if ('.py' not in x):
 #       print '<a href="'+x+'" >'+x+'</a><br />'

import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre/sdf')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print "HTTPError",e.reason
except urllib2.URLError, e:
    print e.reason
    print "URLError",e.reason
else:
    print "OK"
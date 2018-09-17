# execute this on python2.7

a_billion = 1000000000
a_million = 1000000
for i in xrange(a_million):
    a = a + 1e-6

print(a - a_billion)
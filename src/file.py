import io, sys, re

filename = "test"
f = open(filename, 'r+')
text = f.read()
text = re.sub('foobar', 'bar', text)
f.seek(0)
f.write(text)
f.truncate()
f.close()

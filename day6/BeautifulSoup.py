#coding=utf-8
from urllib import urlopen
#from BeautifulSoup import BeautifulSoup

text = urlopen('heep://python.org/community/jobs').read()
soup = BeautifulSoup(text)

jobs = set()
for header in soup('h3'):
    links = header('a','reference')
    if not links:
        continue
    link = links[0]
    job.add('%s (%s)' % (link.string, link['href']))

print '/n'.join(sorted(jobs,key=lamba s: s.lower()))

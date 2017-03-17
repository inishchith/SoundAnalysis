import os
import urllib
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import pypandoc

request = urllib.request.urlopen('https://github.com/adambard/learnxinyminutes-docs')

soup = BeautifulSoup(request,'html.parser')

downloads= os.path.dirname(os.path.abspath(__file__))+'/downloads'


for link in soup.findAll('a'):
    filename = link['href']
    filepath = os.path.join(downloads,'hi3.html')
    if not os.path.isfile(filepath):
        url = 'https://github.com' + filename
        path =urllib.parse.urlparse(url).path
        ext = os.path.splitext(path)[1]
        if ext in ['.markdown']:
            file = urllib.request.urlopen(url)
            print(url)
            out = open(os.path.join(filepath),'wb')
            out.write(file.read())
            out.close()

            print('Downloaded: ' +filename )

    else:
        print(filename+' already exists ')

out = pypandoc.convert_file('downloads/hi3.html', 'docx', outputfile='done.docx')
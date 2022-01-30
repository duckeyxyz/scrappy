import urllib.request, urllib.error, urllib.parse
import requests, os
from bs4 import BeautifulSoup

###### IMPORT MODULE ######

# Search the html file
inp_search_query = input("Please enter your search query: ")
answer = inp_search_query.replace(" ", "+")
userinput_url=('https://html.duckduckgo.com/html?q=' + answer )
print("Searching..")
response = urllib.request.urlopen(userinput_url)
webcontent = response.read().decode('UTF-8')

# Write html file
temp_html = open('/tmp/tmp.html','w')
temp_html.write(webcontent)
temp_html.close

# Parse the html file
soup = BeautifulSoup(open('/tmp/tmp.html'), 'html.parser')
els = soup.find(class_='result__url',text=True)

def remove(string):
    return "".join(string.split())
curl_link = remove(els.string)

# Download the html file
print('Download "https://' + curl_link + '" HTML file')
result_file = str(input("Save as (non-HTML file would not work perfectly) : "))
print('Downloading...')
    
try:
    os.system('curl -so ' + result_file + ' https://' + curl_link )
    pass
except(KeyboardInterrupt):
    print("Ctrl+c was pressed.. interrupt while loop.")

print('Finished')

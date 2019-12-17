# import libraries
import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv
import urllib

# connect to website and get list of all pdfs
url="http://www.urso.gov.sk:8088/CISRES/Agenda.nsf/formWebRozhodnutiaValid?OpenForm&Category=E-OZ-OK"
response = urllib.request.urlopen(url).read()
soup= BeautifulSoup(response, "html.parser")     
links = soup.find_all('a')

# save url to csv file
f = csv.writer(open(r"C:\Users\DELL\Documents\Work\urls_oze.csv", "w"))
f.writerow(["Url"]) # Write column headers as the first line

for link in links:
    print(link.get('href'))
    
f.writerows(link) 


# download all pdf files to local folder
DOWNLOADS_DIR = r"C:/Users/DELL/Documents/Work/python-downloader/"

# For every line in the file
for url in open(r'C:/Users/DELL/Documents/Work/url_test.txt'):
    # Split on the rightmost / and take everything on the right side of that
    name = url.rsplit('/', -1)[-1]

    # Combine the name and the downloads directory to get the local filename
    filename = os.path.join(DOWNLOADS_DIR, name).replace('\n', '')

    # Download the file if it does not exist
    if not os.path.isfile(filename):
        urllib.request.urlretrieve(url, filename)

# part for extracting information from the pdf files
import os
import glob
import fitz
import pandas as pd
import re

path = r'C:\Users\DELL\Documents\Work\python-downloader'
files = [f for f in glob.glob(path + "**/*.pdf", recursive=False)]
# print(files)
# create dictionaries for dataframe
subory = []
CR = []
Producer = []
CIV = []
Start_date = []
End_date = []
Price = []


for file in files:
#     print(file)
    subory.append(file)
    doc = fitz.open(file)
    page_count = doc.pageCount
    page = 0
    text = ''
#     print(page_count)
    while (page < page_count):
        p = doc.loadPage(page)
        page += 1
        text = text + p.getText()
        
              
    matches = re.findall(r'Číslo:.*', text)
    if len(matches) == 0:
        CR.append("N/A")
    else:
        CR.append(matches[0])
    
    matches = re.findall(r'\d+\,?\d+\s(?:MW|kWp|kW)', text)
    if len(matches) == 0:
        CIV.append("N/A")
    else:
        CIV.append(matches[0])
        
    matches = re.findall(r'(subjekt)(.*?\n.*)', text)
    # add next line if the match word is at the end of line
    for line in file:
        if line.endswith('subjekt'):
            print(next(line))
#     result = matches[0] if len(matches) > 0 else ""
    if len(matches) == 0:
        Producer.append("N/A")
    else:
        Producer.append(matches[0])
    
    matches = re.findall(r'prevádzky dňa .*', text)
    if len(matches) == 0:
        Start_date.append("N/A")
    else:
        Start_date.append(matches[0])
    
    matches = re.findall(r'skončí dňa .*', text)
    if len(matches) == 0:
        matches = re.findall(r'do .*', text)
        End_date.append(matches[0])
        if len(matches) == 0:
            End_date.append("N/A")
    else:
        End_date.append(matches[0])
    
    matches = re.findall(r'(\d+\,\d+\s)eura/MWh', text)
    result = matches[0] if len(matches) > 0 else ""
    if len(result) == 0:
        Price.append('N/A')
    else:
        Price.append(result[:-1])
          
    doc.close() # close the opened document

print(len(subory), len(Producer), len(CIV), len(Start_date), len(End_date), len(Price)) # check if the array is saame length
    
df = pd.DataFrame({'file': subory, 'CR': CR, 'Subject': Producer, 'CIV': CIV, 'Start_date': Start_date, 'End_date': End_date, 'Price': Price})
df.to_csv('export.csv')

# cealing from unwnated words and export to excel table
df.replace({'CR': r'^(Číslo:)'}, {'CR': ''}, inplace=True, regex=True)
df.replace({'Subject': r'^(subjekt)'}, {'Subject': ''}, inplace=True, regex=True)
df.replace({'Start_date': r'^(prevádzky dňa)'}, {'Start_date': ''}, inplace=True, regex=True)
df.replace({'Start_date': r'(.)$'}, {'Start_date': ''}, inplace=True, regex=True)
df.replace({'End_date': r'^(skončí dňa)'}, {'End_date': ''}, inplace=True, regex=True)
df.replace({'End_date': r'^(do)'}, {'End_date': ''}, inplace=True, regex=True)
df.replace({'End_date': r'(pevnú.*$)'}, {'End_date': ''}, inplace=True, regex=True)
df.replace({'Price': r'^(doplatku vo výške)'}, {'Price': ''}, inplace=True, regex=True)
df
df.to_csv('export2.csv', encoding="cp1250")
import os

import PyPDF2
from tika import parser


pdf_dir = 'resources'


# With PyPDF2
for pdf_filename in os.listdir(pdf_dir):
    pdf_file = open((os.path.join(pdf_dir, pdf_filename)), 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    page = pdf_reader.getPage(0)
    print(page.extractText())


# With tika
# For this to work you need java and the tike-server.jar file
# Download it from https://www.apache.org/dyn/closer.cgi/tika/tika-server-1.23.jar
# run it with java -jar tika-server.jar
# you also need this env in your environment TIKA_SERVER_JAR="file:////tika-server.jar"
# you can do it with `export TIKA_SERVER_JAR="file:////tika-server.jar"`
for pdf_filename in os.listdir(pdf_dir):
    print("*** Parsing {} ***".format(pdf_filename))
    raw_text = parser.from_file(os.path.join(pdf_dir, pdf_filename))
    raw_list = raw_text['content'].splitlines()
    all_text = ' '.join(text for text in raw_list if text)
    all_text = ' '.join(all_text.split())
    print(all_text)

#Import libraries
import urllib.request
import re,sys,zipfile
import schedule
import time

# def job():
#Getting GDELT Event url content into a format that can be manipulated
url = 'http://data.gdeltproject.org/events/index.html'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
#Pattern match text so that it returns string between "" as is the case for links
def doit(text):
  matches=re.search(r'\"(.+?)\"',text).group(0)
  return matches
#Get the href tag for the current day
global curr_file # global variable to be used in dlProgress
curr_file = doit(text.split()[17]).strip("\"")
#Append filename to the events url. From this, we'll be able to download our file.
fin_url = ( "http://data.gdeltproject.org/events/" + curr_file)
#Function to display progress percentage of download
def dlProgress(count, blockSize, totalSize):
  percent = int(count*blockSize*100/totalSize)
  sys.stdout.write("\r" + curr_file + "...%d%%" % percent + "\n")
  sys.stdout.flush()
#Download today's file
urllib.request.urlretrieve(fin_url, curr_file,reporthook=dlProgress)
#Extracting the zip file into csv
zip = zipfile.ZipFile(curr_file)
zip.extractall()

# schedule.every(5).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
#
# while 1:
#     schedule.run_pending()
#
#     time.sleep(1)

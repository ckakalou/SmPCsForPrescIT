# Created by Christine Kakalou on 3/1/2023
# Project: SmPCs for PrescIT
#
import re
import sys
from urllib.request import urlopen

import wget as wget
import pandas as pd
import urllib
import regex as re

path = r"Data\SmPCs\EMA"
urlsDF = pd.read_csv(r'Data/SmPCs/joinedHumanAuthorisedProductURLsONLY.csv')
urlsDF.dropna(inplace = True)
urls = urlsDF['URL(currentwebsite)'].tolist()

#OLD REGEX using ema url regex
#filenameRegex = '(?<=(https:\/\/www.ema.europa.eu\/en\/documents\/product-information\/)|(?<=(https:\/\/www.ema.europa.eu\/documents\/product-information\/))).*'

filenameRegex = '(?<=\/)[\w\-\_]+\.pdf'

urlsDF.to_csv("nonNANURLS.csv")

def check_validity(my_url):
    try:
        urlopen(my_url)
        # print("Valid URL")
        validURL = True
    except IOError:
        print("Invalid URL")
        print("Invalid URL is: ", my_url)
        sys.exit()
    return(validURL)

len(urls)
urlCounter = 0
for url in urls:
    validURLCheck = check_validity(url)
    urlCounter = urlCounter + 1
    if validURLCheck:
        filename = re.search(filenameRegex, url)[0]
        print(filename)
        localFile = path + "\\" + filename
        wget.download(url, localFile)
    # print("URL is valid")
    print("Downloaded ", urlCounter, "of ", str(len(urls)))

print("Done")
# wget.download("https://www.ema.europa.eu/en/documents/product-information/kengrexal-epar-product-information_en.pdf")



#import urllib.request
#urllib.request.urlretrieve("https://www.ema.europa.eu/en/documents/product-information/kengrexal-epar-product-information_en.pdf", r"C:\Users\ckakalou\PycharmProjects\Healie\Data\SmPCs\EMA\kengrexal-epar-product-information_en.pdf")

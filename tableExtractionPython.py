# Created by Christine Kakalou on 7/12/2022
# Project: SmPCs for PrescIT
#
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import camelot
import re
import PyPDF2
import json
import os as os
from os import listdir
from os.path import isfile, join



with open(r"Data\MedDRA\SystemOrganClass.json", 'r') as f:
    SOCList = json.load(f)


SOCListRegex = '(?:% s)' % '|'.join(SOCList)


def pageSpanSectionDetection(filepath):
    object = PyPDF2.PdfFileReader(filepath)
    NumPages = object.getNumPages()
    String = r"Tabulated (list|summary) of adverse reactions"
    Pagelist = []
    PagelistSoC = []
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ReSearch = re.search(String, Text)
        if ReSearch != None:
            Pagelist.append(i+1)
            # print("Tabulated found")
            # print(Pagelist)
        ReSoCSearch = re.search(SOCListRegex, Text)
        if ReSoCSearch != None:
            PagelistSoC.append(i+1)
            # print("SoC found")
        if len(PagelistSoC) > 1 :
            if PagelistSoC[-1] - PagelistSoC[-2] > 1:
                PagelistSoC.pop()
                break
            else:
                break
    # print(Pagelist)
    # print(PagelistSoC)
    return PagelistSoC



def tableExtraction(filepath):
    pageList = pageSpanSectionDetection(filepath)
    stringPageRange = ",".join(map(str, pageList))
    if stringPageRange!="":
        tables = camelot.read_pdf(filepath, pages = stringPageRange, line_scale=80, shift_text = ['', 'l'],process_background=False)
        return(tables)
    else:
        return


eparEMAdirectory = os.fsencode(r"Data\SmPCs\EMA")

for file in os.listdir(eparEMAdirectory):
     filename = os.fsdecode(file)
     filenameFull = r"Data\SmPCs\EMA" + "\\" + str(filename)
     print("Initiating table export for: ", filename)
     tablesTest = tableExtraction(filenameFull)
     medicationNameFull = filenameFull.split("EMA\\")
     medicationName = medicationNameFull[1].split("-epar-product-information")[0]
     exportPath = r"Data\SmPCs\EMA_ExtractedFiles" + "\\" + medicationName + "\\" + medicationName + ".xlsx"
     if not os.path.isdir(r"Data\SmPCs\EMA_ExtractedFiles" + "\\" + medicationName + "\\"):
         os.mkdir(r"Data\SmPCs\EMA_ExtractedFiles" + "\\" + medicationName + "\\")
     if tablesTest!= None:
         if tablesTest.n > 0 :
            tablesTest.export(exportPath, f='excel')
            print(medicationName, " tables exported")



print("All Done!!")
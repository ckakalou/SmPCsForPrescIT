# Created by Christine Kakalou on 12/12/2022
# Project: SmPCs for PrescIT
#

import PyPDF2
import re

object=PyPDF2.PdfFileReader(r'Data\SmPCs\ultomiris-epar-product-information_en.pdf')
NumPages = object.getNumPages()
String = 'Fertility, pregnancy and lactation'
for i in range(0,NumPages):
  PageObj=object.getPage(i)
  Text = PageObj.extractText()
  ReSearch = re.search(String,Text)
  Pagelist=[]
  if ReSearch != None:
     Pagelist.append(i)
     print(Pagelist)
# Created by Christine Kakalou on 20/10/2022
# Project: SmPCs for PrescIT
#
import textile
import pandas as pd
import json
import platform

import yaml
from bs4 import BeautifulSoup
from yaml import CLoader as Loader

SmPCsPath = "Data/SmPCs/"
MedDRAPath = "Data/MedDRA"

text_file = open(SmPCsPath+'ULTOMIRIS.txt', encoding="utf-8")
textileText = text_file.read()
#print("textileText is: ", textileText)

htmlText = textile.textile(textileText)
print("htmlText is: ", htmlText)


tablesPandas = pd.read_html(htmlText)
socFile = open(MedDRAPath+"SystemOrganClass.json")
socTermsArray = json.load(socFile)

with open(MedDRAPath+"frequencyConvention.json", encoding='utf-8') as fh:
    freqDict = json.load(fh)

smpcTableVeryCommon = tablesPandas[0].iloc[:,[0,1]]
smpcTableCommon = tablesPandas[0].iloc[:,[0,2]]
smpcTableUncommon = tablesPandas[0].iloc[:,[0,3]]
splitTableVeryCommon = smpcTableVeryCommon.join(smpcTableVeryCommon[1].str.split(',', 10, expand=True).rename(columns={0:'ADE1', 1:'ADE2', 2:'ADE3', 3: 'ADE4', 4: 'ADE5'}))
splitTableCommon = smpcTableCommon.join(smpcTableCommon[2].str.split(',', 10, expand=True).rename(columns={0:'ADE1', 1:'ADE2', 2:'ADE3', 3: 'ADE4', 4: 'ADE5'}))
splitTableUncommon = smpcTableUncommon.join(smpcTableUncommon[3].str.split(',', 10, expand=True).rename(columns={0:'ADE1', 1:'ADE2', 2:'ADE3', 3: 'ADE4', 4: 'ADE5'}))

print("Done")
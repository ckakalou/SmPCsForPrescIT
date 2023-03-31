# Created by Christine Kakalou on 4/1/2023
# Project: SmPCs for PrescIT
import yaml
from yaml.loader import SafeLoader
import sqlite3
import pandas as pd
import platform
import json

SmPCsPath = "Data/SmPCs/"
MedDRAPath = "Data/MedDRA"

conn = sqlite3.connect(SmPCsPath+'SmPCs.db')
smpcFromDB = pd.read_sql("""SELECT excerptText, citationId FROM smpcs WHERE citationSource='eu-ema' AND citationYear>2015""", conn)

text_file = smpcFromDB.loc[0, 'excerptText']
textileText = text_file.read()
print("textileText is: ", textileText)

htmlText = textile.textile(textileText)
# print("htmlText is: ", htmlText)


tablesPandas = pd.read_html(htmlText)
socFile = open(MedDRAPath+"SystemOrganClass.json")
socTermsArray = json.load(socFile)

with open(MedDRAPath+"frequencyConvention.json", encoding='utf-8') as fh:
    freqDict = json.load(fh)


print("Done")

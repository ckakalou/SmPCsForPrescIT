# Created by Christine Kakalou on 31/10/2022
# Project: SmPCs for PrescIT
#
import yaml
from yaml.loader import SafeLoader
import sqlite3
import pandas as pd
import platform

from yaml import CLoader as Loader

SmPCsPath = "Data/SmPCs/"
MedDRAPath = "Data/MedDRA"

conn = sqlite3.connect(SmPCsPath+'SmPCs.db')

smpcsData = pd.read_csv(SmPCsPath+'dataset.csv')
smpcsData.to_sql('smpcs', conn, if_exists='append', index=False)


medicinesOutputData = pd.read_csv(SmPCsPath+'Medicines_output_european_public_assessment_reports.csv')
medicinesOutputData.to_sql('emaMedicinesOP', conn, if_exists='replace', index=False)

productInformationURLs = pd.read_csv(SmPCsPath+'product-information-urls-member-states_en.csv')
productInformationURLs.to_sql('emaProductInformationURLs', conn, if_exists='append', index=False)


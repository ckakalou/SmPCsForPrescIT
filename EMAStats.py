# Created by Christine Kakalou on 24/2/2023
# Project: SmPCs for PrescIT
#

import numpy as np
import pandas as pd
import sqlite3



SmPCsPath = "Data/SmPCs/"
MedDRAPath = "Data/MedDRA"

conn = sqlite3.connect(SmPCsPath + 'SmPCs.db')

# Select all human medicines that are authorised and have a URL
joinedHumanAuthorisedProductURLs = pd.read_sql("""SELECT [Product number], [Medicine name], ProductName, [ATC code] , [URL(currentwebsite)], [International non-proprietary name (INN) / common name], [Condition / Indication]
FROM emaMedicinesOP
LEFT JOIN emaProductInformationURLs ON emaMedicinesOP.[Medicine name]=emaProductInformationURLs.[ProductName]
WHERE  emaMedicinesOP.Category='Human' AND emaMedicinesOP.[Authorisation Status] ='Authorised';""", conn)

# joinedHumanAuthorisedProductURLs.to_csv("joinedHumanAuthorisedProductURLs.csv")

# Select only the URL column
joinedHumanAuthorisedProductURLsONLY = pd.read_sql("""SELECT [URL(currentwebsite)]
FROM emaMedicinesOP
LEFT JOIN emaProductInformationURLs ON emaMedicinesOP.[Medicine name]=emaProductInformationURLs.[ProductName]
WHERE  emaMedicinesOP.Category='Human' AND emaMedicinesOP.[Authorisation Status] ='Authorised';""", conn)

joinedHumanAuthorisedProductURLsONLY.to_csv("joinedHumanAuthorisedProductURLsONLY.csv")

print("EMA Stats exported to CSV")
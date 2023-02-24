# Created by Christine Kakalou on 24/2/2023
# Project: SmPCs for PrescIT
#

import numpy as np
import pandas as pd
import sqlite3



SmPCsPath = "Data/SmPCs/"
MedDRAPath = "Data/MedDRA"

conn = sqlite3.connect(SmPCsPath + 'SmPCs.db')

#
# humanMedicinesOP = pd.read_sql("""SELECT * FROM emaMedicinesOP WHERE Category = 'Human';""", conn)
# humanMedicinesOPAuthorised = pd.read_sql(
#     """SELECT * FROM emaMedicinesOP WHERE Category = 'Human' AND [Authorisation status] = 'Authorised';""", conn)
# humanMedicinesOPAuthorisedFirstPublishedAfter2015 = pd.read_sql("""SELECT * FROM emaMedicinesOP WHERE [First Published] LIKE "23/02/2017;""""", conn)
# humanMedicinesOPAuthorisedFirstPublishedAfterRegex = pd.read_sql("""SELECT * FROM emaMedicinesOP WHERE [First Published] REGEXP "[0-3][0-9]\/[0-1][0-9]\/(2017)""""", conn)

# tabulatedADRs = pd.read_sql(""""SELECT excerptText, citationId FROM smpcs WHERE citationSource='eu-ema' AND excerptText REGEXP "Tabulated list of adverse reactions"
# """, conn)

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
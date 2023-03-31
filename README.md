# SmPCs for PrescIT
This series of scripts is used to download and process SmPCs from the EMA website. The scripts are written in Python 3.6. The scripts are used to create a database with the SmPCs and to create a monitoring Excel file.
The European public assessment reports (EPARs) are full scientific assessment reports of medicines authorised at a European Union level. 
EPARs also contain a public-friendly overview in question-and-answer format and the package leaflet, otherwise known as the Summary of Product Characteristics.
Information on medicines that have been refused a marketing authorisation or that have been suspended or withdrawn after being approved is also listed here. 
Since EPARs are periodically updated, the information contained in this repository may not reflect the current state of the medicine.
The EPARs are available on the EMA website: https://www.ema.europa.eu/en/medicines/download-medicine-data.

To do this, the following steps need to be taken:

**Step 1:** Download the lists of medicines from the EMA website (https://www.ema.europa.eu/) and save them in a database.

Two separate files need to be downloaded:

a) The file listing all medicines, including the withdrawn and not authorised ones, named *Medicines_output_european_public_assessment_reports.csv*, found here:
https://www.ema.europa.eu/sites/default/files/Medicines_output_european_public_assessment_reports.xlsx

and

b) The file listing all the URLs for the SmPCs, named *Product information URLs for member states.xls*, found here:
https://www.ema.europa.eu/documents/product-information/product-information-urls-member-states_en.xls

***Make sure that you place the two files in the Data/SmPCs folder.***

Run the 
**Step 2:**

## Links to EMA's EPARs

# c/p from deliverable

#DB with SmPCs Data folder structure explanation
Script #1: csvs to sqlite to add data to db
Script #1a: smpcsDB_IE ???
Script #2: download EMApdfs.py
Script #3: EMAStats.py
Script #4: textileToHTMLconversion.py
Script #5: table extractionPython
-- Explain directories
Script #6: checkEmptyDirectories
Script #7: determineTableStructureSaveToJSON
Script #8: monitoringExcelFile


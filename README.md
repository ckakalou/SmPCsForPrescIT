# SmPCs for PrescIT
This series of scripts is used to download and process SmPCs from the EMA website. The scripts are written in Python 3.6. The scripts are used to create a database with the SmPCs and to create a monitoring Excel file.
The European public assessment reports (EPARs) are full scientific assessment reports of medicines authorised at a European Union level. 
EPARs also contain a public-friendly overview in question-and-answer format and the package leaflet, otherwise known as the Summary of Product Characteristics.
Information on medicines that have been refused a marketing authorisation or that have been suspended or withdrawn after being approved is also listed here. 
Since EPARs are periodically updated, the information contained in this repository may not reflect the current state of the medicine.
The EPARs are available on the EMA website: https://www.ema.europa.eu/en/medicines/download-medicine-data.

To do this, the following steps need to be taken:

**Step 1: Download EPARs from the EMA website** 

Download the lists of medicines from the EMA website (https://www.ema.europa.eu/) and save them in a database.

Two separate files need to be downloaded:

a) The file listing all medicines, including the withdrawn and not authorised ones, named *Medicines_output_european_public_assessment_reports.csv*, found here:
https://www.ema.europa.eu/sites/default/files/Medicines_output_european_public_assessment_reports.xlsx

and

b) The file listing all the URLs for the SmPCs, named *Product information URLs for member states.xls*, found here:
https://www.ema.europa.eu/documents/product-information/product-information-urls-member-states_en.xls

The Excel files need to be converted to csv format, after editind out the EMA headers and reporting information.
The files can then be converted using the following commands:

    `read_file = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx', sheet_name='Your Excel sheet name')
    read_file.to_csv (r'Path to store the CSV file\File name.csv', index = None, header=True)`


***Make sure that you place the two files in the Data/SmPCs folder.***

Finally, run the script `csvsToSQLite.py` to add the data to the database.


**Step 2: Select the authorised medicines for human use**

The EMA files contain all medicines for human and veterinary use, including authorised, withdrawn and refused (not authorised) ones. 

Run the script `EMAStats.py` to create a new database with only the authorised medicines.
The actual SmPCs information will be extracted from the `joinedHumanAuthorisedProductURLsONLY.csv` file which contains the URLs for the authorised medicines for human use.

**Step 3: Extract the 4.8**



#DB with SmPCs Data folder structure explanation
Script #1: csvs to sqlite to add data to db
Script #1a: smpcsDB_IE ???
Script #2: download EMApdfs.py
Script #3: EMAStats.py
Script #4:
Script #5: table extractionPython
-- Explain directories
Script #6: checkEmptyDirectories
Script #7: determineTableStructureSaveToJSON
Script #8: monitoringExcelFile


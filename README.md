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

**Step 3: Extract the "Tabulated Summary of Adverse Reactions" from the 4.8 section "Undesirable Effects".**

Run the script `tableExtractionPython.py` to extract the table from the SmPCs. 
The script will create a new folder for each medicine and save the table as a csv file in the folder, all under the . 
The script will also create a new folder for the tables that could not be extracted.

**Step 4: Check whether there are any empty directories**
The script `checkEmptyDirectories.py` will check if there are any empty directories where the tables could not be extracted and count the number to be able to monitor the progress.

**Step 5: Determine the structure of the tables and save the structure to a JSON file.**
The script `determineTableStructureSaveToJSON.py` will determine the structure of the tables and save the structure to a JSON file. 
However, due to the huge diversity in the structure of the tables, the script will not be able to determine the structure of all the tables.
So far, for the first medications on the list, a dedicated python script has been written to determine the structure of the table for each medication/pdf file.

**Step 6: Create a monitoring Excel file**
The script `createMonitoringExcelFile.py` will create a monitoring Excel file with the following columns: 
"medicationName", "tableFound", "typeOfTable", "jsonFormat" so that the current status of the tables can be monitored.


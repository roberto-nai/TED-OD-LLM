# Tenders Electronic Daily texts - Bids Opening
![PyPI - Python Version](https://img.shields.io/badge/python-3.12-3776AB?logo=python)    

This project takes into account the Italian texts of the tenders on the Tenders Electronic Daily (TED) portal and extracts the date of the bids-opening event in the "Tender Opening Method" section, using LLM capabilities.  
TED portal main page: [https://ted.europa.eu/en/](https://ted.europa.eu/en/).   

## TED Open Data - Documentation
TED CSV open data NOTES & CODEBOOK (PDF): [https://data.europa.eu/api/hub/store/data/ted-csv-data-information-v3-6.pdf](https://data.europa.eu/api/hub/store/data/ted-csv-data-information-v3-6.pdf)  
TED CSV open data Advanced notes on methodology (PDF): [http://data.europa.eu/euodp/en/data/storage/f/2022-02-14T122830/TED_advanced_notes_vers_0.92.pdf](http://data.europa.eu/euodp/en/data/storage/f/2022-02-14T122830/TED_advanced_notes_vers_0.92.pdf)  

## TED Open Data - Download
Sample URL with a PDF: [https://ted.europa.eu/it/notice/2872-2016/pdf](https://ted.europa.eu/it/notice/2872-2016/pdf)  
The 2016 - 2022 sample files (in Italian) are also available in a public Drive here: [https://bit.ly/3QBxdC3](https://bit.ly/3QBxdC3). Download the PDFs in the ```GUUE_DIR``` directory.     

## > Script Execution
```01_read_pdf.ipynb```  
Reads the PDFs and extracts the portion of text contained in the section 'Modalità di apertura delle offerte'; the texts are saved in a CSV file.      
```02_read_date_OPENAI.ipynb```  
For each text in the CSV extracted in the script ```01_read_pdf.ipynb```, it requests the LLM to identify the date. Use OpenAI models.  
```02_read_date_HUGCHAT.ipynb```  
For each text in the CSV extracted in the script ```01_read_pdf.ipynb```, it requests the LLM to identify the date. Use HuggingChat supported by HuggingFace.  
For ```02_*``` scripts, set ```BID_SAMPLE_SIZE``` in the ```config.yml``` file to apply LLM to only one sample out of the total. If ```BID_SAMPLE_SIZE``` is 0, LLM will be applied to the entire dataset.  

## > Script Dependencies
See ```requirements.txt``` for the required libraries (```pip install -r requirements.txt```).  
Create the ```.env``` in the root directory of the project.   
To use OpenAI, save your Open AI API key (```OPENAI_API_KEY="..."```) in the ```.env``` file.  
To use HuggingChat, subscribe to HuggingFace then save the login (```HC_EMAIL="..."```) and password (```HC_PASS="..."```) in the ```.env``` file.  
NOTE: HuggingChat has a login and query limit, so a ```time.sleep()``` was applied to avoid request blocking problems.    

## > Directories
```anac_cig```  
Directory with ANAC tender's CIG to be searched in the PDFs.  
```config```  
Directory with the configuration file in YAML format (```config.yml```) and script to read it (```config_reader.py```).   
```data```  
Data created from PDFs in ```guue```.  
```guue```    
Directory of TED texts in PDF format.  

## Other projects
This project is also related to: [https://github.com/roberto-nai/TED-OD-EVENTLOG](https://github.com/roberto-nai/TED-OD-EVENTLOG)  

## Share
If you use it, please cite:    
```
@InProceedings{10.1007/978-3-031-47112-4_17,
author="Nai, Roberto
and Sulis, Emilio
and Genga, Laura",
editor="Sales, Tiago Prince
and Ara{\'u}jo, Jo{\~a}o
and Borbinha, Jos{\'e}
and Guizzardi, Giancarlo",
title="Automated Analysis with Event Log Enrichment of the European Public Procurement Processes",
booktitle="Advances in Conceptual Modeling",
year="2023",
publisher="Springer Nature Switzerland",
address="Cham",
pages="178--188",
isbn="978-3-031-47112-4"
}
``` 
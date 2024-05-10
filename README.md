# Tenders Electronic Daily texts - Bids Opening
![PyPI - Python Version](https://img.shields.io/badge/python-3.12-3776AB?logo=python)    

This project takes into account the Italian texts of the tenders on the Tenders Electronic Daily (TED) portal and extracts the date of the bids-opening event in the "Tender Opening Method" section, using LLM capabilities.  

## TED Open Data - Download
Sample URL with a PDF: [https://ted.europa.eu/it/notice/2872-2016/pdf](https://ted.europa.eu/it/notice/2872-2016/pdf)  
The 2016 - 2022 sample files (in Italian) are also available in a public Drive here: [https://bit.ly/3QBxdC3](https://bit.ly/3QBxdC3). Download the PDFs in the ```guue``` directory.     

## > Script Execution
```01_read_pdf.ipynb```  
Reads the PDFs and extracts the portion of text contained in the section 'Modalità di apertura delle offerte'; the texts are saved in a CSV file.      
```02_read_date.ipynb```  
For each text in the CSV extracted in the script ```01_read_pdf```, it requests the LLM to identify the date.  
NOTE (1): see ```requirements.txt``` for the required libraries (```pip install -r requirements.txt```).   
NOTE (2): create the ```.env``` file with your Open AI API key in it (```OPENAI_API_KEY="..."```).  

## > Directories
```config```  
Directory with the configuration file in YAML format (```config.yml```) and script to read it (```config_reader.py```).   
```data```  
Data created from PDFs in ```guue```.  
```guue```    
Directory of TED texts in PDF format. 

## > Share
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
## DRT Program
This project contains three below files:
1. DRT.py:
    I have created this file as a Model class for DRT containing its attribute list
2. db.py:
    This file is used for interacting with db. I have used sqlite3 which will create a .db file and create a table namely DRT. This file contains method for inserting the values in the DRT table and returning all the saved DRTs.
3. main.py:
    This files contains the driver program of the project.
    This files contains the method for scraping of all the DRTs according to the provided party_name.

## Prerequisites
    Libraries used:
    1. requests
    2. pytesseract
    3. BeautifulSoup
    
## Running the project
    Simply run the below command :
    ```
    python main.py
    ```

### sample output
```
[(' 247/2021', ' OA', ' OA/153/2021', ' 26/03/2021', 'TAMILNAD MERCANTILE BANK LIMITED', 'SHARMI  CO', '', ''), (' 9416/2017', ' OA', ' OA/388/2017', ' 12/05/2017', 'BANK OF INDIA', 'SHANTHI', '', ''), (' 285/2021', ' MA', ' MA/31/2021', ' 19/04/2021', 'STATE BANK OF INDIA', 'SHAMSHAD BEGUM B', '', ''), (' 81/2021', ' OA', ' OA/257/2021', ' 30/01/2021', 'SOUTH INDIAN BANK', 'SHAHUL HAMEED SNKM', 
'', ''), (' 9657/2017', ' OA', ' OA/615/2017', ' 10/10/2017', 'STATE BANK OF INDIA', 'SHANNUGASUNDRAM', '', ''), (' 42/2020', ' SA', 
' SA/30/2020', ' 16/01/2020', 'SHANMUGADURAI', 'ASREC INDIA LTD', '', ''), (' 480/2019', ' OA', ' OA/24/2020', ' 06/11/2019', 'CORPORATION BANK', 'SHATAKSHI ENTERPRISES', 'S SETHURAMAN', ''), (' 9014/2006', ' OA', ' OA/537/2007', ' 06/10/2006', 'INDIAN BANK', 'SHANTILAL JAIN', '', ''), (' 529/2019', ' SA', ' SA/211/2019', ' 28/11/2019', 'SHAKTHIVEL NADANASABABADY', 'BANK OF INDIA', '', ''), (' 571/2019', ' OA', ' OA/11/2021', ' 17/12/2019', 'THE COSMOS CO OPERATIVE BANK LTD', 'SHANKAR ASSOCIATES S', '', ''), (' 574/2019', ' OA', ' OA/70/2020', ' 18/12/2019', 'PUNJAB NATIONAL BANK', 'SHANKAR G', '', ''), (' 171/2020', ' MA', ' MA/26/2020', ' 03/03/2020', 'STATE BANK OF INDIA', 'SHANNUGASUNDRAM', '', ''), (' 80/2021', ' SA', ' SA/42/2021', ' 29/01/2021', 'SHASHI MODE', 'EDELWEISS ASSET RECONSTRUCTION COMPANY LTD', '', ''), (' 342/2020', ' OA', ' OA/163/2020', ' 07/08/2020', 'SOUTH INDIAN BANK', 'SHARMILA TRADERS', '', ''), (' 477/2021', ' OA', ' Case Not Registered', ' 20/08/2021', 'PUNJAB NATIONAL BANK (ORIENTAL BANK OF COMMERCE)', 'SHANTHIM', 'REGHU RAJA P', ''), (' 9026/2008', ' OA', ' OA/229/2008', ' 01/08/2008', 'PUNJAB NATIONAL BANK', 'SHARAPPA EXPORTS PVT LTD', '', ''), (' 
9046/2008', ' OA', ' OA/315/2008', ' 09/05/2008', 'CENTRAL BANK OF INDIA', 'SHABIR AHMED', '', ''), (' 9393/2015', ' SA', ' SA/243/2015', ' 24/03/2015', 'SHAHANA KHATOON PROP NEW RAB WEIGH BRIDGE', 'STATE BANK OF INDIA', '', ''), (' 641/2019', ' OA', ' OA/204/2021', ' 01/05/2019', 'STATE BANK OF INDIA', 'SHAMSHAD BEGUM BB', '', ''), (' 192/2021', ' OA', ' Case Not Registered', ' 10/03/2021', 'INDIAN OVERSEAS BANK', 'SHALINI PAPER MACKERS', 'P H VINODH PANDIAN', ''), (' 9896/2014', ' OA', ' OA/603/2014', ' 07/07/2014', 'STATE BANK OF INDIA', 'SHANTHI TRACTORS', '', '')]
```

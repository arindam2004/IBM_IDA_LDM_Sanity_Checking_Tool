{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;\f1\fnil\fcharset0 AppleColorEmoji;\f2\fnil\fcharset0 Georgia;
\f3\froman\fcharset0 Times-Bold;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red246\green246\blue249;\red0\green0\blue255;
}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c97255\c97255\c98039;\cssrgb\c0\c0\c100000;
}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl336\slmult1\sa120\partightenfactor0

\f0\fs18 \cf2 \cb3 # IBM IDA LDM Sanity Checking Tool\uc0\u8232 \u8232 A GUI-based Python utility for validating IBM InfoSphere Data Architect (IDA) Logical Data Model (LDM) and Naming Standard Model (NDM) XML files. The tool helps data architects and modelers quickly identify common compliance issues in data models and generates a detailed sanity report.\u8232 \u8232 ---\u8232 \u8232 ## 
\f1 \uc0\u10024 
\f0  Features\uc0\u8232 \u8232 - **Domain and Data Type Extraction:** Lists all domain values and their base data types used in the LDM.\u8232 - **Attribute Length Check:** Identifies columns with names longer than 30 characters.\u8232 - **Abbreviation Compliance:** Detects missing abbreviations in the NDM file for attribute names.\u8232 - **Description Completeness:** Flags attributes that lack descriptions.\u8232 - **Domain Usage Check:** Finds attributes not assigned to a domain.\u8232 - **Comprehensive Report:** Outputs all findings to a timestamped text file.\u8232 - **User-Friendly GUI:** Simple Tkinter interface for file selection and report generation.\u8232 \u8232 ---\u8232 \u8232 ## 
\f1 \uc0\u55357 \u56741 \u65039 
\f0  How to Use\uc0\u8232 \u8232 1. **Requirements**\u8232    - Python 3.x\u8232    - Standard libraries: `tkinter`, `xml.dom.minidom`, `json`, `datetime`, `re`\u8232 \u8232 2. **Run the Tool**\u8232 
\f2\fs21 \
\pard\pardeftab720\sl360\slmult1\sa210\partightenfactor0

\f0 \cf2 \cb1 python IBM_IDA_Compliance_Check.py
\f2 \
\pard\pardeftab720\sl336\slmult1\sa157\partightenfactor0

\f0\fs18 \cf2 \cb3 \uc0\u8232 3. **Using the GUI**\u8232 - Enter the full path to your IBM IDA LDM XML file.\u8232 - Enter the full path to your IBM IDA NDM XML file.\u8232 - Click **Submit** to run the checks and generate the report.\u8232 - The output report will be saved in the current directory with a name like:\u8232   ```\u8232   IDA LDM Sanity Report_DD Month YYYY-HH MM SS.txt\u8232   ```\u8232 - Click **Quit** to close the tool.\u8232 \u8232 ---\u8232 \u8232 ## 
\f1 \uc0\u55357 \u56523 
\f0  What the Report Includes\uc0\u8232 \u8232 - **Domain Values Used In The Model:**  \u8232 All domains and their base types.\u8232 \u8232 - **Columns Which Are More Than 30 Characters Long:**  \u8232 List of attribute names exceeding 30 characters.\u8232 \u8232 - **Names For Which Abbreviations To Be Added in NDM File:**  \u8232 Attribute name parts missing abbreviations in the NDM.\u8232 \u8232 - **List Of Attributes Where No Description is Present:**  \u8232 Attributes without a description.\u8232 \u8232 - **List Of Attributes Where No Domain is Used:**  \u8232 Attributes not assigned to any domain.\u8232 \u8232 ---\u8232 \u8232 ## 
\f1 \uc0\u55357 \u57056 \u65039 
\f0  Code Structure\uc0\u8232 \u8232 - **GUI Section:** Built with Tkinter for easy file selection and operation.\u8232 - **XML Parsing:** Uses `xml.dom.minidom` to extract and analyze model metadata.\u8232 - **Checks Implemented:**\u8232 - Domain extraction\u8232 - Attribute length validation\u8232 - Abbreviation presence (via regex and NDM cross-check)\u8232 - Description presence\u8232 - Domain assignment\u8232 \u8232 - **Output:**  \u8232 All results are written to a human-readable text file with JSON-formatted sections.\u8232 \u8232 ---\u8232 \u8232 ## 
\f1 \uc0\u55357 \u56550 
\f0  Sample Output\uc0\u8232 \u8232 
\f2\fs21 \
\pard\pardeftab720\sl270\slmult1\sa157\partightenfactor0

\f3\b\fs39 \cf2 \cb1 Domain Values Used In The Model:
\f2\b0\fs21 \

\f3\b\fs39 \{\uc0\u8232 "DomainName1": "BaseType1",\u8232 "DomainName2": "BaseType2"\u8232 \}\u8232 Columns Which Are More Than 30 Characters Long:
\f2\b0\fs21 \

\f3\b\fs39 ["VeryLongAttributeNameExceedingThirtyCharacters"]\uc0\u8232 Names For Which Abbreviations To Be Added in NDM File:
\f2\b0\fs21 \

\f3\b\fs39 ["Customer", "Account"]\uc0\u8232 List Of Attributes Where No Description is Present:
\f2\b0\fs21 \

\f3\b\fs39 ["AttributeWithoutDescription"]\uc0\u8232 List Of Attributes Where No Domain is Used:
\f2\b0\fs21 \
\pard\pardeftab720\sl360\slmult1\sa210\partightenfactor0

\f0 \cf2 ["AttributeWithoutDomain"]
\f2 \
\pard\pardeftab720\sl336\slmult1\sa120\partightenfactor0

\f0\fs18 \cf2 \cb3 \uc0\u8232 ---\u8232 \u8232 ## 
\f1 \uc0\u55357 \u56420 
\f0  Author\uc0\u8232 \u8232 - **Arindam Banerjee**\u8232 - Email: {\field{\*\fldinst{HYPERLINK "mailto:arindam.banerjee.in@gmail.com"}}{\fldrslt 
\f2\fs21 \cf4 \ul \ulc4 arindam.banerjee.in@gmail.com}}\uc0\u8232 \u8232 ---\u8232 \u8232 ## 
\f1 \uc0\u55357 \u56541 
\f0  License\uc0\u8232 \u8232 This tool is provided as-is for internal and educational use. For commercial or enterprise usage, please contact the author.\u8232 \u8232 ---\u8232 \u8232 ## 
\f1 \uc0\u55357 \u56911 
\f0  Acknowledgements\uc0\u8232 \u8232 - Developed for IBM InfoSphere Data Architect users and data modeling practitioners.\u8232 \u8232 ---\u8232 }
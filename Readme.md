# IBM IDA LDM Sanity Checking Tool

A GUI-based Python utility for validating IBM InfoSphere Data Architect (IDA) Logical Data Model (LDM) and Naming Standard Model (NDM) XML files. The tool helps data architects and modelers quickly identify common compliance issues in data models and generates a detailed sanity report.

---

## ✨ Features

- **Domain and Data Type Extraction:** Lists all domain values and their base data types used in the LDM.
- **Attribute Length Check:** Identifies columns with names longer than 30 characters.
- **Abbreviation Compliance:** Detects missing abbreviations in the NDM file for attribute names.
- **Description Completeness:** Flags attributes that lack descriptions.
- **Domain Usage Check:** Finds attributes not assigned to a domain.
- **Comprehensive Report:** Outputs all findings to a timestamped text file.
- **User-Friendly GUI:** Simple Tkinter interface for file selection and report generation.

---

## 🖥️ How to Use

1. **Requirements**
   - Python 3.x
   - Standard libraries: `tkinter`, `xml.dom.minidom`, `json`, `datetime`, `re`

2. **Run the Tool**

python IBM_IDA_Compliance_Check.py

3. **Using the GUI**
- Enter the full path to your IBM IDA LDM XML file.
- Enter the full path to your IBM IDA NDM XML file.
- Click **Submit** to run the checks and generate the report.
- The output report will be saved in the current directory with a name like:
  ```
  IDA LDM Sanity Report_DD Month YYYY-HH MM SS.txt
  ```
- Click **Quit** to close the tool.

---

## 📋 What the Report Includes

- **Domain Values Used In The Model:**  
All domains and their base types.

- **Columns Which Are More Than 30 Characters Long:**  
List of attribute names exceeding 30 characters.

- **Names For Which Abbreviations To Be Added in NDM File:**  
Attribute name parts missing abbreviations in the NDM.

- **List Of Attributes Where No Description is Present:**  
Attributes without a description.

- **List Of Attributes Where No Domain is Used:**  
Attributes not assigned to any domain.

---

## 🛠️ Code Structure

- **GUI Section:** Built with Tkinter for easy file selection and operation.
- **XML Parsing:** Uses `xml.dom.minidom` to extract and analyze model metadata.
- **Checks Implemented:**
- Domain extraction
- Attribute length validation
- Abbreviation presence (via regex and NDM cross-check)
- Description presence
- Domain assignment

- **Output:**  
All results are written to a human-readable text file with JSON-formatted sections.

---

## 📦 Sample Output


Domain Values Used In The Model:
{
"DomainName1": "BaseType1",
"DomainName2": "BaseType2"
}
Columns Which Are More Than 30 Characters Long:
["VeryLongAttributeNameExceedingThirtyCharacters"]
Names For Which Abbreviations To Be Added in NDM File:
["Customer", "Account"]
List Of Attributes Where No Description is Present:
["AttributeWithoutDescription"]
List Of Attributes Where No Domain is Used:
["AttributeWithoutDomain"]

---

## 👤 Author

- **Arindam Banerjee**
- Email: arindam.banerjee.in@gmail.com

---

## 📝 License

This tool is provided as-is for internal and educational use. For commercial or enterprise usage, please contact the author.

---

## 🙏 Acknowledgements

- Developed for IBM InfoSphere Data Architect users and data modeling practitioners.

---

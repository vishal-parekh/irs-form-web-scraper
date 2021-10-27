# IRS Form Web Scraper
Search and download utilities for IRS Prior Year Products web page. 

# Python Version

Python 3.8.9

# Pip Version

pip 20.2.3 (from Python3 version above)

If pip (or pip3 for Python3 is not installed, please download and install now:

    First, download get-pip.py from [Link](https://bootstrap.pypa.io/get-pip.py).

    Then, open a terminal/command prompt, cd to the folder containing the get-pip.py file and run:
        Mac/Linux: python get-pip.py
        Windows: py get-pip.py

# Project Setup and Dependencies

  * cd into root of project folder
  
  * Note: Best practice is to create and use virtual environment (venv module is part of the standard Python library so no external  installation is necessary):
    ```
    python -m venv <name_of_virtualenv>
    ```
  * Activate virtual environment:
      ```
    source <name_of_virtualenv>/bin/activate
    ```

  * Install requirements.txt file:
    ```
    pip install -r requirements.txt 
    ```

# Script Input
  ## Utility to search tax form names and return informational results:
  * While in the root of the project folder, run the [searchIrsTaxForms.py](./searchIrsTaxForms.py) file. The script will prompt you to enter which form you would like to search. The program is designed to accept either a single form number string that contains the exact form number or multiple form number strings separated by commas (with or without spaces). Do not include quotation marks in either inputs. Inputs are already assumed to be of type string. Any whitespace will be stripped. Some examples of form numbers include, "Form W-2," "Form W-2 P," "Publ 1," and "Publ 15-A." 
    * Sample input for single form number search:
      ```
      Please enter which form you would like to search (Only plain text without quotations allowed. Multiple form types allowed with comma as required delimiter.): Form W-2   
      ```
    * Sample input for multiple form number search:
      ```
      Please enter which form you would like to search (Only plain text without quotations allowed. Multiple form types allowed with comma as required delimiter.): Form W-2, Form W-2 P, Publ 1
      ```

  ## Utility to search tax form names and download forms in PDF format:
  * While in the root of the project folder, run the [downloadIrsTaxForms.py](./downloadIrsTaxFormPDFs.py) file. The script will prompt you to enter which form you would like to search, the minimum year, and maximum year for the range. The program is designed to accept a single string that contains the exact form number. Some examples of form numbers include, "Form W-2," "Form W-2 P," "Publ 1," and "Publ 15-A." The logic in the program also assumes that your input years are valid for the searched form number.
    * Sample input for single form number search:
      ```
      Please enter which form you would like to search (single and multiple form types allowed): Form W-2

      Please type the mininum year for the range: 1990

      Please type the maximum year for the range: 2020
      ```


# Script Output
  ## Utility to search tax form names and return informational results:
  * The expected output should be the list of correct json data returned in the terminal.
  
  ## Utility to search tax form names and download forms in PDF format:
  * The expected output is a new subdirectory in the root of the project named as the tax form name that was searched. The subdirectory includes all PDF files with the naming convention as "Form Name" - "Year" for each respective form downloaded.


# Next steps and feedback on coding challenge
Some of the next steps for improving both utility script sis to update and refactor the code to handle errors for an invalid year range and invalid form number inputs.
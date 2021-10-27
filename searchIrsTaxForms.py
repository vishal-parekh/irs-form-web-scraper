from datetime import date
from io import StringIO
import requests
import json
from bs4 import BeautifulSoup

# Retrieve current date to use year as maxYear in range
current_date = date.today()

#Prompt to take required form number input
irs_Search_Term = input("Please enter which form you would like to search (Only plain text without quotations allowed. Multiple form types allowed with comma as required delimiter.): ")
searchList = irs_Search_Term.split(",")

# Declare an empty list to eventually store list of lists for multiple form types
listOfSingleAndMulitpleFormTypes= []

for j in searchList: 
    # Declare an empty list to eventually store single list of forms one type at a time
    listOfForms = []

    # Declare and initialize url formatted to dynamically add irs_Search_Term to make GET request in next lines.
    url = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value={j.strip()}&isDescending=false'

    # Declare and initialize BeautifulSoup variable to parse (html) GET request made in previous lines.
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Declare and initialize desired table to iterate through
    table = soup.find_all(class_='picklist-dataTable')[0]
    records = table.find_all('tr')

    # Create a class to format/clean required data from web scraping.  
    class formatterClass:
        def __init__(self, form_number, form_title, min_year, max_year):
            self.form_number = form_number.strip()
            self.form_title = form_title.strip()
            self.min_year = min_year.strip()
            self.max_year = max_year

        # Method to represent objects of this class as string
        def __repr__(self):
            return json.dumps({"form_number": self.form_number, "form_title": self.form_title,"min_year": self.min_year,"max_year": self.max_year}, indent=4)

    # Iterate through records
    for i in records:
        # Declare and initialize LeftCellSpacer, MiddleCellSpacer, and EndCellSpacer classes in picklistTable div.
        # After if statement and try/except blocks, we can retrieve new values of these variables.
        form_number = 'Form Number Placeholder'
        form_title = 'Form Title Placeholder'
        min_year = 'Min Year Placeholder'
        max_year = 'Max Year Placeholder'

        # If condition to  retrieve form_number records that match exactly with the irs_Search_Term input.
        # For Example, the input "Form W-2" will only return exact "Form W-2" results.
        # This is to ensure proper handling of expected final results because the IRS web page
        # will return search terms whose strings end differently like "Form W-2 P" or "Form W-2GU"
        if (i.find('a').contents[0] == j.strip()):
                form_number = i.find('a').contents[0]
                try:
                    form_title = i.find(class_='MiddleCellSpacer').get_text()
                except AttributeError:
                    print ("")
                try:
                    min_year = i.find(class_='EndCellSpacer').get_text()
                except AttributeError:
                    print ("")
                max_year = current_date.year

        if form_title != 'Form Title Placeholder':
            # If not true, append object to list because the variable was updated.
            listOfForms.append(formatterClass(form_number, form_title, min_year, max_year))
    listOfSingleAndMulitpleFormTypes.append(listOfForms)

print(listOfSingleAndMulitpleFormTypes)


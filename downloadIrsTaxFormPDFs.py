import os
import requests
from bs4 import BeautifulSoup

#Prompts to take required inputs
irs_Search_Term = input("Please type exactly which form you would like to download (only one type of form can be downloaded at a time): ")

min_year_input = input("Please type the mininum year for the range: ")

max_year_input = input("Please type the maximum year for the range: ")

# Declare and initialize url formatted to dynamically add irsSearchTerm to make GET request in next lines.
url = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value={irs_Search_Term}&isDescending=false'

# Declare and initialize BeautifulSoup variable to parse (html) GET request made in previous lines.
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Declare and initialize desired table to iterate through
table = soup.find_all(class_='picklist-dataTable')[0]
records = table.find_all('tr')

# Declare an empty list to eventually store list of forms 
listOfForms = []

# Create a class to format/clean required data from web scraping.  
class formatterClass:
    min_year = min_year_input.strip
    max_year = max_year_input
    def __init__(self, form_number, form_title, min_year, max_year, pdf):
        self.form_number = form_number.strip()
        self.form_title = form_title.strip()
        self.min_year = min_year.strip()
        self.max_year = max_year
        self.pdf = pdf.strip()

# Iterate through records
for i in records:
    # Declare and initialize LeftCellSpacer, MiddleCellSpacer, and EndCellSpacer classes in picklistTable div.
    # After if statement and try/except blocks, we can retrieve new values of these variables.
    form_number = 'Form Number Placeholder'
    form_title = 'Form Title Placeholder'
    min_year = 'Min Year Placeholder'
    max_year = 'Max Year Placeholder'
    pdf = 'PDF Placeholder'

    # If condition to  retrieve form_number records that match exactly with the irs_Search_Term input.
    # For Example, the input "Form W-2" will only return exact "Form W-2" results.
    # This is to ensure proper handling of expected final results because the IRS web page
    # will return search terms whose strings end differently like "Form W-2 P" or "Form W-2GU"
    if (i.find('a').contents[0] == irs_Search_Term):
            form_number = i.find('a').contents[0]
            try:
                form_title = i.find(class_='MiddleCellSpacer').get_text()
            except AttributeError:
                    print ("")
            try:
                min_year = i.find(class_='EndCellSpacer').get_text()
            except AttributeError:
                print ("")
            try:
                pdf = i.find('a', href=True).get('href')
            except AttributeError:
                print ("")

    # If statement to check if required data point was assigned over original placeholder value.
    if form_title != 'Form Title':
        # If not true, append object to list because the variable was updated.
        listOfForms.append(formatterClass(form_number, form_title, min_year, max_year, pdf))
    
print("\nPlease wait. Downloading " + irs_Search_Term + " PDFs from " + min_year_input + " to " + max_year_input + "....")

#Function to go through listOfForms to download to respective folders with required file naming convention
def get(min, max):
    if not os.path.exists('./' + irs_Search_Term):
        os.makedirs('./' + irs_Search_Term)
    for i in listOfForms:
        if min <= i.min_year and max >= i.min_year:
            url = i.pdf
            r = requests.get(url)
            subdirectoryPath = './' + irs_Search_Term + '/' + i.form_number+" - "+i.min_year+".pdf"
            with open(subdirectoryPath, 'wb') as f:
                f.write(r.content)

get(min_year_input, max_year_input)

print("\nPDFs successfully downloaded in " + "'" + irs_Search_Term + "'" + " subfolder\n")

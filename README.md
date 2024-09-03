Documentation for Web Scraping Script
This Python script is designed to scrape product information from the Rozetka website, specifically targeting the notebooks category. The script collects details such as product name, product link, new price, and old price, and saves this data into a CSV file.

Requirements
To run this script, you need Python 3.x installed on your machine. Additionally, you will need the following libraries:

requests: For making HTTP requests to fetch web pages.
BeautifulSoup from the bs4 library: For parsing HTML and extracting data.
csv: A built-in module for writing data to a CSV file.
You can install the required libraries using pip.

Overview of the Script
The script begins by defining a base URL template for the notebook category pages on the Rozetka website. The template includes a placeholder for the page number, which will be replaced during the scraping process.

Next, the script opens a CSV file named "data.csv" for writing and writes the header row with the specified column names: Count, Product Text, Product Link, New Price, and Old Price.

The main part of the script consists of a loop that iterates through the pages of the notebook category, from page 1 to page 67. For each page, the script makes an HTTP request to fetch the page content and then parses the HTML using BeautifulSoup.

Within each page, the script finds all product tiles and extracts relevant information for each product, including the product name, link, new price, and old price. It handles cases where the old price may not be present by assigning a default value of "N/A".

After extracting the data, the script writes each product's information to the CSV file, incrementing a counter for each entry and printing a message to indicate that the entry has been saved.

Once all pages have been processed, the script prints a final success message indicating that the data has been successfully collected and saved in the CSV file.

Usage
To use this script, ensure that you have Python and the required libraries installed. Run the script in your terminal or command prompt. The data will be saved in "data.csv" in the same directory as the script.

Notes
Users should be mindful of the website's robots.txt file and terms of service regarding web scraping. The script may require adjustments if the website structure changes in the future.

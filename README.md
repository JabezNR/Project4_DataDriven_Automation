Objective:
The main goal is to automate the testing processes on the Moneycontrol website using a data-driven approach, with input values sourced from a MySQL database and from Excel Sheet.

Process Breakdown:
Launch Browser: Initialize a browser session using Selenium WebDriver.

Navigate to Moneycontrol: Direct the browser to the Moneycontrol website.

Read Data from Excel/MySQL: Use Python libraries like  openpyxl/mysql-connector-python to read data from an Excel spreadsheet / MySQL Tables.

Execute Test Cases:

Login: If needed, automate the login process using credentials from Excel.

Perform Actions: Automate tasks like searching for stocks, retrieving financial data, or validating displayed information using inputs from the Excel sheet.

Capture Results: Save the results of each test case, including any discrepancies or errors encountered, for later analysis.

Error Handling: Implement error handling to manage any issues that arise during automation, ensuring robustness.

Close Browser: End the browser session after completing all test cases.

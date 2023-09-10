# File Uploader Task

## Overview

The File Uploader Task is a web application that allows users to register, authenticate, and perform various operations on CSV files. It provides a user-friendly interface for uploading, processing, and manipulating CSV data.


## Features
1. **User Registration and Authentication**: Users can create accounts, log in, and log out using the [allauth](https://django-allauth.readthedocs.io/en/latest/) package, ensuring secure access to the CSV uploader and enabling user-specific functionalities.
2. **CSV File Upload**: Users can easily upload CSV files, supporting comma-separated values, through the user interface.
3. **Data Processing**: The uploaded CSV files can be processed to extract meaningful information. Users can perform operations like filtering, sorting, and data manipulation on the uploaded data.


## Installation

To run the CSV uploader project locally, follow these steps:

1. Clone the repository from GitHub:
   ```bash
   git clone [repository_url]

2. Navigate to the project directory:
bash
>>cd csv-uploader-project

3. Create a virtual environment:
>>python -m venv myenv

4. Activate the virtual environment:
>>myenv/Scripts/activate  # On Windows
>>source myenv/bin/activate  # On macOS and Linux

5. Install the required dependencies:
>>pip install -r requirements.txt


6. Set up the database:
>>configure database in .env file

7. Create Database.
>>create database catalyst_db

8. Perform the migration to create the table
>>python manage.py migrate

9. Start the development server:
>>python manage.py runserver


10. Configuration
**Open the project's settings file: csv_uploader/settings.py.

Locate the INSTALLED_APPS section and ensure that the following apps are included:

#INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    # ... other apps ...
]



##USAGE
1. Register a new account or log in using an existing account.
2. Once logged in, navigate to the CSV uploader section.
3. Click on the "Upload CSV" button and select a CSV file to upload.
4. After the file is uploaded, perform the desired operations on the data.

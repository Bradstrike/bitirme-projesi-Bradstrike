# DataViewer

DataViewer is a simple Python application built with Tkinter for GUI, and MySQL for database. It allows users to load, view, and (for admin users) edit data from CSV files.

## Features

- **User authentication:** Users can login with their credentials. New users can register with a username, password, and role (either 'admin' or 'user').
- **Data loading:** Users can load data from a CSV file.
- **Data viewing:** Users can view the loaded data.
- **Data editing and saving:** Admin users can edit the loaded data and save it to an Excel file.

## Setup and Run

1. Clone the repository to your local machine.
2. Install the required Python packages: pip install -r requirements. txt
3. Run the application:


## Usage

1. Start the application. The login page will appear.
2. Enter your username, password, and role. If you are a new user, click 'Register' to create a new account.
3. Once logged in, you will see the main page. Here you can load a CSV file, view the data, and (if you are an admin) edit the data and save it to an Excel file.
4. To logout, click the 'Logout' button.

## Note

This application is a simple demonstration and not meant for production use. The database connection details are hardcoded, and the password is stored and transmitted in plaintext. In a production application, you would want to secure the database connection and store passwords in a secure manner.
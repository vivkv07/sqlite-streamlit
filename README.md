# SQL Editor on Streamlit using SQLITE
[![Streamlit](https://badgen.net/pypi/v/streamlit)](https://pypi.org/project/streamlit/)
![Example of live coding an app in Streamlit|635x380](https://github.com/vivkv07/sqlite-streamlit/blob/main/data/sqlite_streamlit.gif?raw=true)


The above code is a Python script that uses the Streamlit library to create a web application for working with SQLite databases. The script uses the SQLite library to connect to the database and perform operations such as creating and uploading data to tables.

The script starts by importing the necessary libraries including Streamlit, SQLite3, Pandas, and others.

The first thing the script does is set the page layout, title, and icon of the web application using the st.set_page_config() function. It also sets the title of the page and the caption of the developer.

The script then defines a main() function that contains several other functions. The first function is the create_connection() function, which creates a connection to the SQLite database specified by the 'db_file' parameter.

The next function is the create_database() function, which allows the user to create a new database by specifying a name and clicking a button. The function also displays a list of available databases on the server using the SQLite PRAGMA statement.

The upload_data() function allows the user to upload data to an existing table by specifying the table name and selecting a file to upload. The data is read using the Pandas library and inserted into the specified table.

The script then uses the Streamlit tabs() function to create four tabs: "1 Intro to SQL", "2 Create Database", "3 Upload Data", "4 Query Data". The first tab displays a markdown file with an introduction to SQL, the second tab allows the user to create a new database, the third tab allows the user to upload data to a table, and the fourth tab allows the user to query data from the database.

Overall, the script provides a simple and user-friendly interface for working with SQLite databases using Streamlit and Python.

# SQL Editor on Streamlit using SQLITE
[![Streamlit](https://badgen.net/pypi/v/streamlit)](https://pypi.org/project/streamlit/)


![Example of live coding an app in Streamlit|835x480](https://github.com/vivkv07/sqlite-streamlit/blob/main/data/sqlite_streamlit.gif?raw=true)

Creating a web app that allows users to create and query a database is a great way to make data management more accessible and user-friendly. In this article, we will be building a web app using the Python framework Streamlit and the SQLite3 library. This app will allow users to create a new database file, create tables within the database, and run SQL queries to retrieve data from the tables.

First, we will start by installing Streamlit and SQLite3. To do this, we will use the pip package manager by running the following command in the terminal:

```python
pip install streamlit sqlite3
```
Next, we will import the necessary libraries and create a basic Streamlit app. The following code creates a simple Streamlit app that displays a title and a message on the screen:

```python
import streamlit as st

st.title("SQL Editor")
st.write("Welcome to the SQL Editor app!")
```
Now that we have a basic Streamlit app set up, we can add the functionality to create a new database file. We can do this by using the sqlite3 library to create a new connection to a database file. The following code creates a new database file called "mydatabase.db" and stores it in the current working directory:

```python
import sqlite3

conn = sqlite3.connect("mydatabase.db")
```
We can also use the sqlite3 library to create tables within the database. In this example, we will create a table called "employees" with the columns "id", "name", "email", and "salary":

```python
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    salary REAL
)
""")
conn.commit()
```
Finally, we can use the sqlite3 library to run SQL queries on the tables within the database. In this example, we will retrieve all the data from the "employees" table:

```python
cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()
st.write(results)
```

We can also use the streamlit library to create a user interface where the user can enter their own SQL queries and see the results. For example,

```python 
query = st.text_input("Enter a SQL query")
if st.button("Submit"):
    cursor.execute(query)
    results = cursor.fetchall()
    st.write(results)
    
```
Now, we have a basic web app that allows users to create a new database file, create tables within the database, and run SQL queries to retrieve data from the tables. With a little bit more development, this app can be made more robust, with user authentication and a more user-friendly interface.

In summary, we have seen how to create a web app using Streamlit and SQLite3. The app allows users to create a new database file, create tables within the database, and run SQL queries to retrieve data from the tables. It is a great way to make data management more accessible and user-friendly.
Code is a Python script that uses the Streamlit library to create a web application for working with SQLite databases. The script uses the SQLite library to connect to the database and perform operations such as creating and uploading data to tables.

The script starts by importing the necessary libraries including Streamlit, SQLite3, Pandas, and others.
```python
import streamlit as st
import sqlite3
import pandas as pd
import os
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES
from readme import readme
import  streamlit_toggle as tog
from pathlib import Path
```
The first thing the script does is set the page layout, title, and icon of the web application using the st.set_page_config() function. It also sets the title of the page and the caption of the developer.

```python
st.set_page_config(layout='wide', page_title="Sql Editor", page_icon= "./data/sql.png") 
```
create_connection() function creates a connection to the SQLite database specified by the 'db_file' parameter.

```

The next function is the create_database() function, which allows the user to create a new database by specifying a name and clicking a button. The function also displays a list of available databases on the server using the SQLite PRAGMA statement.

The upload_data() function allows the user to upload data to an existing table by specifying the table name and selecting a file to upload. The data is read using the Pandas library and inserted into the specified table.

The script then uses the Streamlit tabs() function to create four tabs: "1 Intro to SQL", "2 Create Database", "3 Upload Data", "4 Query Data". The first tab displays a markdown file with an introduction to SQL, the second tab allows the user to create a new database, the third tab allows the user to upload data to a table, and the fourth tab allows the user to query data from the database.

Overall, the script provides a simple and user-friendly interface for working with SQLite databases using Streamlit and Python.

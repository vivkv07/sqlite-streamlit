import streamlit as st
import sqlite3
import pandas as pd
import os
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES
from readme import readme
import  streamlit_toggle as tog
from pathlib import Path


st.set_page_config(layout='wide', page_title="Sql Editor", page_icon= "./data/sql.png") 

st.title(" Just enough SQL to get started with Analysis! ")
st.caption(" Developer - Vivek Kovvuru")
st.markdown('''[![Streamlit App](https://badgen.net/pypi/v/streamlit)](https://pypi.org/project/streamlit/)
                [![Github Link](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/vivkv07/sqlite-streamlit.git)
            [![BymeaCoffee](https://badgen.net/badge/icon/buymeacoffee?icon=buymeacoffee&label)](https://www.buymeacoffee.com/vivekkovvuru)''')
st.write("")
st.write("")


def main():
    

    
    
    def create_connection(db_file):
        """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Exception as e:
            st.write(e)

        return conn


    def create_database():
        st.markdown("# Create Database")

        st.info("""A database in SQLite is just a file on same server. 
        By convention their names always must end in .db""")


        db_filename = st.text_input("Database Name")
        create_db = st.button('Create Database')
        
        conn = create_connection('default.db')
        mycur = conn.cursor() 
        mycur.execute("PRAGMA database_list;")
        available_table=(mycur.fetchall())
        with st.expander("Available Databases"): st.write(pd.DataFrame(available_table))
        
        if create_db:
            
            
            if db_filename.endswith('.db'):
                conn = create_connection(db_filename)
                

                st.success("New Database has been Created! Please move on to next tab for loading data into Table.")
            else: 
                st.error('Database name must end with .db as we are using sqlite in the background to create files.')


    def upload_data():
        st.markdown("# Upload Data")
        sqlite_dbs = [file for file in os.listdir('.') if file.endswith('.db')]
        db_filename = st.selectbox('Database', sqlite_dbs)
        table_name = st.text_input('Table Name to Insert')
        conn = create_connection(db_filename)
        uploaded_file = st.file_uploader('Choose a file')
        upload = st.button("Create Table")
        if upload:
            #read csv
            try:
                df = pd.read_csv(uploaded_file)
                df.to_sql(name=table_name, con=conn)
                st.write('Data uploaded successfully. These are the first 5 rows.')
                st.dataframe(df.head(5))

            except Exception as e:
                st.write(e)
    intro, db, tbl, qry = st.tabs(["Intro to SQL","Create Database", "Upload Data", "Query Data"])
    with intro:
        st.write((Path(__file__).parent/"data/sql.md").read_text()) 
    with db:
        create_database()
    with tbl: 
        upload_data()
    with qry:
        sqlite_dbs = [file for file in os.listdir('.') if file.endswith('.db')]
        db_filename = st.selectbox('DB Filename', sqlite_dbs)
        conn = create_connection(db_filename)
        mycur = conn.cursor() 
        mycur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        available_table=(mycur.fetchall())
        st.write("Available Tables")
        st.dataframe(pd.DataFrame(available_table))
        with readme("streamlit-ace"):
            c1, c2 = st.columns([3, 0.5])

            # c2.subheader("Parameters")
            # st.write(LANGUAGES)
            with c2: 
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                dark_mode = tog.st_toggle_switch(label="Dark", 
                            key="darkmode", 
                            default_value=False, 
                            label_after = False, 
                            inactive_color = '#D3D3D3', 
                            active_color="#11567f", 
                            track_color="#29B5E8"
                            )
                if dark_mode: THEME = THEMES[0]
                else: THEME = THEMES[3]
            with c1:
                st.subheader("Query Editor")
                content = st_ace(
                    placeholder="--Select Database and Write your SQL Query Here!",
                    language= LANGUAGES[145],
                    theme=THEME,
                    keybinding=KEYBINDINGS[3],
                    font_size=c2.slider("Font Size", 10, 24, 16),
                    min_lines=15,
                    key="run_query",
                )

                if content:
                    st.subheader("Content")
                    
                    st.text(content)
                    
                    def run_query():
                        query = content
                        conn = create_connection(db_filename)

                        try:
                            query = conn.execute(query)
                            cols = [column[0] for column in query.description]
                            results_df= pd.DataFrame.from_records(
                                data = query.fetchall(), 
                                columns = cols
                            )
                            st.dataframe(results_df)
                            export = results_df.to_csv()
                            st.download_button(label="Download Results", data=export, file_name='query_results.csv' )
                        except Exception as e:
                            st.write(e)

                    run_query()


if __name__ == "__main__":
    main()
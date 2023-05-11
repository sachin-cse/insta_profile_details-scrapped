import csv
import sqlite3
import os
import time


def insert_file(file_path):
    try:
        if file_path.lower().endswith('.csv'):
            with open(file_path, newline = '', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)
                data = [tuple(row) for row in reader]
        else:
            raise ValueError("Unsupported file format. Only .csv files are allowed.")
        
        conn = sqlite3.connect("./database/insta.db")
        cursor = conn.cursor()

        # IF TABLE NOT EXIST
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_details (id INTEGER PRIMARY KEY AUTOINCREMENT,
        Username TEXT NOT NULL,
        User_Id INTEGER,
        Profile_Image TEXT,
        Followers INTEGER,
        Following INTEGER,
        Bio TEXT) 
        ''')

        # insert data into table
        start_time = time.time()

        cursor.executemany('INSERT INTO user_details (Username, User_Id, Profile_Image, Followers, Following, Bio) VALUES (?, ?, ?, ?, ?, ?)', data)
        conn.commit()
        conn.close()

        end_time = time.time()

        execution_time = end_time - start_time
        print('Data added to the database successfully!')
        print(f"Execution time: {execution_time:.2f} seconds")
    except Exception as e:
        print(f"An error occurred: {e}") 




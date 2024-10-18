import os

# 1. Resource leak (File not properly closed)
def read_file(file_path):
    f = open(file_path, "r")  # File is opened but not properly closed
    content = f.read()
    return content

# 2. SQL Injection vulnerability
import sqlite3

def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Directly embedding user input into query without validation
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return result

# 3. Hardcoded credentials
def authenticate():
    username = "admin"
    password = "password123"  # Hardcoded password (bad practice)
    if username == "admin" and password == "password123":
        return True
    else:
        return False

# 4. Insecure use of subprocess
import subprocess

def execute_command(cmd):
    # Insecure call to subprocess without sanitizing input
    result = subprocess.run(cmd, shell=True)  # Potential shell injection
    return result

# 5. Unused variable
def calculate_sum(a, b):
    result = a + b  # The result is calculated but never returned or used
    unused_variable = 42  # Unused variable
